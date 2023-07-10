from flask import Flask, request
from confluent_kafka import Producer
import json
import logging
import sys
import configparser

logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    stream=sys.stdout)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

config = configparser.ConfigParser()
config.read('config.ini')

producer = Producer({'bootstrap.servers':config['broker']['server']})
logger.info('Kafka producer has been initiated...')

def acked(err, msg):
    if err is not None:
        logger.error('Error: {}'.format(err))
    else:
        message = 'Produced message on topic {} with value of {}\n'.format(msg.topic(), msg.value().decode('utf-8'))
        logger.info(message)

app = Flask(__name__)

@app.route('/produce', methods=['POST'])
def produce():
    data = json.dumps(request.get_json())
    producer.produce(config['broker']['topic'], data.encode('utf-8'), callback=acked)
    producer.flush()
    return ('', 200)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
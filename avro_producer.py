from flask import Flask, request
from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
import json
import uuid
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

def load_avro_schema():
    key_schema_string = """
    {"type": "string"}
    """
    
    key_schema = avro.loads(key_schema_string)
    value_schema = avro.load("./schema.avsc")
    
    return key_schema, value_schema

key_schema, value_schema = load_avro_schema()
producer = AvroProducer({'bootstrap.servers':config['broker']['server'],'schema.registry.url':config['broker']['schema_registry']}, 
                        default_key_schema=key_schema, 
                        default_value_schema=value_schema)

app = Flask(__name__)

@app.route('/produce', methods=['POST'])
def produce():
    
    key = str(uuid.uuid4()) # auto-generating key
    value = request.get_json()
    
    topic = config['broker']['topic']
    
    try:
        producer.produce(topic=topic, key=key, value=value)
    except Exception as e:
        logger.error('Exception while producing record value - {} to topic - {}: {}'.format(value, topic, e))
    else:
        logger.info('Successfully producing record value - {} to topic - {}'.format(value, topic))
    
    producer.flush()
    return ('', 200)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
from confluent_kafka import Consumer
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

consumer = Consumer({'bootstrap.servers':config['broker']['server'],'group.id':'kafka-client-consumer','auto.offset.reset':config['consumer']['auto_offset_reset']})
logger.info('Kafka consumer has been initiated...')

logger.info('Available topics to consume: {}'.format(consumer.list_topics().topics))
consumer.subscribe([config['broker']['topic']])

def main():
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            logger.error('Error: {}'.format(msg.error()))
            continue
        data = msg.value().decode('utf-8')
        logger.info('Consumed message: {}'.format(data))
    c.close()

if __name__ == '__main__':
    main()
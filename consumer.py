from kafka import KafkaConsumer
import sys

print('Consumer Started')

var = 1
while var == 1:

    # initialize consumer to topic as name 'test-topic' and broker
    consumer = KafkaConsumer('test-topic',
                            group_id='consumer-1',
                            bootstrap_servers='localhost:9092',api_version=(0,10))
    
    for msg in consumer:
        print('Consuming -> {}'.format(msg))
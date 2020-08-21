from kafka import KafkaConsumer
import sys

print('Consumer Started')
# continuous loop
var = 1
while var == 1:

    # initialize consumer to given topic and broker
    consumer = KafkaConsumer('test-topic',
                            group_id='consumer-1',
                            bootstrap_servers='localhost:9092',api_version=(0,10))

    print('Consuming')
    
    # loop and print messages
    for msg in consumer:
        print (msg.)
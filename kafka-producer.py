import time
import random
from kafka import KafkaProducer
import sys

print('Producer Started')
# give broker IP from docker
producer = KafkaProducer(bootstrap_servers='localhost:9092',api_version=(0,10))

print('Producer Started 2')
# continuous loop
var = 1
while var == 1:

    # generate a random integer
    num = random.randint(0, 10)

    # send to topic on broker
    producer.send('test-topic', key=b'message-two', value=b'This is Kafka-Python')

    print('Sent message')
    # wait 1 second
    time.sleep(1)
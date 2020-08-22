import time
import random
from kafka import KafkaProducer
import sys

print('Producer Started')

producer = KafkaProducer(bootstrap_servers='localhost:9092',api_version=(0,10))

var = 1
while var == 1:

    num = random.randint(0, 10)
    
    # send to topic as name 'test-topic' on broker
    producer.send('test-topic', value=bytes(str(num),encoding='utf-8'))
    
    print('Produced -> {}'.format(num))
    
    time.sleep(2)
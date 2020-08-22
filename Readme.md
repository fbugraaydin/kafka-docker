## Pub/Sub implementation on Kafka with Docker using Python

Simple project to understand Kafka. Publish messages to topic and Consumer that listens topic consumes message.

## Tech/Frameworks

- [Docker] (https://www.docker.com/)
- [Kafka] (https://kafka.apache.org/)
- [Python] (https://www.python.org/)

## Prerequisites

Before everything, install docker: https://docs.docker.com/get-docker/

Install pip to manage packages: https://pip.pypa.io/en/stable/installing/

Next, install **Kafka-Python** using python.
```
pip install kafka-python
```

Change IP with your local IP in docker-compose.yml file.
```
KAFKA_ADVERTISED_HOST_NAME : {YOUR_IP}
```

Locate to project directory and up container as detached mode.
```
docker-compose up -d
```

You see two containers(docker ps) that zookeper & kafka like below:
```
CONTAINER ID        IMAGE                    COMMAND                  CREATED             STATUS              PORTS                                                NAMES
962b30d63d11        wurstmeister/kafka       "start-kafka.sh"         28 seconds ago      Up 27 seconds       0.0.0.0:9092->9092/tcp                               kafka-docker-pub-sub_kafka_1
ef927dd82719        wurstmeister/zookeeper   "/bin/sh -c '/usr/sb…"   28 seconds ago      Up 27 seconds       22/tcp, 2888/tcp, 3888/tcp, 0.0.0.0:2181->2181/tcp   kafka-docker-pub-sub_zookeeper_1
```
Everything is ready to run

## Let's Run

First, run consumer in terminal
```
python consumer.py
```

Second, run producer in another terminal
```
python producer.py
```


## Output

In Producer terminal:
```
Producer Started
Produced -> 6
Produced -> 4
```

In consumer terminal:
```
Consumer Started
Consuming -> ConsumerRecord(topic='test-topic', partition=0, offset=64, timestamp=1598112728866, timestamp_type=0, key=None, value=b'6', headers=[], checksum=568130586, serialized_key_size=-1, serialized_value_size=1, serialized_header_size=-1)
Consuming -> ConsumerRecord(topic='test-topic', partition=0, offset=65, timestamp=1598112730868, timestamp_type=0, key=None, value=b'4', headers=[], checksum=3868220605, serialized_key_size=-1, serialized_value_size=1, serialized_header_size=-1)
```

## Useful Kafka Commands

List topics
```
docker exec -t <kafka-container-name> kafka-topics.sh --bootstrap-server :9092 --list
```

Create Topic
```
docker exec -t <kafka-container-name> kafka-topics.sh --bootstrap-server :9092 --create --topic <topic-name> --partitions 3 --replication-factor 1
```

Describe Topic
```
docker exec -t <kafka-container-name> kafka-topics.sh --bootstrap-server :9092 --describe --topic <topic-name>
```
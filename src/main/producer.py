'''
Created on 2017年6月3日

@author: king
'''
# !/usr/bin/env python
import pika

if __name__ == '__main__':
    credentials = pika.PlainCredentials('bohe','wlswn')
    connection = pika.BlockingConnection(pika.ConnectionParameters(
    '192.168.99.100',32771,'/',credentials))
    channel = connection.channel()

    # 声明queue
    channel.queue_declare(queue='user')

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
    channel.basic_publish(exchange='',
                      routing_key='user',
                      body='Hello World!')
    print(" [x] Sent 'Hello World!'")
    fp = open("test.txt",'w') 
    fp.write("OOOOO");
    connection.close()
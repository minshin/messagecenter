'''
Created on 2017年6月2日

@author: king
'''


# _*_coding:utf-8_*_
__author__ = 'King'
import pika
import os


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
class process:
    def run(self):
        print("KKKKKK\n")
        credentials = pika.PlainCredentials('bohe','wlswn')
        connection = pika.BlockingConnection(pika.ConnectionParameters('message-middleware',5672,'/',credentials))
        channel = connection.channel()
        channel.queue_declare(queue='user')
        channel.basic_consume(callback,
                      queue='user',
                      no_ack=True)

        print(' [*] Waiting for messages. To exit press CTRL+C \n')
        
        channel.start_consuming()

# You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
# was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.


if __name__ == '__main__':
    instance = process()
    instance.run()
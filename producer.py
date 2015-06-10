#!/usr/bin/env python

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=str(sys.argv[1])))
channel = connection.channel()

channel.queue_declare(queue=str(sys.argv[2]), durable=True)

message = ' '.join(sys.argv[3:]) 
channel.basic_publish(exchange='',
                      routing_key=str(sys.argv[2]),
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
print " [x] Sent %r" % (message,)
connection.close()

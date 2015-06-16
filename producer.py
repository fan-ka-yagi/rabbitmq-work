#!/usr/bin/env python

import pika
import sys

host_name        = str(sys.argv[1])
exchange_name    = str(sys.argv[2])
queue_name       = str(sys.argv[3])
routing_key_name = str(sys.argv[4])

credentials = pika.PlainCredentials('user', 'password')
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host_name, 5672, '/', credentials))
channel = connection.channel()

channel.exchange_declare(exchange=exchange_name,
                         type='topic')

channel.queue_declare(queue=queue_name, durable=True)

message = ' '.join(sys.argv[5:]) 
channel.basic_publish(exchange=exchange_name,
                      routing_key=routing_key_name,
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
print " [x] Sent %r" % (message,)
connection.close()

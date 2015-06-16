#!/usr/bin/env python

import pika
import time
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

result = channel.queue_declare(queue=queue_name, durable=True)

channel.queue_bind(exchange=exchange_name,
                   queue=queue_name,
                   routing_key=routing_key_name)

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r:%r" % (method.routing_key, body,)
    time.sleep( body.count('.') )
    print " [x] Done"
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue=queue_name)

channel.start_consuming()

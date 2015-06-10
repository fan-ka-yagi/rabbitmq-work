#!/usr/bin/env python

import pika
import time
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=str(sys.argv[1])))
channel = connection.channel()

channel.queue_declare(queue=str(sys.argv[2]), durable=True)
print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    time.sleep( body.count('.') )
    print " [x] Done"
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue=str(sys.argv[2]))

channel.start_consuming()

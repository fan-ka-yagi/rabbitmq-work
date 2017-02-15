# rabbitmq-work

Install
===============
	$ sudo pip install pika

Usage
===============
	$ ./producer.py <host> <exchange> <queue> <routing_key> "string"
	$ ./consumer.py <host> <exchange> <queue> <routing_key>

Example
===============
	$ # send 
	$ for i in `seq 1 10`; do ./producer.py 10.0.0.123 test.exchange test.queue test.routing_key "msg ${i} ..."; done

	$ # receive
	$ ./consumer.py 10.0.0.123 test.exchange test.queue test.routing_key

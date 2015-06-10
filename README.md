# rabbitmq-work

Install
===============
	$ sudo pip install pika

Usage
===============
	$ ./producer.py <host> <queue> "string"
	$ ./consumer.py <host> <queue>

Example
===============
	$ # send 
	$ for i in `seq 1 10`; do ./producer.by 10.0.0.123 test_queue "msg ${i} ..."; done

	$ # receive
	$ ./consumer.py 10.0.0.123 test_queue

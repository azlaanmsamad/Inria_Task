import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_exchanger', exchange_type='direct')

result_1 = channel.queue_declare(queue='sensor_1', exclusive=True)
result_2 = channel.queue_declare(queue='sensor_2', exclusive=True)
result_3 = channel.queue_declare(queue='sensor_3', exclusive=True)

channel.confirm_delivery()

channel.queue_bind(queue='sensor_1', exchange='direct_exchanger', routing_key='1')
channel.queue_bind(queue='sensor_2', exchange='direct_exchanger', routing_key='2')
channel.queue_bind(queue='sensor_3', exchange='direct_exchanger', routing_key='3')

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received Message %r with Routing key %r" % (body, method.routing_key))


channel.basic_consume(queue=result_1.method.queue, on_message_callback=callback, auto_ack=False)
channel.basic_consume(queue=result_2.method.queue, on_message_callback=callback, auto_ack=False)
channel.basic_consume(queue=result_3.method.queue, on_message_callback=callback, auto_ack=False)

channel.start_consuming()

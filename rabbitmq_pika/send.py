import pika
import sys
import random

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_exchanger', exchange_type='direct')

if len(sys.argv) >= 2:
    arg1 = sys.argv[1]
else:
    arg1 = None

if len(sys.argv) >= 3:
    arg2 = sys.argv[2]
else:
    arg2 = None

if len(sys.argv) == 4:
    arg3 = sys.argv[3]
else:
    arg3 = None

if arg1:
    message_1 = random.randint(1, 5)

if arg2:
    message_2 = random.randint(1,9)

if arg3:
    message_3 = random.randint(1,10)

if arg1:
    channel.basic_publish(
        exchange='direct_exchanger', routing_key=str(arg1), body=str(message_1))
    print(" [x] Sent to sensor {} the message {}".format(arg1, message_1))

if arg2:
    channel.basic_publish(
        exchange='direct_exchanger', routing_key=str(arg2), body=str(message_2))
    print(" [x] Sent to sensor {} the message {}".format(arg2, message_2))

if arg3:
    channel.basic_publish(
        exchange='direct_exchanger', routing_key=str(arg3), body=str(message_3))
    print(" [x] Sent to sensor {} the message {}".format(arg3, message_3))

connection.close()
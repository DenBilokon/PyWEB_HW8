import pika
from mongoengine import connect, DoesNotExist
from models import Client


connect(host='mongodb+srv://userweb10:567234@pyweb.e9uvnnc.mongodb.net/?retryWrites=true&w=majority')


def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='sms_queue')

    def callback(ch, method, properties, body):
        try:
            message = body.decode()
            contact = Client.objects.get(id=message)
            print(f" [x] Отримано повідомлення {message}")
            contact.sent_message = True
            ch.basic_ack(delivery_tag=method.delivery_tag)
        except DoesNotExist:
            print(f'Не змогли відправити повідомлення')

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='sms_queue', on_message_callback=callback)
    print('Чекаємо голубів...')
    channel.start_consuming()


if __name__ == '__main__':
    main()
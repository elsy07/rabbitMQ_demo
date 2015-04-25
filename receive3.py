import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='mylog')
#channel.confirm_delivery()

def callback(ch, method, properties, body):
    import os
    import requests
    import time
    fname = os.path.basename(body)
    print body
    print fname
    try:
        r = requests.get(body)
    except:
        pass
    with open(fname, "wb") as f:
        f.write(r.content)
    #time.sleep(160)

channel.basic_consume(callback, queue='mylog', no_ack=True)
channel.start_consuming()


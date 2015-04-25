import web
import pika

urls = (
  '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        return render.hello_form1()

    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        greeting = "%s" % (form.greet)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='mylog')
        channel.basic_publish(exchange='', routing_key='mylog', body=greeting)

        return render.index(greeting = greeting)
if __name__ == "__main__":
    app.run()

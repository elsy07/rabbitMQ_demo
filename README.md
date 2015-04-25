# rabbitMQ_demo
A Demo of producer and consumer using python

Here is an example that uses RabbitMQ messaging system:

http://23.21.167.60:8080/hello

You simply have to provide the path of the file that you want to download from the web. It will download the file and save it in directory on the server.
It may look like a very simple application that can be easily built using any other software like php / mysql or Java. The advantage is that it is infinitely scalable. Even if there are thousands of people submitting files to be downloaded, it can be handle that load. If you have even more hits, rabbitMQ can be easily scaled out using clusters.

1) Start built in python simple server listening on port 8000
root@ip-10-120-6-221:/home/ubuntu/mydownload# python -m SimpleHTTPServer

This will display all the files in the current directory (mydownload in this case)
http://23.21.167.60:8000/

2) communicate with rabbitMQ and get the messages to be processed.

root@ip-10-120-6-221:/home/ubuntu/mydownload# python receive3.py

3) Start listening on port 8080 and work like web-server

root@ip-10-120-6-221:/var/www/html/new_email360_panel# python app2.py

visit this page:
http://23.21.167.60:8080/hello

app2.py file has all the code required to send messages to rabbitMQ server. files in template folder are using to show and process html form.

#!/bin/sh
while read id
do
curl --data "greet=$id" http://23.21.167.60:8080/hello
done << heredoc
http://ahvaz.ist.unomaha.edu/azad/temp/softarch/05-welling-php-mysql-web.pdf
http://cdn.oreillystatic.com/oreilly/booksamplers/9781449319267_sampler.pdf
http://www.fis.unipr.it/pub/doc/mysql/manuale_mysql.pdf

heredoc

#!/usr/bin/python

import smtplib
import string


HOST = "smtp.gmail.com"
SUBJECT = "Test email from Python"

TO = "1026799129@qq.com"
FROM = "chizhouqiang@163.com"

text = "Python rules them all"

BODY = string.join((
        " Feom: %s " % FROM,
        " To: %s" % TO,
        " Subject: %s" %SUBJECT,
        "",
         text
         ), "\r\n")

server = smtplib.SMTP()
server.connect(HOST)

server.login("chizhouqiang@163.com", "mumu6397")
server.sendmail(FROM, [TO], BODY)
server.quit()

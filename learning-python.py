#!/usr/bin/env python3
#coding: utf-8
import smtplib
from email.mime.text import MIMEText

sender = 'supengfei007@163.com'
receiver = 'supengfei007@gmail.com'
subject = 'python email test'
smtpserver = 'smtp.163.com'
username = 'supengfei007@163.com'
password = '********'

msg = MIMEText('<html><h1>Hello World</h1></html>','html','utf-8')

msg['Subject'] = subject

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()

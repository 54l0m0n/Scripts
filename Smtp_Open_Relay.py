#!/usr/bin/python

import smtplib

target = raw_input ("Insert your target IP/DNS: ")
sender = raw_input ("Insert your email: ")
receivers = raw_input ("Insert your target: ")
message = raw_input ("Insert your message: ")

try:
     smtpObj = smtplib.SMTP(target)
     smtpObj.sendmail(sender, receivers, message)
     print "Successfully sent email"
except SMTPException:
     print "Error to send email"

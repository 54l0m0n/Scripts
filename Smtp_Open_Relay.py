#!/usr/bin/python

import smtplib

target = raw_input ("Insert your target IP/DNS: ")
s = raw_input ("Insert your email: ")
r = raw_input ("Insert the target email: ")
message = raw_input ("Insert your message: ")

try:
     smtpObj = smtplib.SMTP(target)
     smtpObj.sendmail(s, r, message)
     print "Successfully sent email"
except SMTPException:
     print "Error to send email"

#!/usr/bin/python

import smtplib


print """
-------------. || .--------------. || .--------------. || .--------------. |
| |    _______   | || | ____    ____ | || |  _________   | || |   ______     | |
| |   /  ___  |  | || ||_   \  /   _|| || | |  _   _  |  | || |  |_   __ \   | |
| |  |  (__ \_|  | || |  |   \/   |  | || | |_/ | | \_|  | || |    | |__) |  | |
| |   '.___`-.   | || |  | |\  /| |  | || |     | |      | || |    |  ___/   | |
| |  |`\____) |  | || | _| |_\/_| |_ | || |    _| |_     | || |   _| |_      | |
| |  |_______.'  | || ||_____||_____|| || |   |_____|    | || |  |_____|     | |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------' """


t = raw_input ("Enter SMTP server: ")
p = raw_input ("Enter SMTP port: ")
e = raw_input ("Insert your email (To): ")
r = raw_input ("Insert your email target (From): ")
s = raw_input ("Subject: ")
m = raw_input ("Message: ")

try:
     smtpObj = smtplib.SMTP(t,p)
     smtpObj.sendmail(s,r,s,m)
     print "Successfully sent email"
except SMTPException:
     print "Error to send email"

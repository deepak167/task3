#!/usr/bin/env python
# coding: utf-8



import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host_address = "ramwadhwa67@gmail.com"
host_pass = "13061996"
guest_address = "ramwadhwa1031@gmail.com"
subject = "Regarding Failure of your webserver "
content = "Your webserver is not working. Kindly check it soon and start";
message = MIMEMultipart()
message['From'] = host_address
message['To'] = guest_address
message['Subject'] = subject
message.attach(MIMEText(content, 'plain'))
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(host_address, host_pass)
text = message.as_string()
session.sendmail(host_address, guest_address  , text)
session.quit()
print('Successfully sent your mail')

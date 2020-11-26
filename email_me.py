#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SpawnTerror 2020

import config
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_notification(body, subject):
  
    msg = MIMEMultipart()
    msg['To'] = config.mailToAddress
    msg['From'] = config.mailFromAddress
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'plain'))
    message = msg.as_string()

    server = smtplib.SMTP(config.mailFromServer)
    server.starttls()
    server.login(config.mailFromAddress, config.mailFromPassword)

    try:
        server.sendmail(config.mailFromAddress, config.mailToAddress, message)
    except:
        print("Something went wrong. Unable to send email.")
    server.quit()
    


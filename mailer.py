#!/usr/bin/env python3

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send(cred, subject, body):
    password = cred['password']
    sender = cred['sender']
    receiver = cred['receiver']
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = receiver
    html = MIMEText(body, "html")
    message.attach(html)
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465,
                              context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, message.as_string())
            server.quit()
    except Exception as e:
        pass

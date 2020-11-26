import config
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_notification(body, subject):
  
    msg = MIMEMultipart()
    msg['To'] = mailer.mailToAddress
    msg['From'] = mailer.mailFromAddress
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'plain'))
    message = msg.as_string()

    server = smtplib.SMTP(mailer.mailFromServer)
    server.starttls()
    server.login(mailer.mailFromAddress, mailer.mailFromPassword)

    try:
        server.sendmail(mailer.mailFromAddress, mailer.mailToAddress, message)
    except:
        print("Something went wrong. Unable to send email.")
    server.quit()
    


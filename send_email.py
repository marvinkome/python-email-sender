from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from parse_text import compose_message


def send_email(recipient_email,
               subject,
               message,
               from_email='marvinkome@gmail.com',
               server='smtp.gmail.com',
               port=587,
               password='ucauyydjzlmzqvwf'):
    # create message object instance
    msg = MIMEMultipart()

    # setup message params
    msg['from'] = from_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # attach message to body
    msg.attach(MIMEText(message))

    # create server
    server = smtplib.SMTP(host=server, port=port)
    # server.starttls()

    # login with credentials
    server.login(from_email, password)

    # send the message
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    # close server
    server.quit()

    print('successfully sent email to %s:' % msg['To'])


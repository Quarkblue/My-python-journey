import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()

server.login('d.s.c.r.3012@gmail.com', 'BEST301276')


msg = MIMEMultipart()
msg['From'] = 'divyansh'
msg['To'] = 'abcd@mallination.com'
msg['Subject'] = 'TEST'

msg.attach(MIMEText("HELLO", 'plain'))



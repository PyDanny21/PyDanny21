from email.message import EmailMessage
import ssl
import smtplib
#from app2 import password

email_sender='quansahd19@gmail.com'
password='password'

email_receiver='newmandanny992gmail.com'

subject='Dont forget to subscribe'
body='''
When you watch a video,please hit the subscribe button
'''
em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['subject']=subject
em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())

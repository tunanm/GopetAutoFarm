import os
import ssl
import smtplib
import datetime
from email.message import EmailMessage
from simplegmail
# Set up the SMTP server and login details

def screen_captcha_capture():
    return ''
def read_email_reply():
    return ''
def fill_in_captcha():
    return ''
def send_captcha_email():
    sender_email = 'gopetcaptchanotification@gmail.com'
    password = os.environ.get('EMAIL_PASSWORD')
    # Create the email headers and body
    receive_email = 'tuanquangtrungtuky5899@gmail.com'
    subject = f'Captcha {datetime.datetime.now()}'
    body = ''
    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = receive_email
    msg['Subject'] = subject
    context = ssl.create_default_context()
    with open('Resources/Captcha/captcha.jpg','rb') as f:
        file_data = f.read()
        file_type = 'jpg'
        file_name = f.name
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(sender_email,password)
        smtp.sendmail(sender_email,receive_email,msg.as_string())

send_captcha_email()

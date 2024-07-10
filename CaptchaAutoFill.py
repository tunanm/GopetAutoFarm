import os
import ssl
import smtplib
import datetime
import re
import pyautogui as gui
from email.message import EmailMessage
from simplegmail import Gmail
from simplegmail.query import construct_query
# Set up the SMTP server and login details
captcha = ''
captcha_file_path = 'Resources\Captcha\captcha.jpg'

def screen_captcha_capture():
    screen_shot = gui.screenshot(region=(0, 0, 850, 520))
    screen_shot.save(captcha_file_path)
def read_email_reply():
    global captcha
    gmail = Gmail()
    query_params = {
        'newer_than':(1,"day")
    }
    messages = gmail.get_unread_inbox(query=construct_query(query_params))
    if "Captcha" in messages[0].subject:
        match = re.findall(r"\D(\d{5})\D", " "+messages[0].plain+" ")
        if match:
            captcha = match
    return captcha[0]

def fill_in_captcha(numbers):
    ind = 0
    while ind <= 5:
        gui.click()
        ind += 1
    for number in numbers:
        if number == '0':
            gui.click()
        if number == '1':
            gui.click()
        if number == '2':
            gui.click()
        if number == '3':
            gui.click()
        if number == '4':
            gui.click()
        if number == '5':
            gui.click()
        if number == '6':
            gui.click()
        if number == '7':
            gui.click()
        if number == '8':
            gui.click()
        if number == '9':
            gui.click()
def send_captcha_email():
    sender_email = 'gopetcaptchanotification@gmail.com'
    password = os.environ.get('EMAIL_PASSWORD')
    # Create the email headers and body
    receive_email = 'saometvay5899@gmail.com'
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

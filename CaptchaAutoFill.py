import os
import ssl
import smtplib
import datetime
from datetime import datetime as date
import re
import time
import random

import pyautogui as gui
from email.message import EmailMessage
from simplegmail import Gmail
from Variable import captcha_file_path
from simplegmail.query import construct_query
# Set up the SMTP server and login details

numbers_position = [(206,401),(249,401),(291,401),(338,403),(382,403),
                    (425,403),(470,401),(511,401),(556,401),(600,400)]
delete_position = [(642,401),(648,405),(638,397)]
capture_area = (277, 174, 300, 200)
date_send = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")


def screen_captcha_capture():
    screen_shot = gui.screenshot(region=capture_area)
    screen_shot.save(captcha_file_path)
def read_email_reply():
    gmail = Gmail()
    query_params = {
        'newer_than':(1,"day")
    }
    messages = gmail.get_unread_inbox(query=construct_query(query_params))
    date_receive = date.strptime(messages[0].date, "%Y-%m-%d %H:%M:%S%z").strftime("%Y-%m-%d %H:%M")
    if date_receive > date_send:
        if "Captcha" in messages[0].subject:
            match = re.findall(r"\D(\d{5})\D", " "+messages[0].plain+" ")
            if match:
                captcha = match
                return captcha[0]
    return ''

def fill_in_captcha(numbers):
    ind = 0
    while ind <= 5:
        gui.click(delete_position[random.randint(0,2)])
        time.sleep(0.5)
        ind += 1
    for number in numbers:
        if number == '0':
            gui.click(numbers_position[0])
            time.sleep(0.3)
        if number == '1':
            gui.click(numbers_position[1])
            time.sleep(0.3)
        if number == '2':
            gui.click(numbers_position[2])
            time.sleep(0.3)
        if number == '3':
            gui.click(numbers_position[3])
            time.sleep(0.3)
        if number == '4':
            gui.click(numbers_position[4])
            time.sleep(0.3)
        if number == '5':
            gui.click(numbers_position[5])
            time.sleep(0.3)
        if number == '6':
            gui.click(numbers_position[6])
            time.sleep(0.3)
        if number == '7':
            gui.click(numbers_position[7])
            time.sleep(0.3)
        if number == '8':
            gui.click(numbers_position[8])
            time.sleep(0.3)
        if number == '9':
            gui.click(numbers_position[9])
            time.sleep(0.3)
def send_captcha_email():
    global date_send
    sender_email = 'gopetcaptchanotification@gmail.com'
    password = os.environ.get('EMAIL_PASSWORD')
    # Create the email headers and body
    receive_email = 'saometvay5899@gmail.com'
    date_send = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    subject = f'Captcha {date_send}'
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

def captcha_solve():
    screen_captcha_capture()
    time.sleep(1)
    send_captcha_email()
    time.sleep(120)
    captcha_string = read_email_reply()
    fill_in_captcha(captcha_string)



import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import cv2

# Set up the SMTP server and login details
def send_captcha_email():
    smtp_port = 587
    sender_email = 'gopetcaptchanotification@gmail.com'
    server = smtplib.SMTP(sender_email, smtp_port)
    password = 'violetevergarden99@'
    # Create the email headers and body
    recipient_email = 'tuanquangtrungtuky5899@gmail.com'
    message = 'Fill the captcha'
    # Connect to the server and send the email
    try:
        server.ehlo()
        server.starttls()
        server.login(sender_email,password)
        server.sendmail(sender_email,recipient_email,message)
        print('Email sent successfully!')
    except smtplib.SMTPException as e:
        print(f'Failed to send email: {e}')
    finally:
        server.quit()
    cv2.waitKey()

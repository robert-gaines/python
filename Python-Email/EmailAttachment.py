
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from getpass import getpass
from email import encoders
import smtplib
import email
import ssl
import sys
import os

def main():
    #
    print("[*] E-Mail Attachment Transmission Script ")
    #
    sender = input("[+] Enter the sender's e-mail address-> ")
    #
    recipient = input("[+] Enter the recipient's e-mail address-> ")
    #
    subject = input("[+] Enter the subject of the message-> ")
    #
    password = getpass("[+] Enter the sender's account password-> ")
    #
    body = "This is an e-mail message with an attachment! "
    #
    message = MIMEMultipart()
    #
    message['From']    = sender
    #
    message['To']      = recipient
    #
    message['Subject'] = subject
    #
    message.attach(MIMEText(body,"plain"))
    #
    attachment = input("[+] Enter the path to the attachment-> ")
    #
    if(os.path.exists(attachment)):
        #
        print('[*] File exists ')
        #
    else:
        #
        print("[!] File could not be located, departing ")
        #
        sys.exit(1)
        #
    with open(attachment,"rb") as attached_file:
        #
        part = MIMEBase("application","octet-stream")
        #
        part.set_payload(attached_file.read())
        #
    encoders.encode_base64(part)
    #
    part.add_header(
        "Content-Disposition",
        f"attachment; filename={attachment}",
        )
    #
    message.attach(part)
    #
    text = message.as_string()
    #
    context = ssl.create_default_context()
    #
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
        #
        server.login(sender,password)
        #
        server.sendmail(sender,recipient,text)

if(__name__ == '__main__'):
    #
    main()

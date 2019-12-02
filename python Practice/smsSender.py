import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = 'shahrozimtiaz07@gmail.com'
password = input("Enter password for Shahroz\n")
sms_gateway = '5714205607@txt.att.net'

sms_gateway_prompt = input("Enter SMS gateway or leave blank for default\n")
if(sms_gateway_prompt != ""):
    sms_gateway = sms_gateway_prompt
    if('@' not in sms_gateway):
        sms_gateway += '@txt.att.net'

subject = input("Enter subject or leave blank for no subject\n")

# Create a multipart message and set headers
message = MIMEMultipart()
if(subject!=""):
    message["Subject"] = subject

text = 'I just slithered into your texts using python'
text_prompt = input('Enter text for SMS or leave blank for default\n')
if(text_prompt!=""):
    text=text_prompt

body = MIMEText(text, "plain")

message.attach(body)
# message["Bcc"] = receiver_email  # Recommended for mass emails

context = ssl.create_default_context()
server = smtplib.SMTP_SSL('smtp.gmail.com', 465,context=context)

#Next, log in to the server
username = sender_email.split("@")[0]
server.login(username, password)

#Send the text
# msg = "Python sample message\n Hello!" # The /n separates the message from the headers
x = input("How many times would you like to send the message?\n")
for i in range(int(x)):
    print("sending:",i+1)
    server.sendmail(sender_email, sms_gateway, message.as_string())
server.close()
print("sent")

# AT & T: [number] @ txt.att.net
# Sprint: [number] @ messaging.sprintpcs.com or [number] @ pm.sprint.com
# T - Mobile: [number] @ tmomail.net
# Verizon: [number] @ vtext.com
# Boost
# Mobile: [number] @ myboostmobile.com
# Cricket: [number] @ sms.mycricket.com
# Metro
# PCS: [number] @ mymetropcs.com
# Tracfone: [number] @ mmst5.tracfone.com
# U.S.Cellular: [number] @ email.uscc.net
# Virgin
# Mobile: [number] @ vmobl.com

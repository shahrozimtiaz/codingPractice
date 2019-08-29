import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class emailSender:
    # sender_email = ''
    # password = ''
    # receiver_email = ''
    # subject = ''
    # text = ''
    # message = None

    def __init__(self,sender_email,password):
        self.sender_email = sender_email
        self.password = password
        self.context = ssl.create_default_context()
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=self.context)
        self.username = sender_email.split("@")[0]
        self.server.login(self.username, self.password)

    def sendMessage(self,receiver_email,subject,text):
        self.receiver_email = receiver_email
        self.subject = subject
        self.text = text
        self.message = MIMEMultipart()
        self.message["From"] = self.sender_email
        self.message["To"] = self.receiver_email
        self.message["Subject"] = self.subject
        body = MIMEText(text, "plain")
        self.message.attach(body)
        self.server.sendmail(self.sender_email, self.receiver_email, self.message.as_string())

    def close(self):
        self.server.close()
        print("Good bye")

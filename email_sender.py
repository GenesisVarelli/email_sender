# Setup Gmail 2 factor authentication
from email.message import EmailMessage

# Generate app password
from app2 import password
import ssl
import smtplib

# Create a function to send the mail
email_sender = 'genesisvarelli@gmail.com'
email_password = password

email_receiver = 'rexaci9301@kernuo.com'

subject = "Hello Genesis"
body = """Keep going! you will make it"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

# Used the smtp library to log in and send email
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
      smtp.login(email_sender, email_password)
      smtp.sendmail(email_sender, email_receiver, em.as_string())

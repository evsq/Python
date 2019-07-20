import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Enter SMTP server credentials
host = "smtp.gmail.com"
port = 587
# Enter your credentials
login = "your@email.com"
password = "yourpassword"
#Enter sender's and recipient's email addresses
from_email = login
destination_list = "dest@email.com"

# Create SMTP variable
smtp_server = smtplib.SMTP(host, port)
# Establish connection
smtp_server.ehlo()
# Start TLS connection
smtp_server.starttls()
# Log in on an SMTP server
smtp_server.login(login, password)
# Create message container
msg = MIMEMultipart('alternative')
msg['Subject'] = "Test"
msg['From'] = from_email
msg['To'] = destination_list
# Create the body of the message
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="https://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""
# Record the MIME type
html = MIMEText(html, 'html')
# Attach part into message container
msg.attach(html)
# Send message
smtp_server.sendmail(from_email, destination_list, msg.as_string())
# Terminate the SMTP session and close the connection
smtp_server.quit()




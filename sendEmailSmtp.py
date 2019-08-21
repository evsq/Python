import smtplib

# Enter SMTP server credentials
host = "smtp.gmail.com"
port = 587
# Enter your credentials
login = "your@email.com"
password = "yourpassword"
#Enter sender's and recipient's email addresses
from_email = login
destination_list = ["dest@email.com", "dest2@email.com"]

# Create SMTP variable
smtp_server = smtplib.SMTP(host, port)
# Establish connection
smtp_server.ehlo()
# Start TLS connection
smtp_server.starttls()
# Log in on an SMTP server
smtp_server.login(login, password)
# Send message
smtp_server.sendmail(from_email, destination_list, "just type any message")
# Terminate the SMTP session and close the connection
smtp_server.quit()

import smtplib

host = "smtp.gmail.com"
port = 587
login = "your@email.com"
password = "yourpassword"
from_email = login
destination_list = ["dest@email.com", "dest2@email.com"]

smtp_server = smtplib.SMTP(host, port)
smtp_server.ehlo()
smtp_server.starttls()
smtp_server.login(login, password)
smtp_server.sendmail(from_email, destination_list, "just type any message")
smtp_server.quit()

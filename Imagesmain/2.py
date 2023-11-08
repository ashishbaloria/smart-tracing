import csv
import smtplib
from email.message import EmailMessage
EMAIL_ADDRESS = "asbb1925@gmail.com"
EMAIL_PASSWORD = "syreqipoxnngszin"
recipients=['asbb1925@gmail.com','ashish19011a0543@gmail.com','yousuf89786@gmail.com']
msg = EmailMessage()
msg['Subject'] = 'Danger'
msg['From'] = EMAIL_ADDRESS
msg['To'] = recipients
msg.set_content('Person detected from the list')
files = r'C:\Users\ASHISH BALORIA\PycharmProjects\facerecognition'
for file in files:
    with open('NPerson.csv', 'rb') as s:
        file_data = s.read()
        file_name = s.name
msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
text = msg.as_string()
server.send_message(msg)
def check_name_in_csv(filename, name):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if name in row:
                return True
    return False
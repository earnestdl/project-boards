import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def notify(recipients): 

    body = 'Your email content here'
    msg = MIMEMultipart()

    msg['Subject'] = 'Email Subject'
    msg['From'] = 'your.email@gmail.com'
    msg['To'] = (', ').join(recipients.split(','))

    msg.attach(MIMEText(body,'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your.email@gmail.com', 'yourpassword')
    server.send_message(msg)
    server.quit()

if __name__ == '__main__':
    
    notify('email_1@domain.com,email_2@domain.com',body)
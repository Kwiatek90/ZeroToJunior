#dzien 90


import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email import encoders

#Tworzenie wiadomości e-mail

msg = MIMEMultipart()
msg['From'] = 'kwiatkowsky24@gmail.com'
msg['To'] = 'kwiatkowsky24@gmail.com'
msg['Subject'] = 'Testowa wiadomośc'

#Dodanie treści do maila

tekst = 'Czesc! Oto przykładowa wiadomość!'
msg.attach(MIMEText(tekst, 'plain'))

#Wczytanie obrazka i dodanie jako załącznik

with open(r'D:\Programowanie\ZeroToJunior\100dni\90\dokument.pdf', 'rb') as file:
    pdf = MIMEApplication(file.read(), _subtype='pdf')
    pdf.add_header('Content-Disposition', 'attachment', filename='dokument.pdf')
    msg.attach(pdf)
    
# Konfiguracja serwera SMTP i wysłanie wiadomości

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('kwiatkowsky24@gmail.com', 'barcelona95')
server.send_message(msg)
server.quit()


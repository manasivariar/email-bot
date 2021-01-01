import smtplib

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login('manasirvariar13121999@gmail.com','gfduqhtxinpmymxi')
    
    subject= 'how are you?'
    body= 'I hope you are fine.'

    msg= f'Subject: {subject}\n\n{body}'

    smtp.sendmail('manasirvariar13121999@gmail.com', 'manasirvariar007@gmail.com', msg)
    print('EMAIL SENT!')

    smtp.quit()

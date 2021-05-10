import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)

#conn.ehlo()
print(conn.ehlo())

#conn.starttls()
print(conn.starttls())

#conn.login('username', 'password')

#conn.sendmail('394839fdf@gmail.com', '23409fdfs@gmail.com', 'Subject: Hello \n\nDear User, delete this email.\n\n Regards')
#sendmail returns an dictonairy containing any failed emails, if its blank everything is good

#conn.quit()
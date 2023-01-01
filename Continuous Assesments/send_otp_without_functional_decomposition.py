#CA Program no:1
#Sending and generating OTP as a program without Functional decomposition

#generate OTP
#random module

import random
import math
import smtplib

'''data ="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

leng=len(data)
otp= ""
for i in range(6):
    otp +=data[math.floor(random.random()*leng)]

print("your otp is",otp)'''

#Send OTP in email
#create SMTP session
server=smtplib.SMTP('smtp.gmail.com',587)
# start TLS for security
server.starttls()
#Authentication
password="agiv rekq tzmu czvf"
server.login("akankshasvirkar@gmail.com",password)
#generate otp
data ="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

leng=len(data)
otp= ""
for i in range(6):
    otp +=data[math.floor(random.random()*leng)]

print("your otp is",otp)

#sending email
msg=("Hello, your OTP is "+str(otp))
server.sendmail("akankshasvirkar@gmail.com","akankshasvirkar26@dbatu.ac.in",msg)
server.quit()







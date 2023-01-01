# CA program no: 3
# Implementation OTP assignment as per OOP design described in classroom

import random
import re
import smtplib
import time


# creation of class otpservice
class otpservice:

    def __init__(self, email, size):
        self.email = email
        self.size = size
        self.check_email()
        otp_id = self.generate_otp()
        self.send_otp(otp_id)
        self.validate_otp(otp_id)

    # method for validation of Email
    def check_email(self):

        p = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if (re.search(p, self.email)):  # regular expression is used here
            print("Email id is valid!")

        else:
            print(self.email + "- is not valid email id.\nPlease Enter valid Email Id!!")

    # Method for Generation of OTP

    def generate_otp(self):
        otp = ''
        for i in range(self.size):
            value = random.randint(0, 9)
            otp = otp + str(value)
        return otp

    # Method for Sending OTP
    def send_otp(self, otp):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        password = "agiv rekq tzmu czvf"
        sender_mail = "akankshasvirkar@gmail.com"
        self.otp = otp
        msg = 'Hello, Your OTP is ' + str(self.otp)
        server.login(sender_mail, password)
        server.sendmail('akankshasvirkar@gmail.com', self.email, msg)
        print("OTP send !!")
        server.quit()

    # Method for validating OTP
    def validate_otp(self, otp):
        test_time = 30
        begnining_time = time.time()
        current_time = time.time()
        self.otp = otp
        original_otp = self.otp
        input_otp = 0

        if input_otp == original_otp:
            pass
        else:
            while input_otp != original_otp and int(current_time) - int(begnining_time) <= test_time:
                if current_time - begnining_time <= test_time:
                    input_otp = input("Enter Valid OTP :")
                current_time = time.time()
        if input_otp == original_otp:
            print("\nOTP is Valid!!")
        else:
            print("\nOut Of Time! OTP is valid for 30 seconds.")


email = input("Enter Email:")
otp_size = random.randint(4, 8)
a = otpservice(email, otp_size)  # creation of object

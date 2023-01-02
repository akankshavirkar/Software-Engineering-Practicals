#CA PRogram no:4
#Test cases for OTP assignment

#This file contains methods fir sending and geenration of otp
import random
import re
import smtplib
import time


#method for validation of Email
def check(email):
    p= "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    if(re.search(p,email)):
        print("Email Is vaild")
    else:
        raise AssertionError(email + "- is not valid email id.\nPlease Enter valid Email Id!!")

#Method for Generation of OTP

def generate_otp(size):
    otp=""
    for i in range(size):
        value = random.randint(0,9)
        otp= otp + str(value)
    return otp

#method for checking length of otp
def otp_length(otp):
    if not (4 <= len(otp) <=8):
        raise AssertionError("Length of OTP should be in betweern 4 and 8 ")
    else:
        print("Length of otp is valid!")

#Method for sending OTP
def send_otp(receiver_mail,otp):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    password = "agiv rekq tzmu czvf"
    sender_mail ="akankshasvirkar@gmail.com"
    msg = "Hello,Your OTP is" +str(otp)
    server.login(sender_mail,password)
    server.sendmail("akankshasvirkar@gmail.com",receiver_mail,msg)
    print("OTP send !!")
    server.quit()

    # Method for validating OTP
    def validate_otp(otp):
        test_time = 30
        begnining_time = time.time()
        current_time = time.time()
        original_otp = otp
        input_otp = 0
        if input_otp == original_otp:
            pass
        else:
            while input_otp != original_otp and int(current_time) - int(begnining_time) <= test_time:
                if current_time - begnining_time <= test_time:
                    input_otp = input("Enter Valid OTP :")
                current_time = time.time()
        if input_otp == original_otp:
            print("OTP is Valid!!")
        else:
            raise AssertionError("Out Of Time! OTP is valid for 30 seconds.")
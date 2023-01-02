# CA PRogram no:4
# Test cases for OTP assignment
# This file contains Test Cases for OTP

import unittest
import OTP


class TestOtp(unittest.TestCase):

    # Testcase for correct inputs
    def test_case1(Self):
        print("--------TestCase 1--------")
        email = 'akankshasvirkar@gmail.com'
        OTP.check_email(email)
        otp = OTP.generate_otp(4)
        OTP.otp_length(otp)
        OTP.send_otp(email, otp)
        OTP.validate_otp(otp)

    # TestCase for Invalid Email
    def test_case2(Self):
        print("\n--------TestCase 2--------")
        email = 'akankshasvirkar@gmail.com'
        OTP.check_email(email)
        otp = OTP.generate_otp(4)
        OTP.otp_length(otp)
        OTP.send_otp(email, otp)
        OTP.validate_otp(otp)

    # Testcase for invalid otp length
    def test_case3(Self):
        print("\n--------TestCase 3--------")
        email = 'akankshasvirkar@gmail.com'
        OTP.check_email(email)
        otp = OTP.generate_otp(3)
        OTP.otp_length(otp)
        OTP.send_otp(email, otp)
        OTP.validate_otp(otp)

    # Testcase for validating otp
    def test_case4(Self):
        print("\n--------TestCase 4--------")
        email = 'akankshasvirkar@gmail.com'
        OTP.check_email(email)
        otp = OTP.generate_otp(5)
        OTP.otp_length(otp)
        OTP.send_otp(email, otp)
        OTP.validate_otp(otp)


if __name__ == '__main__':
    unittest.main()
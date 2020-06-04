# OTP class for getting OTP's from a secret

import pyotp
import datetime

class OTP:

    def __init__(self):
        print('foo')

    def get_otp(self, secret, timestamp=datetime.datetime.now()):
        totp = pyotp.TOTP(secret)
        return totp.at(timestamp)
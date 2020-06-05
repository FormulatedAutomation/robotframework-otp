"""Library for generating OTP's from a secret

Generates TOTP's based on a base32 secret
"""

import pyotp
import datetime

class OTP:

    def get_otp(self, secret, timestamp=datetime.datetime.utcnow()):
        """Takes 1 argument and an optional timestamp argument.

        Example:
        | base32secret |
        | base32secret | timestamp |
        """
        totp = pyotp.TOTP(secret)
        return totp.at(timestamp)
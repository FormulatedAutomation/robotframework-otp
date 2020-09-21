import pyotp
import datetime

class OTP:
    """Library for generating OTP's from a secret

    Generates TOTP's based on a base32 secret
    """


    def get_otp(self, secret, timestamp=False):
        """Takes 1 argument and an optional timestamp argument.

        Example:
        | base32secret |
        | base32secret | timestamp |
        """
        if not timestamp:
            timestamp = datetime.datetime.utcnow()
        totp = pyotp.TOTP(secret)
        return totp.at(timestamp)
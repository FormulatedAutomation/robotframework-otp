*** Settings ***
Library  OTP
Library  DateTime

*** Test Cases ***
Get OTP from secret
    ${otp}=    Get OTP    base32secret
    Should Match Regexp	${otp}	\\d{6}

Get OTP from secret with time
    ${timestamp}=    Convert Date	2014-06-11 10:07:42.000
    ${otp}=    Get OTP    base32secret    ${timestamp}
    Should Match Regexp	${otp}	\\d{6}
    Should Be Equal As Strings    ${otp}    285912

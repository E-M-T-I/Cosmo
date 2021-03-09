import random
import os
from twilio.rest import Client

otp=random.randint(100000,999999)
print(otp)

# Account Sid and Auth Token from twilio.com/console
account_sid = 'ACcfded5c814de352eb71e16be381d4a63'
auth_token = '58d3fd901d209de5225dec7604caa338'
client = Client(account_sid, auth_token)

#  send sms 
verification = client.verify \
                .services('VA982640a09885ed166809555d8648cde2') \
                .verifications \
                .create(to='+919815615582', channel='sms')

print(verification.status)


import random
import os
from twilio.rest import Client

otp=random.randint(100000,999999)
print("RANDOM NUMBER IS: ",otp)

# Account Sid and Auth Token from twilio.com/console
account_sid = 'AC18b2edb36345f2428d27bd66c4e1883e'
auth_token = '0dba6c56719bc06d2dcfafc6599cc4ad'
client = Client(account_sid, auth_token)

#  send sms 
verification = client.verify \
                .services('VA6c19b31a510b4856fc8496fec2c82e63') \
                .verifications \
                .create(to='', channel='sms')

print(verification.status)
  
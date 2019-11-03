from twilio.rest import Client

def send_sms(phone_no, text):
	phone_no = "+4" + phone_no
	account_sid = ''
	auth_token = ''
	client = Client(account_sid, auth_token)
	message = client.messages.create(
         body=text,
         from_='+12565784399',
         to=phone_no
     )
from twilio.rest import Client

def send_sms(phone_no, text):
	phone_no = "+4" + phone_no
	account_sid = 'AC6c348e70e56ae2d415d49d612abadc48'
	auth_token = '22d42ae040ff410efbff660fd074e1a7'
	client = Client(account_sid, auth_token)
	message = client.messages.create(
         body=text,
         from_='+12565784399',
         to=phone_no
     )
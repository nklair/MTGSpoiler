from twilio.rest import Client
import os
import re


class TextAlert:
	def __init__(self):
		pass

	def send(self, recipient, cards, website):
		message = ''
		if len(cards) == 1:
			message = 'A new card has been spoiled!\n'
		else:
			message = 'New cards have been spoiled!\n'

		message += self.generateMessage(cards, website)

		account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
		auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
		from_number = os.environ.get('TWILIO_FROM_NUMBER')

		client = Client(account_sid, auth_token)

		client.messages.create(
			to=self.formatNumber(recipient),
			from_=from_number,
			body=message
		)

	def generateMessage(self, cards, website):
		message = ''
		for cardName in cards:
			message += cardName + '\n'

		message += website
		return message

	def formatNumber(self, number):
		number = re.sub('[^1234567890]', '', number)
		if not len(number) == 11:
			print('Error: invalid number provided.')

		return '+' + number
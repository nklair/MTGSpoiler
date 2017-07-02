import smtplib
import os
from email.mime.text import MIMEText


class EmailAlert:
	def __init__(self):
		pass

	def send(self, recipient, cards, website):
		subject = ''
		if len(cards) == 1:
			subject = 'A new card has been spoiled!\n'
		else:
			subject = 'New cards have been spoiled!\n'

		message = self.generateMessage(cards, website)

		msg = MIMEText(message)

		# This is the best I could come up with for keeping my info private
		fromEmail = os.environ.get('FROMEMAIL')
		smtpServer = os.environ.get('SMTPSERVER')
		smtpPort = os.environ.get('SMTPPORT')
		emailUsername = os.environ.get('EMAILUSERNAME')
		emailPassword = os.environ.get('EMAILPASSWORD')

		if not fromEmail or not smtpServer or not smtpPort or not emailUsername or not emailPassword:
			print('Environment variables not properly set.')
			return



		msg['Subject'] = subject
		msg['From'] = fromEmail
		msg['To'] = recipient


		mail = smtplib.SMTP(smtpServer, smtpPort)
		mail.login(emailUsername, emailPassword)
		mail.sendmail(fromEmail, [recipient], msg.as_string())
		mail.quit()

	def generateMessage(self, card, website):
		message = ''
		for cardName in cards:
			message += cardName + '\n'

		message += website
		return message
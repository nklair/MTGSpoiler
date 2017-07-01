from BSCrawlerMTGS import BSCrawlerMTGS
from EmailAlert import EmailAlert
from twilio.rest import Client


class MTGSpoiler():
	def __init__(self):
		self.crawler = BSCrawlerMTGS()
		self.alert = EmailAlert()

	def checkForCards(self, website):
		return self.crawler.getCards(website)

	def sendNewCardAlert(self, recipients, cards):
		for recipient in recipients:
			self.alert.send(recipient, cards, website)

	def checkAndSend(self, website, recipients):
		sendNewCardAlert(recipients, checkForCards(website), website)

email = EmailAlert()
email.send('nklair@nd.edu', ['Test Card Name', 'Another test card'], 'www.google.com')
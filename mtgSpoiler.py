from CrawlerFactory import CrawlerFactory
from AlertFactory import AlertFactory

class MTGSpoiler():
	def __init__(self, crawlMethod='BSMTGS', alerts=['email']):
		self.crawler = CrawlerFactory().create(crawlMethod)
		self.alerts = AlertFactory().create(alerts)

	def checkForCards(self, website, minutes=5):
		if self.crawler is None:
			return []
		return self.crawler.getCards(website, minutes)

	def sendNewCardAlert(self, recipients, cards, website):
		if len(cards) == 0:
			return
		for recipient in recipients:
			for alert in self.alerts:
				alert.send(recipient, cards, website)

	def checkAndSend(self, website, recipients, minutes=5):
		self.sendNewCardAlert(recipients, self.checkForCards(website, minutes), website)


from bs4 import BeautifulSoup
import requests
import time


# A crawler using Beautiful Soup that parses the MTG Salvation spoiler website
class BSCrawlerMTGS:

	def __init__(self):
		pass

	def getCards(self, website, minutes):
		newCards = []
		page = self.getSiteHTML(website)

		soup = BeautifulSoup(page.content, 'lxml')

		foundCards = soup.find_all("div", { "class" : "spoiler-update"})
		for card in foundCards:
			if self.isNew(card, minutes):
				newCards.append(str(card.contents[2].text))

		return newCards


	def isNew(self, cardTagInfo, minutes):
		minutes = int(minutes)
		currTime = int(time.time())
		for data in str(cardTagInfo.contents[0]).split(' '):
			if 'data-epoch' in data:
				cardTime = int(data.split('=')[1].split('"')[1])
				if currTime - cardTime <= minutes * 60:
					return True
				else:
					return False


	def getSiteHTML(self, website):
		return requests.get(website)
from BSCrawlerMTGS import BSCrawlerMTGS

class CrawlerFactory:
	def create(self, method):
		if method is 'BSMTGS':
			return BSCrawlerMTGS()
		return None
from EmailAlert import EmailAlert
from TextAlert import TextAlert

class AlertFactory:
	def create(self, alerts):
		alertTypes = []
		for alert in alerts:
			if alert is 'email':
				alertTypes.append(EmailAlert())
			elif alert is 'text':
				alertTypes.append(TextAlert())
		return alertTypes
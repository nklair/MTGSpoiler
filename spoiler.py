import sys
from mtgSpoiler import MTGSpoiler
from EmailAlert import EmailAlert

def usage():
	print('Usage: python3 spoiler.py')
	print('flags:')
	print('-t, --text <phone_number>')
	print('-e, --email <email_address>')
	print('-m <minutes>')
	print('-c <crawler>')
	print('-w <website_url>')
	sys.exit(1)

args = sys.argv
length = len(args)

if len(args) is 1:
	usage()
alerts = []
crawler = 'BSMTGS'
recipients = []
minutes = None
web = ''
for index, arg in enumerate(args):
	if arg == '-t' or arg == '--text':
		if index + 1 >= length:
			usage()
		recipients.append(args[index + 1])
		if 'text' not in alerts:
			alerts.append('text')
	elif arg == '-e' or arg == '--email':
		if index + 1 >= length:
			usage()
		recipients.append(args[index + 1])
		if 'email' not in alerts:
			alerts.append('email')
	elif arg == '-m':
		if index + 1 >= length:
			usage()
		minutes = int(args[index + 1])
	elif arg == '-c':
		if index + 1 >= length:
			usage()
		crawler = args[index + 1]
	elif arg == '-w':
		if index + 1 >= length:
			usage()
		web = args[index + 1]
if minutes is not None:
	spoil = MTGSpoiler(crawler, alerts)
	spoil.checkAndSend(web, recipients, minutes)
else:
	spoil = MTGSpoiler(crawler, alerts)
	spoil.checkAndSend(web, recipients)

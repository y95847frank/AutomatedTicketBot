from ticketBot import websiteSignIn, buyTickets, terminateBot, scheduleBot, AutoTicketsBot, configRead

#TODO: yml setup

config = configRead('config.yml')
ticketsBot = AutoTicketsBot(config)

scheduleBot(ticketsBot, config['Config']['startTime'])

try:
	websiteSignIn(ticketsBot, retryCounter=3)
	buyTickets(ticketsBot)
	notifyUser('AutoTicketsBot Notification', 'Got tickets!!!!!')
	terminateBot(ticketsBot, waitTime=600)

except RuntimeError as e:
	terminateBot(ticketsBot, waitTime=0)
	print(e)
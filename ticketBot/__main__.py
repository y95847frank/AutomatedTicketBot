from ticketBot import websiteSignIn, buyTickets, terminateBot, AutoTicketsBot, configRead

#TODO: yml setup

config = configRead('config.yml')
ticketsBot = AutoTicketsBot(config)

try:
	websiteSignIn(ticketsBot, retryCounter=3)
	buyTickets(ticketsBot)
	notifyUser('AutoTicketsBot Notification', 'Got tickets!!!!!')
	terminateBot(ticketsBot, waitTime=600)

except RuntimeError as e:
	terminateBot(ticketsBot, waitTime=0)
	print(e)
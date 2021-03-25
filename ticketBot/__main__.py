from ticketBot import websiteSignIn, buyTickets, terminateBot, AutoTicketsBot, configRead

#TODO: yml setup

config = configRead('config.yml')
ticketsBot = AutoTicketsBot(config['username'], config['password'], config['homePage'], config['ticketPage'], config['executable_path']
                        , config['ticketCount'])

try:
	websiteSignIn(ticketsBot)
	buyTickets(ticketsBot)

except RuntimeError as e:
	terminateBot(ticketsBot)
	print(e)

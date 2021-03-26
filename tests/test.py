import AutoTicketsBot as tBot

configDestination = 'var/config.yml'

args = tBot.addArgs()
config = tBot.configRead(configDestination)
if tBot.configWrite(configDestination, args, config) is True:
	print("Successfully store new config to {}".format(configDestination))

ticketsBot = tBot.AutoTicketsBot(config)

#scheduleBot(ticketsBot, config['Config']['startTime'])

try:
	tBot.websiteSignIn(ticketsBot, retryCounter=3)
	tBot.buyTickets(ticketsBot)
	tBot.notifyUser('AutoTicketsBot Notification', 'Got tickets!!!!!')
	tBot.terminateBot(ticketsBot, waitTime=900)

except RuntimeError as e:
	tBot.terminateBot(ticketsBot, waitTime=0)
	print(e)
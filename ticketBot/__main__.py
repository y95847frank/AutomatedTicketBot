from ticketBot import websiteSignIn, buyTickets, terminateBot, scheduleBot, AutoTicketsBot, configRead, notifyUser, addArgs, configWrite

#TODO: yml, splinter setup

configDestination = 'var/config.yml'

args = addArgs()
config = configRead(configDestination)
if configWrite(configDestination, args, config) is True:
	print("Successfully store new config to {}".format(configDestination))

ticketsBot = AutoTicketsBot(config)

#scheduleBot(ticketsBot, config['Config']['startTime'])

try:
	websiteSignIn(ticketsBot, retryCounter=3)
	buyTickets(ticketsBot)
	notifyUser('AutoTicketsBot Notification', 'Got tickets!!!!!')
	terminateBot(ticketsBot, waitTime=600)

except RuntimeError as e:
	terminateBot(ticketsBot, waitTime=0)
	print(e)
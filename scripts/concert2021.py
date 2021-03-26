import AutoTicketsBot as tBot

configDestination = 'config.yml'

args = tBot.addArgs()
config = tBot.configRead(configDestination)
if tBot.configWrite(configDestination, args, config) is True:
	print("Successfully store new config to {}".format(configDestination))

ticketsBot = tBot.AutoTicketsBot(config)

scheduleBot(ticketsBot, config['Config']['startTime'])

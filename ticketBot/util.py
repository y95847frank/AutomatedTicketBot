import sys
import os
import yaml
import schedule
import time
import datetime

def configRead(fileName):
    with open(os.path.join(os.path.dirname(__file__), fileName)) as c:
        config = yaml.safe_load(c)
    return config

def notifyUser(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

def terminateBot(ticketsBot, waitTime=0):
	time.sleep(waitTime)
	ticketsBot.quit()

def websiteSignIn(ticketsBot, retryCounter=5):
    ticketsBot.initBrowser()
    ticketsBot.visitHomePage()
    iteration = 0
    while iteration < retryCounter:
        try:
            ticketsBot.signInHomePage()
            ticketsBot.signInChecker(wait_time=3)
            break
        except RuntimeError as e:
            print(e)
            iteration += 1
            print('Retrying {} time...'.format(iteration))
    if iteration >= retryCounter:
    	raise RuntimeError("Failed to sign in to the website. Please verify your account information and restart the program.")

def buyTickets(ticketsBot):
    ticketsBot.enterTicketPage()
    ticketsBot.selectTicket()

def buyTicketsPipeline(ticketsBot):
    buyTickets(ticketsBot)
    notifyUser('AutoTicketsBot Notification', 'Got tickets!!!!!')
    terminateBot(ticketsBot, waitTime=600)

def scheduleBot(ticketsBot, startTime):
    twoMinDelta = datetime.datetime.strptime(startTime, "%H:%M") - datetime.timedelta(minutes=2)
    schedule.every().day.at(twoMinDelta.strftime("%H:%M")).do(websiteSignIn, ticketsBot, 3)
    schedule.every().day.at(startTime).do(buyTicketsPipeline, ticketsBot)

    while True:
        schedule.run_pending()
        time.sleep(1)
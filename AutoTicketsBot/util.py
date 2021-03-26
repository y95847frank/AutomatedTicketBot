import sys
import os
import yaml
import schedule
import time
import datetime
import argparse

def addArgs():
    parser = argparse.ArgumentParser(description='Set config yaml.')
    parser.add_argument("-a", "--username", help="set the account name")
    parser.add_argument("-p", "--password", help="set the password")
    parser.add_argument("-u", "--homePage", help="set the home page url")
    parser.add_argument("-t", "--ticketPage", help="set the ticket page url")
    parser.add_argument("-e", "--executable_path", help="set path of the web driver")
    parser.add_argument("-c", "--ticketCount", help="set number of tickets")
    parser.add_argument("-s", "--startTime", help="set time for buying tickets")
    args = parser.parse_args()
    return args

def configRead(fileName):
    with open(os.path.join(os.getcwd(), fileName)) as file:
        config = yaml.safe_load(file)
    return config

def configWrite(fileName, args, config):
    writeFlag = False

    for arg in vars(args):
        if getattr(args, arg) is not None:
            config['Config'][arg] = getattr(args, arg)
            writeFlag = True

    if writeFlag is True:
        with open(os.path.join(os.getcwd(), fileName), 'w') as file:
            yaml.dump(config, file)
        return True
    else:
        return False

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
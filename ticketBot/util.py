import sys
import os
import yaml
import schedule

def configRead(fileName):
    with open(os.path.join(os.path.dirname(__file__), fileName)) as c:
        config = yaml.safe_load(c)['Config']
    return config

def notifyUser(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

def terminateBot(ticketsBot):
	ticketsBot.quit()

def websiteSignIn(ticketsBot):
    ticketsBot.initBrowser()
    ticketsBot.visitHomePage()
    iteration = 0
    while iteration < 5:
        try:
            ticketsBot.signInHomePage()
            ticketsBot.signInChecker(wait_time=3)
            break
        except RuntimeError as e:
            print(e)
            iteration += 1
            print('Retrying {} time...'.format(iteration))
    if iteration >= 5:
    	raise RuntimeError("Failed to sign in to the website. Please verify your account information and restart the program.")

def buyTickets(ticketsBot):
    ticketsBot.enterTicketPage()
    ticketsBot.selectTicket()
    sleep(600)
    ticketsBot.quit()

def schedultBot():
    schedule.every().day.at("19:58").do(websiteSignIn, ticketsBot)
    schedule.every().day.at("20:00").do(buyTicket, ticketsBot)

    while True:
        schedule.run_pending()
        sleep(1)
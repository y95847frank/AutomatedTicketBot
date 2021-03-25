import os
import sys
from time import sleep
from datetime import datetime
import schedule
import yaml

#TODO: yml setup
#TODO: config reader function

with open('config.yml') as c:
    config = yaml.load(c)['Config']

buy_Tickets = Buy_Tickets(config['username'], config['password'], config['homePage'], config['ticketPage'], config['executable_path']
                        , config['ticketCount'])


schedule.every().day.at("19:58").do(job, buy_Tickets)
schedule.every().day.at("20:00").do(buying, buy_Tickets)

while True:
    schedule.run_pending()
    sleep(1)
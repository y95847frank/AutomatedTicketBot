import os
import sys
from splinter.browser import Browser
from time import sleep
from datetime import datetime
import schedule

username = 'Frank'
lastName = 'Yen'

birth = '08/05/1996'

number = "frank0804"

email = 'y95847@gmail.com'
zipCode = '78731'
phone = "7737663971"

date = '5/1/2021'

buy_Tickets = Buy_Tickets(username, lastName, birth, number, email, zipCode, phone, date, sys.argv[1])
schedule.every().day.at("19:58").do(job, buy_Tickets)
schedule.every().day.at("20:00").do(buying, buy_Tickets)

while True:
    schedule.run_pending()
    sleep(1)

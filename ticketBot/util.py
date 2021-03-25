def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

def job(buy_Tickets):
    buy_Tickets.home_Page()

def buying(buy_Tickets):
    buy_Tickets.enter_Page()
    buy_Tickets.choose_Ticket()
    sleep(600)
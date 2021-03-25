from splinter.browser import Browser

class Buy_Tickets(object):
    def __init__(self, username, lastName, birth, number, email, zipCode, phone, date, login_url):
        self.username = username
        self.lastName = lastName
        self.birth = birth
        self.number = number
        self.email = email
        self.zipCode = zipCode
        self.phone = phone
        self.date = date

        self.home_page = 'https://kktix.com/'
        #self.login_url = 'https://i-chen.kktix.cc/events/fyu2wd-dsfd2'
        self.login_url = login_url
        self.driver_name = 'chrome'
        self.executable_path = '/Users/tyyen/Downloads/chromedriver'

        self.driver = Browser(driver_name=self.driver_name, executable_path=self.executable_path)
        self.driver.driver.set_window_size(1000, 700)

    def home_Page(self):
        self.driver.visit(self.home_page)
        button = self.driver.find_by_text('Sign In').first.click()
        self.driver.find_by_id('user_login').fill(self.email)
        self.driver.find_by_id('user_password').fill(self.number)
        button = self.driver.find_by_name('commit').first.click()
        sleep(10)
        

    def enter_Page(self):
        self.driver.visit(self.login_url)
        #button = self.driver.find_by_text('Next Step').first.click()

    def choose_Ticket(self):
        #self.driver.check('person_agree_terms')
        count = 0
        while count < 10:
            try:
                button = self.driver.find_by_css('button[class="btn-default plus"]').last.click()
                button = self.driver.find_by_css('button[class="btn-default plus"]').last.click()
                break
            except:
                count += 1
        
        count = 0
        while count < 10:
            try:
                self.driver.find_by_id('person_agree_terms').check()
                button = self.driver.find_by_name('captcha_answer').fill('T2')
                button = self.driver.find_by_text('Next Step').first.click()
                break
            except Exception as e:
                count += 1
                print(e)

    def new_appointment(self):
        count = 0
        while count < 5:
            try:
                button = self.driver.find_by_text('New Appointment').first.click()
                break
            except:
                count += 1
                sleep(1)
                print("Keep trying")

        #button = self.driver.find_by_text('OK').first.click()
        button = self.driver.find_by_text('Service not listed or my license is not eligible').first.click()
        button = self.driver.find_by_text('No').first.click()

    def fill_detial(self):
        #print(self.driver.find_by_text('Email').first.value)
        self.driver.find_by_id('input-134').fill(self.phone)

        self.driver.find_by_id('input-140').fill(self.email)
        self.driver.find_by_id('input-143').fill(self.email)
        self.driver.find_by_id('input-166').fill(self.zipCode)
        button = self.driver.find_by_text(' Next ').first.click()

    def checkDate(self):
        while True:
            try:
                find_h = self.driver.find_by_tag('td')
                
                if len(find_h) == 0:
                    continue

                for i in find_h:
                    outHTML = i["outerHTML"]
                    if "Next Available Date" in outHTML:
                        print(outHTML.split()[-2])
                        if datetime.strptime(self.date, "%m/%d/%Y") > datetime.strptime(outHTML.split()[-2], "%m/%d/%Y"):
                            notify("DPS Appointment", "Found a new appointment time slot!")
                            print("Got it!!!!!!!!!")
                            sleep(10)

                break
            except Exception as e:
                sleep(1)
                print(e)


    def quit(self):
        self.driver.quit()
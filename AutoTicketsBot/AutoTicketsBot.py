from splinter.browser import Browser

class AutoTicketsBot(object):
    def __init__(self, config):
        self.userConfig = config['Config']
        self.browserConfig = config['Browser']
        self.username = self.userConfig['username']
        self.password = self.userConfig['password']
        self.homeUrl = self.userConfig['homeUrl']
        self.ticketPage = self.userConfig['ticketPage']
        self.driver_name = 'chrome'
        self.executablePath = self.userConfig['executablePath']
        self.ticketCount = self.userConfig['ticketCount']

    def initBrowser(self):
        self.driver = Browser(driver_name=self.driver_name, executable_path=self.executablePath)
        self.driver.driver.set_window_size(self.browserConfig['width'], self.browserConfig['height'])

    def visitHomePage(self):
        self.driver.visit(self.homeUrl)
        if self.driver.is_element_present_by_text('English', wait_time=5) is True:
            self.driver.find_by_text('English').first.click()
        else:
            raise RuntimeError("Failed to switch language to English in home page...") 

    def signInHomePage(self):
        if self.driver.is_element_present_by_text('Sign In', wait_time=5) is True:
            self.driver.find_by_text('Sign In').first.click()
        else:
            raise RuntimeError("Failed to find SignIn button in home page...")

        if self.driver.is_element_present_by_id('user_login', wait_time=2) is True:
            self.driver.find_by_id('user_login').fill(self.username)
        else:
            raise RuntimeError("Failed to fill account in signIn page...")
        
        if self.driver.is_element_present_by_id('user_password', wait_time=2) is True:
            self.driver.find_by_id('user_password').fill(self.password)
        else:
            raise RuntimeError("Failed to fill password in signIn page...")
        
        if self.driver.is_element_present_by_name('commit', wait_time=2) is True:
            self.driver.find_by_name('commit').first.click()
        else:
            raise RuntimeError("Failed to find SignIn button in signIn page...")

    def signInChecker(self, wait_time=3):
        if self.driver.is_element_not_present_by_text(self.username, wait_time=wait_time) is True:
            raise RuntimeError("Failed to sign in to the website...")
        
    def enterTicketPage(self):
        #TODO: Keep refreshing
        self.driver.visit(self.ticketPage)
        while self.driver.is_element_not_present_by_css('button[class="btn-default plus"]', wait_time=5) is True:
            self.driver.visit(self.ticketPage)

    def selectTicket(self):
        for __ in range(self.ticketCount):
            self.driver.find_by_css('button[class="btn-default plus"]')[-2].click()

        if self.driver.is_element_present_by_id('person_agree_terms', wait_time=2) is True:
            self.driver.find_by_id('person_agree_terms').check()
        else:
            raise RuntimeError("Failed to find agree_term checkbox in ticket page...")
        
        #self.captchaSolver("T2")

        if self.driver.is_element_present_by_text('Next Step', wait_time=2) is True:
            self.driver.find_by_text('Next Step').first.click()
        else:
            raise RuntimeError("Failed to find Next_Step button in ticket page...")

    def captchaSolver(self, answer):
        if self.driver.is_element_present_by_name('captcha_answer', wait_time=2) is True:
            self.driver.find_by_name('captcha_answer').fill('answer')
        else:
            raise RuntimeError("Failed to find Captcha in ticket page...")

    def quit(self):
        self.driver.quit()
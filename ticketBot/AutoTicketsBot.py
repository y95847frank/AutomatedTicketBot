from splinter.browser import Browser

class AutoTicketsBot(object):
    def __init__(self, username, password, homePage, ticketPage, executable_path, ticketCount):
        self.username = username
        self.password = password
        self.homePage = homePage
        #self.homePage = 'https://kktix.com/'
        self.ticketPage = ticketPage
        self.driver_name = 'chrome'
        self.executable_path = executable_path
        #self.executable_path = '/Users/tyyen/Downloads/chromedriver'
        self.ticketCount = ticketCount

    def initBrowser(self):
        self.driver = Browser(driver_name=self.driver_name, executable_path=self.executable_path)
        #TODO: put width and length into config
        self.driver.driver.set_window_size(1000, 700)

    def visitHomePage(self):
        self.driver.visit(self.homePage)
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
        if self.driver.is_element_present_by_text('Sign In', wait_time=wait_time) is True:
            raise RuntimeError("Failed to sign in to the website...")
        
    def enterTicketPage(self):
        #TODO: Keep refreshing
        self.driver.visit(self.ticketPage)
        while self.driver.is_element_not_present_by_css('button[class="btn-default plus"]', wait_time=5) is True:
            self.driver.visit(self.ticketPage)

    def selectTicket(self):
        for __ in range(self.ticketCount):
            self.driver.find_by_css('button[class="btn-default plus"]').last.click()

        if self.driver.is_element_present_by_id('person_agree_terms', wait_time=2) is True:
            self.driver.find_by_id('person_agree_terms').check()
        else:
            raise RuntimeError("Failed to find agree_term checkbox in ticket page...")
        
        if self.driver.is_element_present_by_text('Next Step', wait_time=2) is True:
            self.driver.find_by_text('Next Step').first.click()
        else:
            raise RuntimeError("Failed to find Next_Step button in ticket page...")
        #button = self.driver.find_by_name('captcha_answer').fill('T2')

    def quit(self):
        self.driver.quit()
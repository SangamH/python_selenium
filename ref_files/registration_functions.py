from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
class Registration():
    driver = None
    username = None
    password = None
    email = None
    first_name = None
    last_name = None
    url = None
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def load_signup_page(self):

        self.driver.get(self.url)
        if "Sign " in self.driver.title:
            return True
        else:
            return False


    def user_signup(self):
        htmusername = self.driver.find_element_by_xpath("//input[@id='usernameghg']")
        htmusername.clear()
        htmusername.send_keys(self.username)
        htmpassword = self.driver.find_element_by_xpath("//input[@name='password']")
        htmpassword.clear()
        htmpassword.send_keys(self.password)
        htmemail = self.driver.find_element_by_name("email")
        htmemail.clear()
        htmemail.send_keys(self.email)
        htmfirst_name = self.driver.find_element_by_xpath("//input[@name='first_name']")
        htmfirst_name.clear()
        htmfirst_name.send_keys(self.first_name)
        htmlast_name = self.driver.find_element_by_xpath("//input[@name='last_name']")
        htmlast_name.clear()
        htmlast_name.send_keys(self.last_name)
        self.driver.find_element_by_id("submitform").click()
        return True

    def load_signin_page(self):
        self.driver.get("https://www.monkeytest1.com/user/sign-in/")
        if "Log in" in self.driver.title:
            return True
        else:
            return False

    def check_user_login(self):
        self.driver.find_element_by_xpath("//button[contains(text(),'LOG')]").click()
        return True

    def test_action_chains_hover_over_menu(self):

        self.driver.get(self.url)
        menu_element = self.driver.find_element_by_xpath("//a[contains(text(),'About')]")
        sub_menu_element = self.driver.find_element_by_xpath("//ul/li/a[contains(text(),'product')]")
        action1 = ActionChains(self.driver)
        action1.move_to_element(menu_element).click(sub_menu_element)
        action1.perform()
        return True

    def test_action_chains_clickhref(self):
        self.driver.get(self.url)
        a_link_element = self.driver.find_element_by_xpath("//a[contains(text(),'Return')]")
        action2 = ActionChains(self.driver)
        action2.click(a_link_element)
        action2.perform()
        return True
import time
from xpath import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from setlog import setLogger
logger = setLogger(log_file_title)
class Monkey():
    driver = None
    username = None
    password = None
    email = None
    first_name = None
    last_name = None
    url = None
    msg = None
    servery_title = None
    browser = globle_browser

    def __init__(self):
        if "chrome" == self.browser.strip().lower():
            self.driver = webdriver.Chrome()
            logger.info('Executing with Chrome browser.')

        elif "firefox" == self.browser.strip().lower():
            self.driver = webdriver.Firefox()
            logger.info('Executing with Firefox browser.')

        else:
            logger.error('Browser: %s not supported, Supported browsers are Firefox and Chrome' % self.browser)
            exit(-1)
        # selenium configuration
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        logger.info("Browser initialized")


    def load_signup_page(self):
        self.driver.get(self.url)
        if "Sign " in self.driver.title:
            logger.error('Loaded: %s ' % self.url)
            return True
        else:
            logger.error('Failed to Load: %s ' % self.url)
            return False

    def user_signup(self):
        try:
            htmusername = self.driver.find_element_by_xpath(xpath_list['signup_page_xpath_user_name'])
            htmusername.clear()
            htmusername.send_keys(self.username)
            logger.error('Entered data for user name: %s ' % self.username)
            htmpassword = self.driver.find_element_by_xpath(xpath_list['signup_page_xpath_password'])
            htmpassword.clear()
            htmpassword.send_keys(self.password)
            logger.error('Entered data for password: %s ' % self.password)
            htmemail = self.driver.find_element_by_name("email")
            htmemail.clear()
            htmemail.send_keys(self.email)
            logger.error('Entered data for email: %s ' % self.email)
            htmfirst_name = self.driver.find_element_by_xpath(xpath_list['signup_page_xpath_fname'])
            htmfirst_name.clear()
            htmfirst_name.send_keys(self.first_name)
            logger.error('Entered data for first name: %s ' % self.first_name)
            htmlast_name = self.driver.find_element_by_xpath(xpath_list['signup_page_xpath_lname'])
            htmlast_name.clear()
            htmlast_name.send_keys(self.last_name)
            logger.error('Entered data for last name: %s ' % self.last_name)
        except:
            logger.error('Submitted Invalid data  : %s ' % self.url)
            return False

        self.driver.find_element_by_id("submitform").click()
        self.url = "https://www.monkeytest2.com/dashboard/"
        self.driver.get(self.url)
        if "Welcome" in self.driver.title:
            logger.error('Loaded Url: %s ' % self.url)
            return True
        else:
            logger.error('Unable to load Url: %s ' % self.url)
            return False


    def load_signin_page(self):
        try:
            self.driver.get(self.url)
            logger.info('Loading Sign in page' + str(self.url))
        except:
            logger.info('Failed to load ' + str(self.url))

        if "Log in" in self.driver.title:
            try:
                htmusername = self.driver.find_element_by_xpath(xpath_list['login_page_xpath_user_name'])
                htmusername.clear()
                htmusername.send_keys(self.username)
                htmpassword = self.driver.find_element_by_xpath(xpath_list['login_page_xpath_password'])
                htmpassword.clear()
                htmpassword.send_keys(self.password)
                logger.info('Entered data for login - Username: %s' % self.username)
                logger.info('Entered data for login - Password: %s ' % self.password)
            except:
                return False
            self.driver.find_element_by_xpath(xpath_list['login_page_xpath_login_btn']).click()
            self.url = "https://www.monkeytest2.com/user/sign-in/"
            self.driver.get(self.url)
            if "Welcome" in self.driver.title:
                logger.info('Logged in with : %s  id' % self.username)
                return True
            else:
                logger.error('Failed to login with : %s  id' % self.username)
                return False
            return True
        else:
            logger.error('Failed to load : %s  Url' % self.url)
            return False

    def load_survery_page(self):
       self.driver.get(self.url)
       if "Log in" in self.driver.title:
                try:
                    self.driver.find_element_by_xpath(xpath_list['login_page_xpath_user_name']).send_keys(self.username)
                    self.driver.find_element_by_xpath(xpath_list['login_page_xpath_password']).send_keys(self.password)
                    self.driver.find_element_by_xpath(xpath_list['login_page_xpath_login_btn']).click()
                    self.url = "https://www.monkeytest2.com/home/?ut_source=header/"
                    self.driver.get(self.url)
                    if "Welcome" in self.driver.title:
                        self.driver.find_element_by_xpath(xpath_list['create_survey_btn']).click()
                        self.driver.find_element_by_xpath(xpath_list['create_survey_from_scratch_btn']).click()
                        self.servery_title = "Servey 28 2018"
                        self.driver.find_element_by_xpath(xpath_list['create_survey_title_field']).send_keys(self.servery_title)
                        self.driver.find_element_by_xpath(xpath_list['create_survey_submit_btn']).click()
                        self.url = "https://www.monkeytest2.com/home/?ut_source=header/"
                        self.driver.get(self.url)
                        self.driver.find_element_by_xpath(xpath_list['my_survery_list_btn']).click()
                        self.driver.find_elements_by_xpath("//td/p/a[contains(text(),'"+str(self.servery_title)+"')]")[0].click()
                        self.driver.find_element_by_xpath(xpath_list['survey_design_btn']).click()
                        time.sleep(5)
                        self.driver.find_element_by_xpath(xpath_list['title_field_for_survey_question']).send_keys("Multiple Qeustion")
                        time.sleep(5)
                        list_elements = self.driver.find_elements_by_xpath(xpath_list['multiple_question_type_for_survey_question'])
                        #print(len(list_elements))
                        i = 1
                        for ele in list_elements:
                            #ele.send_keys(Keys.TAB)
                            val = "Ans " + str(i)
                            ele.send_keys(val)
                            i = i+1
                        try:
                            self.driver.find_element_by_xpath(xpath_list['survey_question_save_btn']).click()
                            return True
                        except Exception,e:
                            # print("Except ---------------------"+str(e))
                            # time.sleep(20)
                            return False
                except:
                   return False
       else:
           return False

    def demo_function(self):
        logger.error('Executed From : %s ')
        return True

    def create_drag_drop_servey(self):
        self.driver.get(self.url)
        self.url = "https://www.monkeytest2.com/user/sign-in/"
        self.driver.find_element_by_xpath(xpath_list['login_page_xpath_user_name']).send_keys(self.username)
        self.driver.find_element_by_xpath(xpath_list['login_page_xpath_password']).send_keys(self.password)
        self.driver.find_element_by_xpath(xpath_list['login_page_xpath_login_btn']).click()
        self.url = "https://www.monkeytest2.com/home/?ut_source=header/"
        self.driver.get(self.url)
        if "Welcome" in self.driver.title:
            logger.info("Logged in successful")
            self.driver.find_element_by_xpath(xpath_list['create_survey_btn']).click()
            self.driver.find_element_by_xpath(xpath_list['create_survey_from_scratch_btn']).click()
            self.servery_title = "Servey 30 2018 1"
            self.driver.find_element_by_xpath(xpath_list['create_survey_title_field']).send_keys(self.servery_title)
            self.driver.find_element_by_xpath(xpath_list['create_survey_submit_btn']).click()
            # wait = WebDriverWait(self.driver, 10)
            # element = wait.until()
            #self.driver.implicitly_wait(10)
            time.sleep(7)
            if self.servery_title in self.driver.title:
                self.driver.find_element_by_xpath(xpath_list['changeQType']).click()
                self.driver.find_element_by_xpath(xpath_list['dropdown_question_type']).click()
                time.sleep(10)
            else:
                return False
            return True
        else:
            logger.error("Login Failed")
            return False
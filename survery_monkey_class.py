import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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

    def __init__(self):
        self.driver = webdriver.Chrome()

    def load_signup_page(self):
        self.driver.get(self.url)
        if "Sign " in self.driver.title:
            return True
        else:
            return False

    def user_signup(self):
        try:
            htmusername = self.driver.find_element_by_xpath("//input[@id='username']")
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
        except:
            return False

        self.driver.find_element_by_id("submitform").click()
        self.url = "https://www.monkeytest2.com/dashboard/"
        self.driver.get(self.url)
        if "Welcome" in self.driver.title:
            return True
        else:
            return False


    def load_signin_page(self):
        self.driver.get(self.url)
        if "Log in" in self.driver.title:
            try:
                htmusername = self.driver.find_element_by_xpath("//input[@id='username']")
                htmusername.clear()
                htmusername.send_keys(self.username)
                htmpassword = self.driver.find_element_by_xpath("//input[@id='password']")
                htmpassword.clear()
                htmpassword.send_keys(self.password)
            except:
                return False
            self.driver.find_element_by_xpath("//button[contains(text(),'LOG')]").click()
            self.url = "https://www.monkeytest2.com/user/sign-in/"
            self.driver.get(self.url)
            if "Welcome" in self.driver.title:
                return True
            else:
                return False
        else:
            return False

    def load_survery_page(self):
       self.driver.get(self.url)
       if "Log in" in self.driver.title:
                try:
                    self.driver.find_element_by_xpath("//input[@id='username']").send_keys(self.username)
                    self.driver.find_element_by_xpath("//input[@id='password']").send_keys(self.password)
                    self.driver.find_element_by_xpath("//button[contains(text(),'LOG')]").click()
                    self.url = "https://www.monkeytest2.com/home/?ut_source=header/"
                    self.driver.get(self.url)
                    if "Welcome" in self.driver.title:
                        self.driver.find_element_by_xpath("//div[@id='hd']/div/div/a[2]").click()
                        self.driver.find_element_by_xpath("//button[@id='scratch']").click()
                        self.servery_title = "Servey 5 2018"
                        self.driver.find_element_by_xpath("//div/input[@id='surveyTitle']").send_keys(self.servery_title)
                        self.driver.find_element_by_xpath("//button[@class='wds-button'][contains(text(),'CREATE')]").click()
                        self.url = "https://www.monkeytest2.com/home/?ut_source=header/"
                        self.driver.get(self.url)
                        self.driver.find_element_by_xpath("//li/a[contains(text(), 'My Surveys')]").click()
                        self.driver.find_elements_by_xpath("//td/p/a[contains(text(),'"+str(self.servery_title)+"')]")[0].click()
                        self.driver.find_element_by_xpath("//ul/li/a[contains(text(), 'DESIGN')]").click()
                        time.sleep(5)
                        self.driver.find_element_by_xpath("//div[@id='editTitle'][@data-id='editTitle']").send_keys("Multiple Qeustion")
                        time.sleep(5)
                        list_elements = self.driver.find_elements_by_xpath("//div[contains(@id,'newChoice')]")
                        #print(len(list_elements))
                        i = 1
                        for ele in list_elements:
                            #ele.send_keys(Keys.TAB)
                            val = "Ans " + str(i)
                            ele.send_keys(val)
                            i = i+1

                        # try:
                            #self.driver.find_element_by_xpath("//form[@name='surveyForm']//div/div/a[contains(text(),'SAVE')][class=(contains(text(),'wds-button wds-button--sm save'))]").click()
                        # except Exception,e:

                            # print("Except ---------------------"+str(e))
                            #time.sleep(20)
                            return True
                except:
                   return False
       else:
           return False
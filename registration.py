from survery_monkey_class import Monkey
from random import randint

def registration():
    obj = Monkey()
    obj.password = "Test@123"
    #obj.username = "TestAccountUSers"+ str(randint(1, 1000))
    obj.username = "testbyqateam"
    obj.email = obj.username+"@gmail.com"
    obj.first_name = "Test"
    obj.last_name = "User"
    obj.url = "https://www.monkeytest2.com/user/sign-up"
    if obj.load_signup_page():
        if obj.user_signup():
            return True
        else:
            return False
    else:
        return False
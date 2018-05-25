from survery_monkey_class import Monkey
from random import randint

def signin():
    obj = Monkey()
    obj.password = "Test@123"
    obj.email = "testmeuser@gmail.com"
    #obj.username = "testmeuser"
    obj.username = "testbyqateam"
    obj.url = "https://www.monkeytest2.com/user/sign-in/"
    if obj.load_signin_page():
        return True
    else:
        return False

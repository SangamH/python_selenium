from survery_monkey_class import Monkey
from random import randint


def create_survery():
    obj = Monkey()
    obj.password = "Test@123"
    obj.email = "testmeuser@gmail.com"
    obj.username = "testbyqateam"
    obj.url = "https://www.monkeytest2.com/dashboard/"
    if obj.load_survery_page():
        return True
    else:
        return False

def create_drag_drop_servey():
    obj = Monkey()
    obj.password = "Test@123"
    obj.email = "testmeuser@gmail.com"
    obj.username = "testbyqateam"
    obj.url = "https://www.monkeytest2.com/dashboard/"
    if obj.create_drag_drop_servey():
        return True
    else:
        return False
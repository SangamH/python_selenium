from registration_functions import Registration

def test_verify_user_name():

    obj = Registration()
    obj.password = "123456"
    obj.username = "TestAccountUSer"
    obj.email = "testmeforauto@me.com"
    obj.first_name = "Test"
    obj.last_name = "User"
   # obj.url = "https://csswizardry.com/demos/css-dropdown/"
    #assert obj.load_signup_page(), "Failed to load page"
    #assert obj.user_signup(), "Failed to Register"
    #assert obj.load_signin_page(), "Failed to load sign in page"
    #assert obj.check_user_login(), "Failed to sign in "
    #assert obj.test_action_chains_hover_over_menu() , ""

def test_signup():
    obj = Registration()
    obj.password = "123456"
    obj.username = "TestAccountUSer"
    obj.email = "testmeforauto@me.com"
    obj.first_name = "Test"
    obj.last_name = "User"
    obj.url = "https://www.monkeytest1.com/user/sign-up"
    assert obj.load_signup_page(), "Failed to load page"
    assert obj.user_signup(), "Failed to Register"

def test_action_chains_hover_over_menu():
    obj = Registration()
    obj.url = "https://csswizardry.com/demos/css-dropdown/"
    assert obj.test_action_chains_hover_over_menu(), "Failed to load submenu"

def test_action_chains_hreflink():
    obj = Registration()
    obj.url = "https://csswizardry.com/demos/css-dropdown/"
    assert obj.test_action_chains_clickhref(), "Link not provided"
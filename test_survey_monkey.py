from registration import registration
from sign_in import signin
from create_survery import create_survery

def test_call():
	#assert registration(), "Error in Registration"
	#assert signin(), "Error in Sign In"
	assert create_survery(), "Error in create survey"

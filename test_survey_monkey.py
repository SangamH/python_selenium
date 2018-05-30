from registration import registration
from sign_in import signin
from create_survery import create_survery
from demo_function import demo_function
import pytest
import sys

#use to run specific marker name {signin_marker} Ex: pytest -v -m signin_marker
@pytest.mark.signin_marker
def test_signin():
	ex = signin()
	assert ex, "Error in Sign In"

#skip is used to exclude the test case while testing
@pytest.mark.skip(reason="no way of currently testing this")
def test_resistration():
	assert registration(), "Error in Registration"

@pytest.mark.skip(reason="no way of currently testing this")
def test_create_servey():
	assert signin(), "Error in Sign In"
	assert create_survery(), "Error in create survey"

#skipif is used to exclude the test case on some condition
@pytest.mark.skipif(sys.version_info < (3,6),reason="requires python3.6")
def test_skipif_example():
	assert demo_function(), "requires python3.6"

@pytest.fixture()
def my_fixture():
    return 2

def test_my_fixture(my_fixture):
    print "I'm the test" + str(my_fixture)

# def test_my_fixture1(my_fixture):
# 	print("@ 2")

############ - k
# pytest -v -k "not sign" test_survey_monkey.py // exclude the test functions which have "sign" content in function name
# pytest -v -k "sign" test_survey_monkey.py // execute the test functions which have "sign" content in function name

"""

@pytest.mark.env(name): mark test to run only on named environment

@pytest.mark.skip(reason=None): skip the given test function with an optional reason. Example: skip(reason="no way of currently testing this") skips the test.

@pytest.mark.skipif(condition): skip the given test function if eval(condition) results in a True value.  Evaluation happens within the module global context. Example: skipif('sys.platform == "win32"') skips the test if we are on the win32 platform. see http://pytest.org/latest/skipping.html

@pytest.mark.xfail(condition, reason=None, run=True, raises=None, strict=False): mark the test function as an expected failure if eval(condition) has a True value. Optionally specify a reason for better reporting and run=False if you don't even want to execute the test function. If only specific exception(s) are expected, you can list them in raises, and if the test fails in other ways, it will be reported as a true failure. See http://pytest.org/latest/skipping.html

@pytest.mark.parametrize(argnames, argvalues): call a test function multiple times passing in different arguments in turn. argvalues generally needs to be a list of values if argnames specifies only one name or a list of tuples of values if argnames specifies multiple names. Example: @parametrize('arg1', [1,2]) would lead to two calls of the decorated test function, one with arg1=1 and another with arg1=2.see http://pytest.org/latest/parametrize.html for more info and examples.

@pytest.mark.usefixtures(fixturename1, fixturename2, ...): mark tests as needing all of the specified fixtures. see http://pytest.org/latest/fixture.html#usefixtures

@pytest.mark.tryfirst: mark a hook implementation function such that the plugin machinery will try to call it first/as early as possible.

@pytest.mark.trylast: mark a hook implementation function such that the plugin machinery will try to call it last/as late as possible.

"""
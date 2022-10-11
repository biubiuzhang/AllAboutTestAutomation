# Pytest Needs to Know

## Frameworks available in Python for unit testing
 - Robot
 - PyTest
 - Unittest
 - DocTest
 - Nose2
 - Testify
## PyTest Interview Questions
### What is PyTest?
Pytest is a Python testing tool. It allows you to write test cases in Python and run them against your code to check for bugs.
## Why do you think PyTest has become so popular in recent years?
I think pytest has become popular in recent years because it is a very powerful and easy to use testing tool. It has a lot of features that make it very versatile and it is also very easy to install and use.
### Is it possible to run a single test case using the pytest runner?
Yes, it is possible to run a single test case using the pytest runner. To do so, simply specify the name of the test case that you wish to run after the pytest runner command.
### How can we use the "assert" keyword in Python?
THe assert keyword in Python can be used in a number of ways to verify that something is true. For example, you could assert that a certain value is equal to another value, or that a certain condition is true. You can also use assert to check that an exception is raised, or that a certain warning is issued. Assert can be used in a number of different ways, so it really depends on what you are trying to verify.
### What are teh main advantages of using fixtures over setup and teardown methods in unit testing?
Fixtures offer a number of advantages over setup and teardown methods in unit testing. First, fixtures can be reused across multiple tests, which can save a lot of time and effort in setting up and tearing down test envirnoments. Second, fixtures can be parameterized, which allows for gearter flexibility in how tests are run. Finally, fixutres can be used to manage complex dependencies, such as database connections or thread pools.
### When would you want to use setUpModule() instead of setUpClass()?
If you want to initialize a database connection or something similar before running any tests in a module, then you would use setUpModule().If you want to set up a class for testing purpose, then you would use setUpClass().
### What does the skipif decorator mean in Python?
The skipif decorator is used to skip a test if a certain condition is met. For example, you might use this decorator to skip a test if a certain module is not installed.
### Is there any way to mark multiple tests for skipping at once?
Yes, there is a way to mark multiple tests for skipping at once. You can do this by using the @pytest.mark,skip() decorator.
### What is the difference between asserRaises(Exception) and assertRaisesRegexp(Exception)?
AssertRaises will check that an exception is raised during the exection of a certain block of code. AsserRaisesRegexp will do the same thing, but it will also check that the exception raised matches a certain regular expression.
### Can you explain what monkeypatching is?
Monkeypatching is the process of dynamically altering the behvaior of a function or object at runtime. This can be useful for testing purposes, as it allows you to mock out certain parts of your code in order to test how the rest of the code behaves.
### What do you understand about unittest vs pytest?
Unittest is a Python unit testing framework. Pytest is a Python testing tool. Both help you test your Python code. Unittest is part of the Python Standard Library, so it comes pre-installed with Python. Pytest is not part of the Standard Library, so you will need to install it separately. Pytest is newer than unittest and has a more flexible approach to testing. It is also eaiser to use and has more features.
### What happens if I try to run all tests in a directory with a wildcard expression?
All tests in the directory will be run.
### How can you define fixture scope in pytest?
Fixture scope defines how often a fixture is run. There are 4 different scopes that a fixture can have: function, class, module, and session.
 - Function scope is the default scope, and it means that the fixture is only going to run once per test function.
 - Class scope means that the fixture is going to run once per test class.
 - Module scope means that the fixture is going to run once per test module.
 - Session scope is the most broad scope, and it means that the fixture is going to run only once for the entire testing session.
### What are the different types of markers available in pytest?
There are 4 different types of markers available in pytest: skip, xfail, run and parametrize. 
 - skip is used to mark a test as being skipped
 - xfail is used to mark a test as expected to fail
 - run is used to mark a test as being able to be run
 - parametrize is used to mark a test as being able to be run with different parameters
### What is the purpose of pytest_namespace()?
The pytest_namespace() hook allows a plugin to expose additional objects and functions to the pytest namespace. This can be used to make custom fixtures or helper functions available to tests.
### How do you create custom hooks in pytest?
You can create custom hooks in pytest by creating your own pytest plugin. A pytest plugin is a class that inherits from the pytest.Plugin class. You can then add your custom hooks as methods on your plugin class.
### What are some examples of built-in python hooks provided by pytest?
 - pytest_addoption(parser)
 - pytest_configuration(config)
 - pytest_runtest_setup(item)
 - pytest_runtest_call(item)
 - pytest_runtest_teardown(item)
 - pytest_runtest_makereport(item,call)
 - pytest_collection_modifyitems(config,items)
 - pytest_unconfigure(config)
### What are plugins and why should we use them?
Plugins are a way to extend the functionality of Pytest. By using plugins, we can add new features or customize existing ones to better suit our needs. Additionally, plugins can be used to improve the speed and efficiency of our tests by reusing code or sharing data between tests.
### What are the differences between xUnit style setup/teardown methods and Python classmethods?
The main difference between xUnit style setup/teardown methods and Python classmethods is that the former are typically used to initialize and clean up test fixtures, while the latter are used to define class-level behaviour. Additionally, xUnit style setup/teardown methods are usually called once per test case, while Python classmethods can be called multiple times.
### What happens when you call slef.skipTest() from inside a test method?
When you call self.skipTest() from inside a test method, the test method is skipped and the next test method is executed.

## Sample For PyTest
### Basic Usage
```
# capitalize.py

def capital_case(x):
    return x.capitalize()
```
```
# test_capitalize.py

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'
```
### Raise Error

```
# capitalize.py

def capital_case(x):
    if not isinstance(x, str):
        raise TypeError('Please provide a string argument')
    return x.capitalize()
```
```
# test_capitalize.py

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)
```
### Use Fixtures
```
# wallet.py
class InsufficientAmount(Exception):
    pass

class Wallet:
    def __init__(self, ini_amount=0):
        self.balance=ini_amount
    
    def spend_cash(self, amount):
        if self.balance < amount:
           raise InsufficientAmount('Not enough available to spend')
        self.balance -= amount
    
    def add_cash(self, amount):
        self.balance += amount
```
```
# test_wallet.py

import pytest
from wallet import InsufficientAmount, Wallet

@pytest.fixture
def empty_wallet():
    """Returns a Wallet instance with a zero balance"""
    return Wallet()
    
@pytest.fixture
def wallet():
    """Return a Wallet instance with a balance of 20"""
    return Wallet(20)
    
def test_default_ini_amount(empty_wallet):
    assert empty_wallet.balance == 0

def test_ini_amount(wallet):
    assert wallet.balance == 20
    
data_used = (
    (30, 10, 20),
    (20, 2, 18)
)
@pytest.mark.parametrize("earned, spent, expected", data_used)
def test_transaction(empty_wallet, earned, spent, expected):
    empty_wallet.add_cash(earned)
    empty_wallet.spend_cash(spent)
    assert empty_wallet.balance == expected
    
def test_exception(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)
```

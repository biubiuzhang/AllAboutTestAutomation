# AllAboutTestAutomation
Learning materials of playwright

## Pre-requisite
 
 - VS Code
 - Python3
 - Create folder # main folder -> tests -> test_case.py

## Install packages

Install virtual environment under main folder
```
python3 -m venv venv	
source venv/bin/activate # Linux
venv\Scripts/activate.bat # Windows
```
Install playwirght and pytest
```
pip3 install playwright
pip3 install pytest
pip3 install pytest-playwright # pytest plug in for playwight
```
Check all the virtual environment packages
```
pip freeze
```
Install playwright browsers
```
playwright install # Install Chrome, Firfox, Webkit
```

## Write Test Cases

```
from playwright.sync_api import Page, expect

def test_basic_search():
	page.goto('https://www.google.ca')
	page.locator('id=identifierId').click()
	page.locator('text=name').fill('myname')
	page.locator('.a').wait_for()
	expect(page.locator('id=search_form_input')).to_have_value('panada')
	
```
## Run pytest

- headed means it is able to show the page, instead of sliently running at the background
```
python3 -m pytest tests --headed
```

## Debug (bash)
```
PWDEBUG=1 pytest -s
```
@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page:Page):
    print("beforeEach")
    page.goto("https://playwright.dev/")
    yield
    print("afterEach")
## Useful Function
```

```

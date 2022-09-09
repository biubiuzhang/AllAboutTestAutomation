from playwright.sync_api import Page

class DuckDuckGoSearchPage:
    # A bad practice
    URL = 'https://www.duckduckgo.com'
    
    # A good practice
    # Use input as URL, instead of coded it
    
    def __init__(self, page: Page) -> None:
        self.page = page
        self.search_input = page.locator('id=search_form_input_homepage')
        self.serach_button = page.locator('id=search_button_homepage')
    
    def load(self) -> None:
        self.page.goto(self.URL)

    def search(self, phrase: str) -> None:
        self.search_input.fill(phrase)
        self.serach_button.click()

    

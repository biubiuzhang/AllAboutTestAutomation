from playwright.sync_api import Page, expect

class DuckDuckGoResultPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.result_links = page.locator('.result_title a.result_a')
        self.search_input = page.locator('id=search_form_input')

    def result_link_titles(self) -> list[str]:
        self.result_links.nth(4).wait_for()
        return self.result_links.all_text_contents()

    def result_link_titles_contains_phrase(self, phrase: str, minimum: int = 1) -> bool:
        titles = self.result_link_titles()
        matches = [t for t in titles if phrase.lower() in t.lower()]
        return len(matches) >= minimum
        
from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage
from playwright.sync_api import Page
from playwright.sync_api import expect

def test_basic_duckduckgo_search(page: Page) -> None:
    search_page = DuckDuckGoSearchPage(page)
    result_page = DuckDuckGoResultPage(page)
    search_page.load()
    search_page.search('panada')
    expect(result_page.search_input).to_have_value('panada')
    assert result_page.result_link_titles_contains_phrase('panada')
    expect(result_page).to_have_title('panada at DuckDuckGo')
    pass
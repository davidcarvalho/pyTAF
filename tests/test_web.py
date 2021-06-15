import json

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pytaf.duckduckgo.pages.results import DuckDuckGoResultPage
from pytaf.duckduckgo.pages.search import DuckDuckGoSearchPage


def test_duckduckgo(browser):
    url = 'https://duckduckgo.com/'
    search_key = 'thinkpad'
    browser.get(url)

    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    search_page.search(search_key)

    results_page = DuckDuckGoResultPage(browser)
    assert results_page.link_div_count() > 0
    assert results_page.phrase_result_count(search_key) > 0
    assert results_page.search_input_value() == search_key

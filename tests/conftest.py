import pytest
from selene import browser

@pytest.fixture
def set_browser_size():
    browser.config.window_width = 1900
    browser.config.window_height = 1080


import pytest
from selene import browser, have


@pytest.fixture
def browser_open():
    browser.config.window_width = 900
    browser.config.window_height = 700


def test_browser_open(browser_open):
    print('Открывается браузер с заданными размерами')
    browser.open('https://www.google.ru/')
    browser.element('#APjFqb').click().type('asdfghjsdfgqasdfgujmyhnt5gbrf123sdfsdfsdfsdfsffd4132ewfefsdfs').press_enter()
    browser.element('#appbar').should(have.text('Результатов: примерно 0'))

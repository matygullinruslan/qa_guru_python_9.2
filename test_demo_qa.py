from selene import browser, have


def open_login_form():
    browser.open('https://demoqa.com/text-box')


def test_zapolnenie_polei():
    open_login_form()

    browser.element('#userName').type('Ruslan')
    browser.element('#userEmail').type('rusel_21@mail.ru')
    browser.element('#currentAddress').type('Moskow')
    browser.element('#permanentAddress').type('Ulyanovsk')
    browser.element('#submit').click()
    browser.element('.btn-primary').should(have.exact_text('Submit'))

from selene import browser, have

def test_succesfull_login():
    browser.open('https://niffler.qa.guru')
    browser.element('input[name="username"]').type('stas')
    browser.element('input[name="password"]').type('12345')
    browser.element('button[type="submit"]').click()

    browser.element('[id="spendings"]').should(have.text('History of Spendings'))
    browser.quit()

def test_succesfull_login_with_enter():
    browser.open('https://niffler.qa.guru')
    browser.element('input[name="username"]').type('stas')
    browser.element('input[name="password"]').type('12345').press_enter()

    browser.element('[id="spendings"]').should(have.text('History of Spendings'))
    browser.quit()

def test_unsuccesfull_login_with_wrong_credentials():
    browser.open('https://niffler.qa.guru')
    browser.element('input[name="username"]').type('stas')
    browser.element('input[name="password"]').type('123456').press_enter()

    browser.element('[class="form__error"]').should(have.text('Bad credentials'))
    browser.quit()

def test_succesfull_logout():
    browser.open('https://niffler.qa.guru')
    browser.element('input[name="username"]').type('stas')
    browser.element('input[name="password"]').type('12345').press_enter()
    browser.element('[id="spendings"]').should(have.text('History of Spendings'))

    browser.element('[aria-label="Menu"]').click()
    browser.element('//li[@role="menuitem"]').click()
    browser.element('//button[@type="button"]').click()
    browser.quit()
    
def test_succesfull_login_check_username():
    browser.open('https://niffler.qa.guru')
    browser.element('input[name="username"]').type('stas')
    browser.element('input[name="password"]').type('12345').press_enter()
    browser.element('[id="spendings"]').should(have.text('History of Spendings'))

    browser.open('https://niffler.qa.guru/profile')
    browser.element('[id="Username"]').should(have.text('stas'))
    browser.quit()

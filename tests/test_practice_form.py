from selene import browser, have, command
from selenium.webdriver import Keys
import os


def test_form(set_browser_size):
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('John')
    browser.element('#lastName').type('Dow')
    browser.element('#userEmail').type('john@dow.com')
    browser.element('#gender-radio-1 + .custom-control-label').click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').type(Keys.CONTROL + 'a' + Keys.NULL + '01 Mar 2000')
    browser.element('.subjects-auto-complete__input>input').type('c')
    browser.element('#react-select-2-option-2').click()
    browser.element('#hobbies-checkbox-2 + .custom-control-label').click()
    os.chdir(r'resources')
    browser.element('#uploadPicture').send_keys(os.getcwd() + r'\file.jpg')
    browser.element('#currentAddress').type('Faizabad Rd 22')
    browser.element('footer').perform(command.js.remove)
    browser.element('#state').click()
    browser.element('#react-select-3-option-1').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-1').click()
    browser.element('#submit').click()

    # check the form is filled out correctly
    browser.element('tr:nth-child(1)>td:nth-child(2)').should(have.exact_text('John Dow'))
    browser.element('tr:nth-child(2)>td:nth-child(2)').should(have.exact_text('john@dow.com'))
    browser.element('tr:nth-child(3)>td:nth-child(2)').should(have.exact_text('Male'))
    browser.element('tr:nth-child(4)>td:nth-child(2)').should(have.exact_text('1234567890'))
    browser.element('tr:nth-child(5)>td:nth-child(2)').should(have.exact_text('01 March,2000'))
    browser.element('tr:nth-child(6)>td:nth-child(2)').should(have.exact_text('Computer Science'))
    browser.element('tr:nth-child(7)>td:nth-child(2)').should(have.exact_text('Reading'))
    browser.element('tr:nth-child(8)>td:nth-child(2)').should(have.exact_text('file.jpg'))
    browser.element('tr:nth-child(9)>td:nth-child(2)').should(have.exact_text('Faizabad Rd 22'))
    browser.element('tr:nth-child(10)>td:nth-child(2)').should(have.exact_text('Uttar Pradesh Lucknow'))

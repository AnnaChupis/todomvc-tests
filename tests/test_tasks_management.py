from selene import have, be
from selene.support.shared import browser
browser.config.hold_browser_open = True

def test_CRUD():
    browser.open('https://todomvc4tasj.herokuapp.com')
    browser.element('#new-todo').should(be.enabled).wait_until('')

    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()
    browser.all('#todo-list li').should(have.exact_texts('a', 'b', 'c'))

    browser.all('#todo-list li').element_by(have.exact_text('b')).double_click()
    browser.all('#todo-list li').element_by(have.css_class('editing')) \
        .element('.edit').type(' edited').press_enter()

    browser.all('#todo-list li').element_by(have.exact_text('b edited')) \
        .element('.toggle').click()
    browser.element('#clear-completed').click()
    browser.all('#todo-list li').should(have.exact_texts('a', 'c'))

    browser.all('#todo-list li').element_by(have.exact_text('c')).double_click()
    browser.all('#todo-list li').element_by(have.css_class('editing')) \
        .element('.edit').type(' to be canceled').press_escape()

    browser.all('#todo-list li').element_by(have.exact_text('c')) \
        .element('.destroy').click()
    browser.all('#todo-list li').should(have.exact_texts('a'))

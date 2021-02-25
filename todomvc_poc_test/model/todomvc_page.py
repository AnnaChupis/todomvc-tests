from selene import have, command
from selene.support.shared import browser
from selenium.webdriver.common.keys import Keys

be_completed = have.css_class('completed')
be_active = have.no.css_class('completed')

class TodoMvcPage:
    def __init__(self, ):
        self.browser = browser
        self.todo_list = browser.all('#todo-list li')


    def open(self):
        self.browser.open('https://todomvc4tasj.herokuapp.com').\
        should(have.js_returned(True, 'return Object.keys(require.s.contexts._.defined).length == 39'))


    def add(self,*todos: str):
        for todo in todos:
            self.browser.element('#new-todo').type(todo).press_enter()


    def given_opened_with(self, *todos: str):
        self.open()
        self.add(*todos)


    def rewrite_selected(self,todo: str,new_text: str):
        self.todo_list.element_by(have.exact_text(todo)).double_click()
        return self.todo_list.element_by(have.css_class('editing')).element('.edit'). \
        perform(command.js.set_value(new_text))


    def edit(self,todo: str,new_text: str,key=Keys.ENTER):
        self.rewrite_selected(todo,new_text).press(key)


    def toggle(self,todo: str):
        self.todo_list.element_by(have.exact_text(todo)).element('.toggle').click()


    def toggle_all(self):
        self.browser.element('#toggle-all').click()


    def clear_completed(self):
        self.browser.element('#clear-completed').click()


    def cancel_edit(self,todo: str,new_text: str):
        self.rewrite_selected(todo,new_text).press_escape()


    def delete(self,*todos: str):
        self.todo_list.element_by(have.exact_text(*todos)).hover().element('.destroy').click()


    def should_have(self,*todos: str):
        self.todo_list.should(have.exact_texts(*todos))


    def should_have_items_left(self,number: int):
        self.browser.element('#todo-count strong').should(have.exact_text(str(number)))


    def should_have_empty_todolist(self):
        self.todo_list.should(have.size(0))


    def should_be_active(self,*todos: str):
        self.todo_list.filtered_by(be_active).should(have.exact_texts(*todos))


    def should_be_complete(self, *todos: str):
        self.todo_list.filtered_by(be_completed).should(have.exact_texts(*todos))

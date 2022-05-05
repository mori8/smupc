from selenium import webdriver
from selenium.webdriver.common.by import By
import secrets


class DomjudgeController:
    def __init__(self, domjudge_url='http://smupc.online'):
        self.domjudge_url = domjudge_url
        self.driver = webdriver.Chrome(executable_path='./chromedriver')

    def move_to(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(2)

    def signin(self, username, password):
        self.move_to(url=self.domjudge_url + '/login')
        self.fill_input(username, input_xpath='//*[@id="username"]')
        self.fill_input(password, input_xpath='//*[@id="inputPassword"]')
        self.click_button(button_xpath='//*[@id="loginform"]/div/form/button')

    def create_team_member(self, team_id, user_name):
        user_info = {}
        self.move_to(url=self.domjudge_url + '/jury/teams/' + team_id)
        password = secrets.token_urlsafe(12)

        user_info['team_id'] = team_id
        user_info['username'] = user_name
        user_info['password'] = password

        add_team_user_button = '/html/body/div/div/div/div[1]/div[1]/table/tbody/tr[7]/td/a'
        self.click_button(button_xpath=add_team_user_button)

        self.fill_input(user_name, input_xpath='//*[@id="user_username"]')
        self.fill_input(user_name, input_xpath='//*[@id="user_name"]')
        self.fill_input(password, input_xpath='//*[@id="user_plainPassword"]')

        self.click_button(button_xpath='//*[@id="user_user_roles"]/div[3]/label')

        return user_info

    def set_team_name(self, team_id, team_name):
        self.move_to(url=self.domjudge_url + '/jury/teams/' + team_id + '/edit')

        self.fill_input(team_name, input_xpath='//*[@id="team_displayName"]')
        self.click_button(button_xpath='//*[@id="team_save"]')

    def fill_input(self, value, input_xpath):
        input_element = self.driver.find_element(by=By.XPATH, value=input_xpath)
        input_element.send_keys(value)

    def click_button(self, button_xpath):
        button_element = self.driver.find_element(by=By.XPATH, value=button_xpath)
        button_element.click()
        self.driver.implicitly_wait(2)





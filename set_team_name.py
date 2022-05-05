import csv
import secrets
from selenium import webdriver

from selenium.webdriver.common.by import By

domjudge_url = 'http://211.253.25.227'
admin_password = 'ca-HWJ9jt7h5foIB'
driver = webdriver.Chrome(executable_path='./chromedriver')

# login
driver.get(url=domjudge_url+'/login')
driver.implicitly_wait(2)

username_input = driver.find_element(by=By.XPATH, value='//*[@id="username"]')
username_input.send_keys('admin')

password_input = driver.find_element(by=By.XPATH, value='//*[@id="inputPassword"]')
password_input.send_keys(admin_password)

signin_button = driver.find_element(by=By.XPATH, value='//*[@id="loginform"]/div/form/button')
signin_button.click()

with open('attendances.csv', 'r', newline='') as file:
    reader = csv.DictReader(file)
    index = 1
    for row in reader:
        team_display_name = row['대회 참가명']
        team_id = str(index + 2 if index < 83 else index + 3)
        driver.get(url=domjudge_url+'/jury/teams/'+team_id+'/edit')

        display_name = driver.find_element(by=By.XPATH, value='//*[@id="team_displayName"]')
        display_name.send_keys(team_display_name)

        save_button = driver.find_element(by=By.XPATH, value='//*[@id="team_save"]')
        save_button.click()

        index += 1
        driver.implicitly_wait(2)

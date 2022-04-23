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

# create users and save accounts info
with open('accounts.csv', 'w', newline='') as account_file:
    csv_writer = csv.writer(account_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(1, 80):
        driver.get(url=domjudge_url+'/jury/teams/' + str(i + 2))
        username = 'team0' + ('0%d' % i if i < 10 else '%d' % i)
        password = secrets.token_urlsafe(12)

        print(", ".join([username, password]))
        csv_writer.writerow([username, password])

        add_team_user_link = driver.find_element(by=By.XPATH,
                                                 value='/html/body/div/div/div/div[1]/div[1]/table/tbody/tr[7]/td/a')
        add_team_user_link.click()

        user_username_input = driver.find_element(by=By.XPATH, value='//*[@id="user_username"]')
        user_fullname_input = driver.find_element(by=By.XPATH, value='//*[@id="user_name"]')
        user_password_input = driver.find_element(by=By.XPATH, value='//*[@id="user_plainPassword"]')
        roles_input = driver.find_element(by=By.XPATH, value='//*[@id="user_user_roles"]/div[3]/label')
        roles_input.click()

        user_username_input.send_keys(username)
        user_fullname_input.send_keys(username)
        user_password_input.send_keys(password)

        save_button = driver.find_element(by=By.XPATH, value='//*[@id="user_save"]')
        save_button.click()
        driver.implicitly_wait(2)

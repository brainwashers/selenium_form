# Open https://the-internet.herokuapp.com/login

# Please automate next test cases:
# 1. Login with valid creds (tomsmith/SuperSecretPassword!) and assert you successfully logged in
# 2. Login with invalid creds and check validation error
# 3. Logout from app and assert you successfully logged out


from selenium import webdriver


login1 = "tomsmith"
login2 = "tomsmith1"
password = "SuperSecretPassword!"


def test1():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element_by_css_selector('#username').send_keys(login1)
    driver.find_element_by_css_selector('#password').send_keys(password)
    driver.find_element_by_css_selector('#login > button').click()
    assert 'You logged into a secure area!' in driver.page_source
    driver.quit()


def test2():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element_by_css_selector('#username').send_keys(login2)
    driver.find_element_by_css_selector('#password').send_keys(password)
    driver.find_element_by_css_selector('#login > button').click()
    assert 'Your username is invalid!' in driver.page_source
    driver.quit()


def test3():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element_by_css_selector('#username').send_keys(login1)
    driver.find_element_by_css_selector('#password').send_keys(password)
    driver.find_element_by_css_selector('#login > button').click()
    assert 'You logged into a secure area!' in driver.page_source
    driver.find_element_by_css_selector('#content > div > a > i').click()
    assert 'logged out' in driver.page_source
    driver.quit()


test1()
test2()
test3()
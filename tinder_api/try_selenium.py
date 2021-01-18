"""
This unfortunately does not work. Other people have also problems logging in through google.
https://gist.github.com/ikegami-yukino/51b247080976cb41fe93
"""

from selenium.webdriver.common.keys import Keys
from seleniumwire import webdriver
from google_secret import username, password



#from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('user-agent = Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
driver = webdriver.Chrome(chrome_options=options, executable_path=r"D:\python\chromedriver_win32\chromedriver.exe")

driver.get('https://tinder.com')

sleep(2)

login_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
login_button.click()

cookies_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/button')
cookies_button.click()

gmail_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[1]/div/button')
gmail_button.click()
#gmail_button.send_keys(Keys.ENTER)


# switch to login popup
base_window = driver.window_handles[0]
driver.switch_to.window(driver.window_handles[2])

email_input = driver.find_element_by_xpath(r'/html/body/div/div[2]/div[2]/div[1]/form/div/div/div/div/div/input[1]')
email_input.send_keys(username)

next_button = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/form/div/div/input')
next_button.click()

pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
pw_in.send_keys(password)

login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
login_btn.click()

self.driver.switch_to_window(base_window)

popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
popup_1.click()

popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
popup_2.click()
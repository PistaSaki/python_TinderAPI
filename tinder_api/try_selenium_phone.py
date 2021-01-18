from selenium.webdriver.common.keys import Keys
from seleniumwire import webdriver
from google_secret import username, password



#from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('user-agent = Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
driver = webdriver.Chrome(chrome_options=options, executable_path=r"D:\python\chromedriver_win32\chromedriver.exe")

driver.get('https://tinder.com')

driver.implicitly_wait(20)

login_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
login_button.click()
##
print("Now manually login with phone number.")

def find_token():
    driver.get('https://tinder.com/app/recs')
    for request in driver.requests:
        for key, value in request.headers.items():
            if key == 'X-Auth-Token':
                return value

    raise Exception("did not find token")



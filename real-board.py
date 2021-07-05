from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#setup your details here
CLIENT_ID=""
USERNAME=""
PASSWORD=""

import sys 
if len(sys.argv)>1 and sys.argv[1]=="out":
        text = 'דיווח יציאה'
else:   
        text = 'דיווח כניסה'

print(text)

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://watt.real-board.com/#/")
assert "RealBoard Portal" in driver.title

elem = driver.find_element_by_css_selector("input[aria-label='מספר לקוח']");
elem.clear()
elem.send_keys(CLIENT_ID)

elem = driver.find_element_by_css_selector("input[aria-label='שם משתמש']");
elem.clear()
elem.send_keys(USERNAME)

elem = driver.find_element_by_css_selector("input[aria-label='סיסמה']");
elem.clear()
elem.send_keys(PASSWORD)

elem.send_keys(Keys.RETURN)

#wait for page to load
sleep(2)

elem = driver.find_elements_by_xpath("//div[contains(text(), '"+text+"')]")
print(elem)
elem[0].click()

driver.close()

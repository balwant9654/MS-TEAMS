from selenium.webdriver.common.keys import Keys
import TeamClick as TC
import time

driver = TC.TeamsClick()

element = driver.find_element_by_tag_name("body")

print("[%] Scrolling Up ..")

for i in range(6):
    element.send_keys(Keys.PAGE_UP)
    time.sleep(0.5)
    

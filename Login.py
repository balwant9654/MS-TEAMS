from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

def Login(Email,Password):

    try:

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        
        driver = webdriver.Chrome(options=chrome_options)
        
        login = "https://www.microsoft.com/en-in/microsoft-teams/log-in"
        driver.get(login)
        SignIn = driver.find_element_by_link_text("Sign in")
        SignIn.click()

        time.sleep(5)
    
        window_after = driver.window_handles
        driver.switch_to.window(window_after[1])

        driver.find_element_by_id("i0116").send_keys(Email)
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("i0118").send_keys(Password)
    
        time.sleep(5)
    
        driver.find_element_by_xpath("//input[@value='Sign in']").click()
        window_after = driver.window_handles
        driver.switch_to.window(window_after[1])
        driver.find_element_by_xpath("//input[@value='Yes']").click()

        time.sleep(10)
        
        window_after = driver.window_handles
        driver.switch_to.window(window_after[1])

        current_link = driver.current_url
        message = "Logged In Successfully"
        driver = driver

    except:

        current_link = "Wrong Email or Password"
        message = "Failed to Logged In"
        driver = None

    return current_link,message,driver

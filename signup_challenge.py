from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com")
time.sleep(1)

f_name = driver.find_element(By.NAME, value="fName")
f_name.send_keys("Shahzada")
time.sleep(1)

l_name = driver.find_element(By.NAME, value="lName")
l_name.send_keys("Latif")
time.sleep(1)

email = driver.find_element(By.NAME, value="email")
email.send_keys("madasar5432@gmail.com")
time.sleep(1)

signup_button = driver.find_element(By.CSS_SELECTOR, value="button")
signup_button.send_keys(Keys.ENTER)
time.sleep(2)



driver.quit()
















from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie")


# 1: Clicking cookie
time_to_end = time.time() + 60
while time.time() <= time_to_end:

    timeout = time.time() + 5
    while time.time() <= timeout:
        cookie_button = driver.find_element(By.ID, value="cookie")
        cookie_button.click()

    money = driver.find_element(By.ID, value="money").text
    print(money)

    if int(money) > int(driver.find_element(By.XPATH, value='//*[@id="buyTime machine"]/b').text.split()[3].replace(',','')):
        buyTime_machine = driver.find_element(By.ID, value="buyTime machine")
        buyTime_machine.click()
    elif int(money) > int(driver.find_element(By.XPATH, value='//*[@id="buyPortal"]/b').text.split()[2].replace(',','')):
        buyPortal = driver.find_element(By.ID, value="buyPortal")
        buyPortal.click()
    elif int(money) > int(driver.find_element(By.XPATH, value='//*[@id="buyAlchemy lab"]/b').text.split()[3].replace(',','')):
        buyAlchemy = driver.find_element(By.ID, value="buyAlchemy lab")
        buyAlchemy.click()
    elif int(money) > int(driver.find_element(By.XPATH, value='//*[@id="buyShipment"]/b').text.split()[2].replace(',','')):
        buyShipment = driver.find_element(By.ID, value="buyShipment")
        buyShipment.click()
    elif int(money) > int(driver.find_element(By.XPATH, value='//*[@id="buyMine"]/b').text.split()[2].replace(',','')):
        buyMine = driver.find_element(By.ID, value="buyMine")
        buyMine.click()
    elif int(money) > int(driver.find_element(By.XPATH, value='//*[@id="buyFactory"]/b').text.split()[2]):
        buyFactory = driver.find_element(By.ID, value="buyFactory")
        buyFactory.click()
    elif int(money) > int(driver.find_element(By.XPATH, value='//*[@id="buyGrandma"]/b').text.split()[2]):
        buyGrandma = driver.find_element(By.ID, value="buyGrandma")
        buyGrandma.click()
    elif int(money) > int(driver.find_element(By.XPATH, value='//*[@id="buyCursor"]/b').text.split()[2]):
        buyCursor = driver.find_element(By.ID, value="buyCursor")
        buyCursor.click()
    else:
        pass

print(driver.find_element(By.ID, value="cps").text)























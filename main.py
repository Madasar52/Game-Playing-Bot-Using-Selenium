from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options= chrome_options)
driver.get("https://www.python.org")

events_data = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
event_list = events_data.text.split("\n")
data_dict = {}
n = 0

for n in range(9):
    data_dict[n] = {"time": event_list[n], "name": event_list[n+1]}
    n+=1

print(data_dict)




















# driver.close()
driver.quit()


















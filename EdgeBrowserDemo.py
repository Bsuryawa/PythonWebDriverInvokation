from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service_obj = Service (r"C:\Users\BHAGYASHRI\Downloads\edgedriver_win64\msedgedriver")
driver =webdriver.Edge(service=service_obj)
driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()
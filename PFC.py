import time #time sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://localhost:8111")

user = driver.find_element(By.ID, "user")
user.clear()
user.send_keys("root")

pw = driver.find_element(By.NAME, "pass")
pw.clear()
pw.send_keys("password")

driver.find_element(By.XPATH, "//input[contains(@type,'submit')]").click()
driver.get("http://localhost:8111")

botonNuevo = driver.find_element(By.XPATH, "//input[@value='Create new ticket']")
botonNuevo.click()
asunto = driver.find_element(By.XPATH, "//input[@name='Subject']")
asunto.send_keys("Este es un mensaje de prueba")

driver.find_element(By.XPATH, "//input[@name='SubmitTicket']").click()

driver.close()
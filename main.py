import selenium
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("chromedriver")
driver.get("https://www.instagram.com")
sleep(2)
username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
username.send_keys("selenium55")
password.send_keys("Kartik@#11")
login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()
sleep(5)
search = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
search.send_keys("23kartikk")
search.send_keys(Keys.ENTER)
sleep(5)
enter = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[1]/div/div/div")
enter.click()
sleep(5)
follow = driver.find_element_by_css_selector("#react-root > section > main > div > header > section > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div > span > span.vBF20._1OSdk > button")
follow.click()
sleep(2)
driver.close()



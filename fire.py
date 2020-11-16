from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


path_to_firefox = 'D:/Programming/geckodriver.exe'
driver = webdriver.Firefox(executable_path=path_to_firefox)

web_path = 'https://www.halfords.com/bikes/mountain-bikes/carrera-titan-mens-full-suspension-mountain-bike---s-m-l-frames-green%2Fgrey-850633.html'
driver.get(web_path)

time.sleep(5)

element = driver.find_element_by_name('q')
element.send_keys('Carrera')
element.send_keys(Keys.RETURN)

# driver.find_element_by_name('simpleSearch').send_keys('Carrera')
# headerSearchForm
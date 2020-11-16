from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


# variables (binary, url)
#
path_to_firefox = 'D:/Programming/geckodriver.exe'
web_path = 'https://www.halfords.com/bikes/mountain-bikes/carrera-titan-mens-full-suspension-mountain-bike---s-m-l-frames-green%2Fgrey-850633.html'


# initialize firefox, load page
#
driver = webdriver.Firefox(executable_path=path_to_firefox)
driver.maximize_window()
#time.sleep(1)
driver.get(web_path)
time.sleep(1)


# main scrolling and clicking
#
# pick size
#
driver.execute_script("window.scrollTo(0, 300)") 
time.sleep(1)
size_choice = driver.find_element_by_xpath("//div[@id='productInfoBlock']/div[5]/div/div/div/div/ul/li[2]/a/span")
size_choice.click()
time.sleep(1)


# pick location
#
driver.execute_script("window.scrollTo(0, 1080)") 
time.sleep(1)
address_input = driver.find_element_by_xpath("//div[@id='productInfoBlock']/div[5]/div[3]/div/div/div/form/div/div/div/div/div/input")
address_input.send_keys('Carlisle\n')
submit_click = driver.find_element_by_xpath("//div[@id='productInfoBlock']/div[5]/div[3]/div/div/div/form/div/div/div[2]/button")
submit_click.click()

time.sleep(2)
# answer = driver.find_element_by_xpath("//div[@id='productInfoBlock']/div[5]/div[3]/div/div/div[3]/div/div/div/span").text
answer = driver.find_element_by_class_name("b-product-home__error").text

print(answer)

driver.quit()



'''
//div[@id='productInfoBlock']/div[5]/div[3]/div/div/div[3]/div/div/div/span

check_home_delivery = driver.page_source
if ("This product is not available for Home Delivery." in check_home_delivery):
    print('Product unavailable...')
else:
    print('Available. Sending email.')


This product is not available for Home Delivery.
element = driver.find_element_by_name('q')
element.send_keys('Carrera')
element.send_keys(Keys.RETURN)



driver.find_element_by_name('simpleSearch').send_keys('Carrera')
headerSearchForm
b-product-nav__link js-attribute-swatch  
'''
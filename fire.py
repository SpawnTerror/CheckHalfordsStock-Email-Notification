from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import configparser

''' temporary
config = configparser.ConfigParser()
config.read('config.ini')

password = config.get('MAIN', 'password')
email = config.get('MAIN', 'email')
'''


# variables
print('Initializing variables, Halfords url and Firefox driver...\n')
fireFoxOptions = webdriver.FirefoxOptions()
# fireFoxOptions.set_headless()
path_to_firefox = 'D:/Programming/geckodriver.exe'
web_path = 'https://www.halfords.com/bikes/mountain-bikes/carrera-titan-mens-full-suspension-mountain-bike---s-m-l-frames-green%2Fgrey-850633.html'

def scrap():

    # initialize firefox, load page
    driver = webdriver.Firefox(executable_path=path_to_firefox, options=fireFoxOptions)
    driver.maximize_window()
    driver.get(web_path)
    time.sleep(2)

    # main scrolling and clicking
    driver.execute_script("window.scrollTo(0, 300)") 
    time.sleep(2)
    size_choice = driver.find_element_by_xpath("//div[@id='productInfoBlock']/div[5]/div/div/div/div/ul/li[2]/a/span")
    size_choice.click()
    time.sleep(2)

    # pick location
    driver.execute_script("window.scrollTo(0, 1080)") 
    time.sleep(2)
    address_input = driver.find_element_by_xpath("//div[@id='productInfoBlock']/div[5]/div[3]/div/div/div/form/div/div/div/div/div/input")
    address_input.send_keys('Carlisle\n')
    submit_click = driver.find_element_by_xpath("//div[@id='productInfoBlock']/div[5]/div[3]/div/div/div/form/div/div/div[2]/button")
    submit_click.click()
    time.sleep(2)

    # read status once
    answer = driver.find_element_by_class_name("b-product-home__error").text
    print(answer)

    answer = "xxx" # for 

    if answer == "This product is not available for Home Delivery.":
        print('Not in stock yet.')
        driver.quit()
        return False
    else:
        print('In stock, sending notification.')
        driver.quit()
        return True


if __name__ == '__main__':
    print('Starting scrapping Halfords...\n')
    
    while scrap() == False:
        scrap()
        time.sleep(5)
        print('Sleeping for 5 seconds.')
    print('Found some stock. Exiting just now.')








'''
send_notification('sp4wnt3rr0r@gmail.com')
driver.quit()
'''

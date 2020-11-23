from selenium import webdriver
import platform
import time



# System inits for Windows and Linux
def init_windows():
    print('Windows detected. Starting in headless mode...\n')
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    path_to_firefox = 'D:/Programming/geckodriver.exe'
    web_path = 'https://www.halfords.com/bikes/mountain-bikes/carrera-titan-mens-full-suspension-mountain-bike---s-m-l-frames-green%2Fgrey-850633.html'
    looper = False
    return path_to_firefox, web_path, looper

def init_linux():
    print('Initializing variables, Halfords url and Firefox driver...\n')
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.add_argument("--headless")
    path_to_firefox = '/home/spawn/programming/halfords/drivers/geckodriver'
    web_path = 'https://www.halfords.com/bikes/mountain-bikes/carrera-titan-mens-full-suspension-mountain-bike---s-m-l-frames-green%2Fgrey-850633.html'
    looper = False
    return path_to_firefox, web_path, looper

def scrap():

    # initialize firefox, load page
    driver = webdriver.Firefox(executable_path=path_to_firefox, options=fireFoxOptions)
    driver.set_window_position(0, 0)
    driver.set_window_size(1920, 1080)

    # driver.maximize_window()
    driver.get(web_path)
    time.sleep(2)
    screenshoted('screen1.png', 'Set 1920 1080 window') 

    # scroll down to size selector
    driver.execute_script("window.scrollTo(0, 300)")
    time.sleep(2)
    screenshoted('screen2.png', 'Scrolling down to size selector')

    # selecting size
    size_choice = driver.find_element_by_xpath("//div[@id='productInfoBlock']/div[5]/div/div/div/div/ul/li[2]/a/span")
    size_choice.click()
    time.sleep(2)
    screenshoted('screen3.png', 'Selecting Medium')

    # scroll down to location
    driver.execute_script("window.scrollTo(0, 1080)")
    time.sleep(2)
    screenshoted('screen4.png', 'Scrolling down to location input textbox')

    # enter location and click submit
    address_input = driver.find_element_by_xpath("//div[@id='productInfoBlock']/div[5]/div[3]/div/div/div/form/div/div/div/div/div/input")
    address_input.send_keys('Carlisle\n')
    submit_click = driver.find_element_by_xpath("//div[@id='productInfoBlock']/div[5]/div[3]/div/div/div/form/div/div/div[2]/button")
    submit_click.click()
    time.sleep(2)
    screenshoted('screen5.png', 'Submited Carlisle')

    try:
        self.driver.find_element_by_xpath(xpath).click()
        add_to_basket = driver.find_element_by_xpath("//div[@id='productInfoBlock']/div[5]/div/div/div/div/ul/li[2]/a/span")
        size_choice.click()
    except Exception:
        time.sleep(5)
        print('No button on the page yet, sleeping 5 seconds!')
        self.clickButton('//button[contains(.,'Add to Basket')]')


    #xpath=//button[contains(.,'Add to Basket')]

    # checking status
    #answer = driver.find_element_by_class_name("b-product-home__error").text
    #print(answer)
    #time.sleep(2)
    screenshoted('Screen6.png', 'Checking availablitiy and message')

    # send email if in stock logic, if not then loop again
    if answer == "This product is not available for Home Delivery.":
        print('STATUS: Not in stock yet.')
        looper = False
        driver.quit()

    else:
        print('STATUS: In stock, sending notification.')
        looper = True
        driver.quit()
    return looper 

# Screenshot function
def screenshoted(file_name, comment):
    driver.save_screenshot(file_name)
    print(comment)

# Main function
# OS check
operating_system = platform.system()
if operating_system == 'Windows':
    print(f'Detected {operating_system}. Initializing...')
    init_windows()
elif operating_system == 'Linux':
    print(f'Detected {operating_system}. Initializing...')
    init_linux()
else:
    print(f'Detected {operating_system}. Exiting...')




# Carry on
if __name__ == '__main__':
    print('Starting scrapping Halfords...\n')
    while looper == False:
        scrap()
        time.sleep(5)
        print('Sleeping for 5 seconds.')
    print('Found some stock. Exiting just now.')




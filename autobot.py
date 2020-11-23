from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

import platform
import time
# import configparser



def akcja():
    fireFoxOptions = webdriver.FirefoxOptions()
    # fireFoxOptions.set_headless()
    path_to_firefox = 'D:/Programming/geckodriver.exe'
    # web_path = 'https://www.halfords.com/bikes/mountain-bikes/carrera-titan-mens-full-suspension-mountain-bike---s-m-l-frames-green%2Fgrey-850633.html'
    web_path = 'https://www.halfords.com/bikes/mountain-bikes/carrera-vengeance-mens-mountain-bike-2020---black---xs-s-m-l-xl-frames-340910.html'
    looper = False

    driver = webdriver.Firefox(executable_path=path_to_firefox, options=fireFoxOptions)
    driver.set_window_position(0, 0)
    driver.set_window_size(1920, 1080)

    driver.get(web_path)
    time.sleep(2)

    driver.execute_script("window.scrollTo(0, 300)")
    time.sleep(2)

    size_choice = driver.find_element_by_xpath("//div[@id='productInfoBlock']/div[5]/div/div/div/div/ul/li[2]/a/span")
    size_choice.click()
    time.sleep(2)

    driver.execute_script("window.scrollTo(0, 1080)")
    time.sleep(2)

    address_input = driver.find_element_by_xpath("//div[@id='productInfoBlock']/div[5]/div[3]/div/div/div/form/div/div/div/div/div/input")
    address_input.send_keys('Carlisle\n')
    submit_click = driver.find_element_by_xpath("//div[@id='productInfoBlock']/div[5]/div[3]/div/div/div/form/div/div/div[2]/button")
    submit_click.click()
    time.sleep(2)
    return driver



def klikaj():
    try:
        add_to_basket = driver.find_element_by_xpath("//div[@id='productInfoBlock']/div[5]/div[3]/div/div/div[3]/div/div/div[2]/div[2]/button")
        add_to_basket.click()
    except Exception:
        time.sleep(5)
        print('No button on the page yet, sleeping 5 seconds!')
        klikaj()


akcja()
klikaj()
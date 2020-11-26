#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SpawnTerror 2020

from selenium import webdriver
import platform
import os
import time
from email_me import send_notification
from time import gmtime, strftime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class bocik(object):

    def __init__(self):
        self.path_to_firefox = ''
        self.web_path = ''
        self.fireFoxOptions = ''
        self.not_in_stock = True
        self.file_name = ''
        self.comment = 'Default comment'

    def oprint(*args):
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()), *args)
        

    def init_windows(self):
        clear = lambda: os.system('cls')
        clear()

        bocik.oprint(f"Detected system: {bcolors.OKGREEN}Windows{bcolors.ENDC}\n")
        self.fireFoxOptions = webdriver.FirefoxOptions()
        self.fireFoxOptions.add_argument("--headless")
        self.path_to_firefox = 'D:/Programming/geckodriver.exe'

        # here is the link for the item
        self.web_path = 'https://www.halfords.com/bikes/mountain-bikes/carrera-titan-mens-full-suspension-mountain-bike---s-m-l-frames-green%2Fgrey-850633.html'
        
    def init_linux(self):
        clear = lambda: os.system('clear')
        clear()

        bocik.oprint(f"Detected system: {bcolors.OKGREEN}Linux{bcolors.ENDC}\n")
        self.fireFoxOptions = webdriver.FirefoxOptions()
        self.fireFoxOptions.add_argument("--headless")
        self.path_to_firefox = '/home/spawn/programming/halfords/drivers/geckodriver'

        # here is the link for the item
        self.web_path = 'https://www.halfords.com/bikes/mountain-bikes/carrera-titan-mens-full-suspension-mountain-bike---s-m-l-frames-green%2Fgrey-850633.html'
        
    def check_system(self):
        self.operating_system = platform.system()
        
        if self.operating_system == 'Windows':
            bocik.init_windows(self)
            run = "True"
        elif self.operating_system == 'Linux':
            bocik.init_linux(self)
            run = "True"
        else:
            bocik.oprint(f"Detected system: {bcolors.OKGREEN}{self.operating_system}{bcolors.ENDC}!\n")
            bocik.oprint(f"Only {bcolors.OKGREEN}Windows{bcolors.ENDC} and {bcolors.OKGREEN}Linux{bcolors.ENDC} is supported.\n")
            run = "False"
        return run
    
    def akcja(self):

        # --- for testing only, first one not in stock (target), second one is random in stock (test) ---
        # self.web_path = 'https://www.halfords.com/bikes/mountain-bikes/carrera-titan-mens-full-suspension-mountain-bike---s-m-l-frames-green%2Fgrey-850633.html'
        # self.web_path = 'https://www.halfords.com/bikes/mountain-bikes/carrera-vengeance-mens-mountain-bike-2020---black---xs-s-m-l-xl-frames-340910.html'
        # ------------------------

        self.driver = webdriver.Firefox(executable_path=self.path_to_firefox, options=self.fireFoxOptions)
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(1920, 1080)
        self.driver.get(self.web_path)
        time.sleep(2)

        # screening
        self.driver.save_screenshot('1windowopen.png')

        self.driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(2)

        # screening
        self.driver.save_screenshot('2scrolleddown.png')

        size_choice = self.driver.find_element_by_xpath("//div[@id='productInfoBlock']/div[5]/div/div/div/div/ul/li[2]/a/span")
        size_choice.click()
        time.sleep(2)

        # screening
        self.driver.save_screenshot('3sizechoiceclicked.png')

        self.driver.execute_script("window.scrollTo(0, 1380)")
        time.sleep(2)

        # screening
        self.driver.save_screenshot('4scrolledtotextbox.png')

        address_input = self.driver.find_element_by_xpath("//div[@id='productInfoBlock']/div[5]/div[3]/div/div/div/form/div/div/div/div/div/input")
        address_input.send_keys('Carlisle\n')
        submit_click = self.driver.find_element_by_xpath("//div[@id='productInfoBlock']/div[5]/div[3]/div/div/div/form/div/div/div[2]/button")
        submit_click.click()
        time.sleep(4)
        
        # screening
        self.driver.save_screenshot('5enteringcarlisle.png')

        while self.not_in_stock == True:
            try:
                add_to_basket = self.driver.find_element_by_xpath("//div[@id='productInfoBlock']/div[5]/div[3]/div/div/div[3]/div/div/div[2]/div[2]/button")
                add_to_basket.click()
                time.sleep(2)
                bocik.oprint(f"{bcolors.WARNING}Product in stock. Sending email notification!{bcolors.ENDC}")
                haha.got_it(announce = "Closing web scrapper script, exiting...")
                run = "False"

                # screening
                self.driver.save_screenshot('6instock.png')

                self.driver.quit()
                return run

            except Exception:
                time.sleep(2)
                bocik.oprint(f"{bcolors.FAIL}Not in stock yet, restarting...{bcolors.ENDC}")
                self.driver.quit()
                bocik.oprint(f"{bcolors.OKBLUE}Sleeping for {sleeping_time/60} minutes.{bcolors.ENDC} \n")
                time.sleep(sleeping_time)

                # screening
                self.driver.save_screenshot('6notinstock.png')

                run = "True"
                return run

    def got_it(self, announce):
        self.announce = announce
        bocik.oprint(self.announce)
        bocik.oprint(f"{bcolors.OKBLUE}Finished...{bcolors.ENDC}\n")  

# VARIABLES
run = "True"
sleeping_time = 5 # in seconds

# MAIN PROCEDURE
if __name__ == '__main__':  
    haha = bocik()
    haha.check_system()
    while run == "True":
        run = haha.akcja()
    send_notification('Visit Halfords now!', 'Stock alert')


        

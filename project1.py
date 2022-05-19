#import libraries#

from selenium import webdriver
from selenium .webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
##creating a class for url##
class Jhansi:
    driver=webdriver.Firefox()
    url="https://www.zenclass.in/"

    def project(self,url):
        element=self.driver.get(url)
        element=self.driver.find_element(by=By.XPATH,value='/html/body/div/div/div/div[1]/div[2]/div/div[1]/form/div[1]/div/input').send_keys("jhansi4a1@gmail.com")
        element=self.driver.find_element(by=By.XPATH,value='/html/body/div/div/div/div[1]/div[2]/div/div[1]/form/div[2]/div/input').send_keys("Guvi@2022")
        submit_button=self.driver.find_element(by=By.XPATH,value='/html/body/div/div/div/div[1]/div[2]/div/div[1]/form/button').click()
    
p=Jhansi()
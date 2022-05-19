#import libraries#

from selenium import webdriver
from selenium .webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import requests
import csv
##creating the class for specify the url##
class scrapping:
    driver=webdriver.Firefox()
    url="https://www.zenclass.in/"
##query the website and return the html to the data##
    data=requests.get(url)
##parse the html using beautifulsoup and store in variable soup###
    soup=BeautifulSoup(data.content,'lxml')
##login needfulls of the website##    
    element=driver.get(url)
    element=driver.find_element(by=By.XPATH,value='/html/body/div/div/div/div[1]/div[2]/div/div[1]/form/div[1]/div/input').send_keys("jhansi4a1@gmail.com")
    element=driver.find_element(by=By.XPATH,value='/html/body/div/div/div/div[1]/div[2]/div/div[1]/form/div[2]/div/input').send_keys("Guvi@2022")
    submit_button=driver.find_element(by=By.XPATH,value='/html/body/div/div/div/div[1]/div[2]/div/div[1]/form/button').click()
##creating a function and prettify method for parse the html##  
    def zen_class(self):
      print(self.soup.prettify())
##creating a function for getting the title of the page##  
    def Name_zenclass(self):
      name=self.soup.find('title')
      return name
##getting the contents of the page##
    def contents_zenclass(self):
      contents=self.soup.find('head')
      return contents
    def session_zenclass(self):
        text=self.soup.find('div',class_="session-area")
        return text
##creating object for th class##
s=scrapping()
s.zen_class()
print(s.Name_zenclass())
print(s.contents_zenclass())
print((s.session_zenclass()))
rows=[]
rows.append(['lxml'])
##creating a csv file##
with open('zenclass.csv','w',newline='') as f:
    csv_data=csv.writer(f) 
    header=['title','tcontents','tags']
    csv_data.writerows(header)
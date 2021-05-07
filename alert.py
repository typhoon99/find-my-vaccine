from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from win32com.client import Dispatch
import time

voice = Dispatch("SAPI.SpVoice").Speak
driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.cowin.gov.in")
search=driver.find_element_by_id('mat-input-0')
search.send_keys('424001')

def find_vaccine():
    driver.find_element_by_class_name('pin-search-btn').click()
    driver.find_element_by_xpath('//label[@for="flexRadioDefault2"]').click()
    table = driver.find_element_by_class_name('center-box')
    rows=table.find_elements_by_class_name('row')
    print("Fetched at: " + time.ctime())

    for row in rows:
        hospital = row.find_element_by_class_name('center-name-title')
        #print(hospital.text)
        tags = row.find_elements_by_tag_name('a')
        for tag in tags:
            if tag.text !='Booked' and tag.text!='NA':
                # print(tag.text)
                for i in range(5):
                    voice('Vaccine Found at '+ hospital.text)
                return

while True:
        find_vaccine()
        time.sleep(5)
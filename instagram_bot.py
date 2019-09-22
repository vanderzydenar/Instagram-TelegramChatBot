import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from init import driver

#https://www.thispersondoesnotexist.com/

class InstagramBot:

    def get_latest(self):
        print('Gathering latest post from instagram...')
        time.sleep(2)
        driver.get("https://www.instagram.com/mytravelingfantasies/")
        time.sleep(2)
        # gathering posts
        pic_hrefs = []
        for i in range(1, 7):
            try:
                time.sleep(2)
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                # print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue
        print('Gathering process complete.')
        return str(pic_hrefs[0])

        driver.quit()

        #print(pic_hrefs[0])
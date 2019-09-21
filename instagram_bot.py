import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#https://www.thispersondoesnotexist.com/

def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()


class InstagramBot:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=/Users/austinvanderzyden/Library/Application Support/Google/Chrome")
        self.driver = webdriver.Chrome(chrome_options=options)

    def closeBrowser(self):
        self.driver.close()

    def like_post(self, post):
        driver = self.driver
        driver.get(post)
        time.sleep(2)
        like_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[1]/span[1]/button/span')
        like_button.click()
        time.sleep(2)

    def get_latest(self):
        driver = self.driver
        time.sleep(2)
        driver.get("https://www.instagram.com/mytravelingfantasies/")
        time.sleep(2)
        print('Gathering latest post from instagram...')
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
        print("")
        return str(pic_hrefs[0])

        driver.quit()

        #print(pic_hrefs[0])


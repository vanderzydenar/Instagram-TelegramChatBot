import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from instagram_bot import InstagramBot


class TelegramBot:

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


    def get_posts(self, engagement_limit):
        driver = self.driver
        time.sleep(2)
        driver.get('https://web.telegram.org/#/im?p=s1272466593_951385863828940473')
        time.sleep(2)

        print('Gathering posts from telegram...')

        post_list = []
        t_end = time.time() + 5
        while time.time() < t_end:
            driver.find_element_by_xpath('// *[ @ id = "ng-app"] / body / div[1] / div[2] / div / div[2] / div[3] / div / div[2] / div[1]').send_keys(Keys.PAGE_UP)
        post_list = driver.find_elements_by_xpath("//a[@href]")
        print(len(post_list))

        temp = []
        for x in range(len(post_list)):
            if '.com/p/' in post_list[x].get_attribute('href'):
                temp.append(post_list[x])
        post_list = temp


        print ('L:'+ str(len(post_list)))

        print ('Removing duplicates...')
        temp = []
        for x in range(len(post_list)):
            duplicate_found = False;
            for y in range(len(temp)):
                if temp[y].get_attribute('href') == post_list[x].get_attribute('href'):
                    duplicate_found = True
            if not duplicate_found:
                temp.append(post_list[x])
        post_list = temp

        print('Done.')
        print ('L:'+ str(len(post_list)))

        #print(post_list)
        return post_list



        print('Done.')

        print('')



    def engage_posts(self, engagement_limit, post_list):
        driver = self.driver
        print('Engaging with posts...')
        print('')
        remaining_enagegment = engagement_limit

        while remaining_enagegment > 0:
            driver.switch_to_window(driver.window_handles[0])
            print('Engagement remaining: '+str(remaining_enagegment))
            post_list[remaining_enagegment].click()
            time.sleep(2)
            driver.switch_to_window(driver.window_handles[1])
            like_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[1]/span[1]/button/span')
            like_button.click()
            driver.close()
            remaining_enagegment -= 1
            time.sleep(2)

        print('Done.')

    def post_latest(self, latest_post):
        driver = self.driver
        driver.get('https://web.telegram.org/#/im?p=s1272466593_951385863828940473')
        time.sleep(5)
        text_message_box = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/div[2]/div/div/div/form/div[2]/div[5]')
        text_message_box.clear()
        text_message_box.send_keys(latest_post)
        text_message_box.send_keys(Keys.ENTER)


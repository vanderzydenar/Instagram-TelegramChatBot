import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from init import driver


class TelegramBot:

    def get_posts(self):
        time.sleep(2)
        driver.get('https://web.telegram.org/#/im?p=@push5k24hlikes')
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
            if 'https://www.instagram.com/p/' in post_list[x].get_attribute('href'):
                temp.append(post_list[x])
        post_list = temp


        print ('L:'+ str(len(post_list)))

        '''
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
        '''

        #print(post_list)
        return post_list



        print('Done.')

        print('')

    x = 0

    def engage_posts(self, engagement_limit, post_list):
        
        print('Engaging with posts...')
        remaining_enagegment = engagement_limit

        while remaining_enagegment > 0:
            driver.switch_to_window(driver.window_handles[0])
            print('Engagement remaining: '+str(remaining_enagegment))
            print (post_list[x].get_attribute('href'))
            post_list[remaining_enagegment].click()
            driver.switch_to_window(driver.window_handles[1])
            if 'Page Not Found' not in driver.title:
                like_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[1]/span[1]/button/span')
                like_button.click()
                remaining_enagegment -= 1
            else:
                print ('Page not found.')
            x += 1
            time.sleep(2)
            driver.close()
            #time.sleep(10)

        print('Done.')


    def post_latest(self, latest_post, engagement_limit):
        driver.switch_to_window(driver.window_handles[0])
        text_message_box = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/div[2]/div/div/div/form/div[2]/div[5]')
        text_message_box.clear()
        text_message_box.send_keys('Dx'+str(engagement_limit)+' '+latest_post)
        text_message_box.send_keys(Keys.ENTER)


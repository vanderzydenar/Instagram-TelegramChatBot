import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from instagram_bot import InstagramBot
from telegram_bot import TelegramBot

engagement_limit = 30

#Turn back on nd liking photos
#Check to make sure title does not contain 'Page not found'

ig = InstagramBot()
latest_post = ig.get_latest()

tb = TelegramBot()
post_list = tb.get_posts(engagement_limit)
tb.engage_posts(engagement_limit, post_list)
tb.post_latest('yeet')

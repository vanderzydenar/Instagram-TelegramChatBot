import time
from instagram_bot import InstagramBot
from telegram_bot import TelegramBot

engagement_limit = 24

#make sure that 30 other hrefs have been added before going again



while True:
    #print ('Waiting 1 hour...')
    #time.sleep(3600)
    ig = InstagramBot()
    latest_post = ig.get_latest()

    tb = TelegramBot()
    post_list = tb.get_posts()
    tb.engage_posts(engagement_limit, post_list)
    tb.post_latest(latest_post, engagement_limit)

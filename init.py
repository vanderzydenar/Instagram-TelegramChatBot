from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=/Users/austinvanderzyden/Library/Application Support/Google/Chrome")
driver = webdriver.Chrome(chrome_options=options)

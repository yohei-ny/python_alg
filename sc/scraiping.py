from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

options =Options()
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

# driver =webdriver.Chrome(options =options)

url ="https://search.rakuten.co.jp/search/mall/anker/"
driver.get(url)

items =driver.find_elements_by_class_name("searchresultitem")
print(items)

driver.quit()
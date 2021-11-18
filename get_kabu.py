
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('C:\data\chromedriver')
url = "https://www.msn.com/ja-jp/money/stockdetails/fi-a9ihkr?ocid=ansMSNMoney11&duration=1D"

driver.get(url)
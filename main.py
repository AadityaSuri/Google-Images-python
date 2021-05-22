from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image

searchQuery = input("enter search query: ")

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome('C:\\chromedriver.exe', options=op)
driver.get('https://www.google.com/imghp?hl=EN')

searchBar = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
searchBar.send_keys(searchQuery)
searchBar.send_keys(Keys.ENTER)

driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img').screenshot(searchQuery + '.png')
img = Image.open(searchQuery + '.png')
img.show()
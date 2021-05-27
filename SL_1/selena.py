from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome("C:/Users/ENG-DESKTOP-4/Documents/Python/chromedriver.exe")

driver.get("https://zerodha.com/margin-calculator/SPAN")

#select  exchange   option of NFO
exchange = driver.find_element_by_name('exchange[]')
exchange.send_keys("NFO")

#  select product option of option
product = driver.find_element_by_name('product[]')
product.send_keys("FUT")

# select symbol  by option value
symbol = Select(driver.find_element_by_name("scrip[]"))
symbol.select_by_value("AARTIIND21JUN")

# select  option Type  CALL option
#optionType = driver.find_element_by_name('option_type[]')
#optionType.send_keys("CE")

#add Strike price
#strikePrice = driver.find_element_by_name('strike_price[]')
#strikePrice.clear()
#strikePrice.send_keys("120")

# add Net quantity
netQty = driver.find_element_by_name('qty[]')
netQty.clear()
netQty.send_keys("425")

# select sell radio button
driver.find_elements_by_css_selector("input[name='trade[]'][value='sell']")[0].click()

#submit form
submit = driver.find_element_by_css_selector("input[type='submit'][value='Add']")
submit.click()

time.sleep(2)

# scrape margin
margin = driver.find_element_by_css_selector(".val.total")
print(margin.text) 
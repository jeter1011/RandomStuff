#pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome("C:/Users/ENG-DESKTOP-4/Documents/Python/chromedriver.exe")

driver.get("https://www.opticutter.com/linear-cut-list-calculator")

#select available stock
stock_length = driver.find_element_by_name('stocks[0].length')
stock_length.send_keys("330")

#  select Kerf option of option
kerf = driver.find_element_by_name('settings.kerf')
kerf.send_keys("1")

# select required parts
required_length = driver.find_element_by_name("requirements[0].length")
required_length.send_keys("66")

# select required parts
required_parts = driver.find_element_by_name("requirements[0].count")
required_parts.send_keys("120")

# # select  option Type  CALL option
# #optionType = driver.find_element_by_name('option_type[]')
# #optionType.send_keys("CE")

# #add Strike price
# #strikePrice = driver.find_element_by_name('strike_price[]')
# #strikePrice.clear()
# #strikePrice.send_keys("120")

# # add Net quantity
# netQty = driver.find_element_by_name('qty[]')
# netQty.clear()
# netQty.send_keys("425")

# # select sell radio button
# driver.find_elements_by_css_selector("input[name='trade[]'][value='sell']")[0].click()

#submit form
submit = driver.find_element_by_css_selector("button[type='submit'][title='solve']")
submit.click()

time.sleep(5)

# scrape margin
margin = driver.find_element_by_css_selector(".table.table border-bottom product-item-table")
print(margin.text) 
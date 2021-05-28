#pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome("C:/Users/erick/OneDrive/Documents/VSPython/chromedriver.exe")

driver.get("https://www.opticutter.com/linear-cut-list-calculator")

#select available stock
stock_length = driver.find_element_by_name('stocks[0].length')
stock_length.send_keys("330")

#submit form
add_len = driver.find_element_by_css_selector("button[type='button'][class='btn btn-sm btn-outline-primary mb-2']")
add_len.click()

add_len2 = driver.find_element_by_css_selector("button[type='button'][class='btn btn-sm btn-outline-primary mb-2']")
add_len2.click()

stock_length = driver.find_element_by_name('stocks[1].length')
stock_length.send_keys("350")

stock_length = driver.find_element_by_name('stocks[2].length')
stock_length.send_keys("430")

#  select Kerf option of option
kerf = driver.find_element_by_name('settings.kerf')
kerf.send_keys("1")

# select required parts
required_length = driver.find_element_by_name("requirements[0].length")
required_length.send_keys("66")

# select required parts
required_parts = driver.find_element_by_name("requirements[0].count")
required_parts.send_keys("120")

#required parts add button
driver.find_element_by_xpath("//button[@onclick=\"javascript:addRequirementsRow(1, 'Delete')\"]").click()
driver.find_element_by_xpath("//button[@onclick=\"javascript:addRequirementsRow(1, 'Delete')\"]").click()

# select required parts
required_length2 = driver.find_element_by_name("requirements[1].length")
required_length2.send_keys("72")

# select required parts
required_parts2 = driver.find_element_by_name("requirements[1].count")
required_parts2.send_keys("90")

# select required parts
required_length3 = driver.find_element_by_name("requirements[2].length")
required_length3.send_keys("92")

# select required parts
required_parts3 = driver.find_element_by_name("requirements[2].count")
required_parts3.send_keys("60")

#add_len3 = driver.find_element_by_css_selector("button[type='button'][class='btn btn-sm btn-outline-primary mb-2'][tabindex='-1'][onclick='javascript:addRequirementsRow(1, 'Delete')']")
#add_len3.click()

#add_len3 = driver.find_element_by_css_selector("button[type='button'][class='btn btn-sm btn-outline-primary dropdown-toggle mb-2']")
#add_len3.click()

# add_len4 = driver.find_element_by_css_selector("button[type='button'][class='btn btn-sm btn-outline-primary mb-2']")
# add_len4.click()


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
margin = driver.find_element_by_xpath("//*[@id='navs-bottom-responsive-link-1']/div[1]/div[2]/div/table/tbody/tr[5]/td[2]")
print(margin.text) 

from selenium import webdriver

chrome_driver_path = (r"C:\Users\Samuel Osondu\Desktop\DEVELOPMENT\chromedriver.exe")
driver = webdriver.Chrome (executable_path = chrome_driver_path)
driver.get("https://www.konga.com/product/apple-iphone-12-pro-max-5g-128gb-rom-6gb-ram-ios-14-1-6-7-graphite-5090356")
price = driver.find_element_by_class("_678e4_e6nqh")
print (price)

driver.quit()

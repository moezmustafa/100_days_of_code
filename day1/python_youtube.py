from selenium import webdriver

from webdriver_manager.firefox import GeckoDriverManager

#for firefox
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


driver.get('https://www.youtube.com')

search = driver.find_element_by_xpath('//*[@id="search"]')

search.send_keys('Blinding Lights')

search_button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')

search_button.click()
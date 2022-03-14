# from selenium import webdriver
#
# driverClass = 'C://Users//diego//Documents//Ferramentas//chromedriver.exe'
# navegador = webdriver.Chrome(driverClass)
# navegador.get('https://diegossena.com.br/')
# screenshot = navegador.save_screenshot('my_screenshot.png')
# navegador.quit()

# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome('C://Users//diego//Documents//Ferramentas//chromedriver.exe')  # Optional argument, if not specified will search path.
# driver.get('https://diegossena.com.br/')
# time.sleep(5)  # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(500)  # Let the user actually see something!
# driver.quit()

# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Chrome('C://Users//diego//Documents//Ferramentas//chromedriver.exe')
# driver.get('https://www.python.org')
# sleep(10)
#
# driver.save_screenshot("screenshot-py.png")
# driver.quit()
# print("end...")

from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ser = Service('C://Users//diego//Documents//Ferramentas//chromedriver.exe')
op = webdriver.ChromeOptions()
s = webdriver.Chrome(service=ser, options=op)

url = "https://diegossena.com.br/"
s.get(url)
s.save_screenshot('C://Users//diego//Desktop//TestesPython//dsena7.png')
# screenshot = Image.open('dsena7.png')
s.quit()

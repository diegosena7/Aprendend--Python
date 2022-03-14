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

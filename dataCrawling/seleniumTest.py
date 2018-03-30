from selenium import webdriver
import time
wd = webdriver.Chrome(r'C:\Python36\WebDriver\chromedriver.exe')

wd.get('https://www.google.com')
print('창이 로딩되었다')

time.sleep(5)
print('창이 닫혔다')

wd.quit()
print('브라우저 종료')
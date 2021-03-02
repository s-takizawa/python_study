import requests
import bs4
import time
from selenium import webdriver
import chromedriver_binary

# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# try:
#     res.raise_for_status()
# except Exception as exc:
#     print('There was a problem: %s' % (exc))

# print(type(res))
# if res.status_code == requests.codes.ok:
#     print(len(res.text))
#     print(res.text[:250])

# requests
res = requests.get('https://nostarch.com')
res.raise_for_status()
sp = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(sp))
elem = sp.select('p')

for el in elem:
    print(el.getText())

# selenium chrome
driver = webdriver.Chrome()
print(type(driver))
driver.get('https://inventwithpython.com')
time.sleep(10)

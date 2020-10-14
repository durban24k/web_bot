from selenium import webdriver
from config import keys
import time

def timeme(method):
     def wrapper(*args,**kw):
          startTime=int(round(time.time()*1000))
          result=method(*args,**kw)
          endTime=int(round(time.time()*1000))
          print("Execution time:{}se".format((endTime-startTime)/1000))
          return result
     return wrapper

@timeme

def login(x):
     driver.get(x['url'])
     driver.find_element_by_xpath('//*[@id="userName"]').send_keys(x["email"])
     driver.find_element_by_xpath('//*[@id="password"]').send_keys(x["password"])
     driver.find_element_by_xpath('//*[@id="btnLogin"]').click()

if __name__ == '__main__':
     driver=webdriver.Chrome('./chromedriver')
     login(keys)
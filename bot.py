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

def search(x):
     driver.get(x['producturl'])
     driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(x["name"])
     driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').click()

if __name__ == '__main__':
     driver=webdriver.Chrome('./chromedriver')
     search(keys)
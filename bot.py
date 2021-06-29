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
     driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div/div[2]/button').click()
     time.sleep(10)
     driver.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div[1]/form/div[3]/ul/li[1]/input').send_keys(x["email"])
     time.sleep(10)
     driver.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div[1]/form/div[3]/ul/li[2]/input').send_keys(x["password"])
     driver.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div[1]/form/div[3]/ul/li[3]/input').click()

if __name__ == '__main__':
     driver=webdriver.Chrome('./chromedriver.exe')
     login(keys)
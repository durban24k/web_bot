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
     driver.find_element_by_xpath('//*[@id="id_esauth_myaccount_login_link"]').click()
     driver.find_element_by_xpath('//*[@id="id_esauth_login_field"]').send_keys(x["email"])
     driver.find_element_by_xpath('//*[@id="id_esauth_pwd_field"]').send_keys(x["password"])
     driver.find_element_by_xpath('//*[@id="stay_signed_in"]').click()
     driver.find_element_by_xpath('//*[@id="id_esauth_login_button"]').click()
     time.sleep(4)
     driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/div[2]/table/tbody/tr[12]/td[2]/a').click()

if __name__ == '__main__':
     driver=webdriver.Chrome('./chromedriver')
     login(keys)
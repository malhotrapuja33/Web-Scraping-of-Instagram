#innnstagram  scrappinng
from selenium import webdriver
#from config import USERNAME,PASSWORD
import time

username='Id of user'
password=''
users=['a','b','c']#name of user u want to extract data
driver=webdriver.Chrome(r"C:\Program Files\chromedriver\chromedriver")

driver.get("https://www.instagram.com/")
time.sleep(5)
username_field=driver.find_element_by_name("username")
username_field.send_keys(username)
time.sleep(5)
password_field=driver.find_element_by_name("password")
password_field.send_keys(password)
time.sleep(5)
btn=driver.find_element_by_css_selector('button[ type="submit"]')
btn.click()
time.sleep(5)
for user in users:
    driver.get(f"https://www.instagram.com/{user}/")
    bio=driver.find_element_by_class_name('QGPIr')
    print(bio.text)
    posts,followers,following=driver.find_elements_by_class_name('g47SY')#g47SY lOXF2
    print("post",posts.text,"followers",followers.text,"following",following.text)
    time.sleep(10)
    
    
##QGPIr    


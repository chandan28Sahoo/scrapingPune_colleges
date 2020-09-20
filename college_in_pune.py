from selenium import webdriver
import time


driver=webdriver.Chrome(r"C:\Users\CHANDAN SAHU\Desktop\chromedriver")
driver.get('https://www.collegedekho.com/colleges-in-pune/')
time.sleep(5)

count=0
while True:
    count+=1
    if count==20:
        break
    else:
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="loadMoreButton"]').click()
        time.sleep(5)
        print(count)

html = driver.execute_script('return document.documentElement.outerHTML')


f=open("pune.html","w+")
lines = f.write(html)

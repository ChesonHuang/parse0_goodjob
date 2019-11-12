#!/usr/bin/python
#-*-coding:utf-8-*-
from selenium import webdriver
import os
import sys
import time

def exit_root():
    user = os.popen('whoami').read()
    if user.strip()=='root':
       print 'hhhhhhhhhh'
       sys.exit('current user is root, not allow, exit!')

def driver(platform,log_path='/tmp/geckodriver.log'):
    print platform.lower()
    if platform.lower()=='ie':
    	driver = webdriver.Ie(log_path=log_path)
    elif platform.lower()=='chrome':
        driver = webdriver.Chrome(log_path=log_path)
    elif platform.lower() =='firefox':
        driver = webdriver.Firefox(log_path=log_path)
    else:
	raise Exception('Unsupport browser',platform)
    driver.implicitly_wait(10)
    return driver

def exit(driver):
    driver.quit()   

 

if __name__=='__main__':
    #dr =webdriver.Firefox(log_path='/tmp/geckodriver.log')
    #dr.implicity_wait(10)
    #dr.get('https://www.baidu.com')
    exit_root()
    time.sleep(2)
    dr = driver('firefox')
    dr.get('https://www.baidu.com')
    exit(dr)

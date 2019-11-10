#!/usr/bin/python
#-*-coding:utf-8-*-
from selenium import webdriver


def driver(platform,**kwargs):
    if platform.lower=='ie':
    	driver = webdriver.Ie(kwargs)
    elif platfor

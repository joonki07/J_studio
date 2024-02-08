from selenium import webdriver
import pyautogui as py
import time

driver = webdriver.Chrome()
driver.get("http://www.naver.com")
# driver.set_window_position(0, 0)
# driver.set_window_size(1920, 1080)
driver.maximize_window()
py.moveTo(1365,468)
py.click()
time.sleep(0.3)
py.write("joonki2007", interval = 0.1)
py.press('tap')

#%% 마우스 위치 잡기

import pyautogui as py

py.mouseInfo()
# 로그인 버튼 1365,468
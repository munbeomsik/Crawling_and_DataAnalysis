# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
from selenium import webdriver


options = webdriver.ChromeOptions()
# options.add_argument('headless') # headless 모드 사용하지 않을 경우 주석처리
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
driver = webdriver.Chrome('chromedriver', options=options)
driver.implicitly_wait(5)

print("Login Start")
driver.get('https://nid.naver.com/nidlogin.login')
tag_id = driver.find_element_by_name('id')
tag_pw = driver.find_element_by_name('pw')
tag_id.clear()
driver.implicitly_wait(1)

driver.execute_script("document.getElementsByName('id')[0].value='아이디'")
driver.implicitly_wait(1)

driver.execute_script("document.getElementsByName('pw')[0].value='비밀번호'")
driver.implicitly_wait(1)

# 로그인 버튼 클릭
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
driver.implicitly_wait(1)
print("Login Completion")


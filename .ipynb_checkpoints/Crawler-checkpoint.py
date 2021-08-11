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

# 카페 글 링크 가져오기
def crawling_new_url(cafe_url):
    print("URL Crawling Start")
    article_url = []
    append = article_url.append
    for url in cafe_url:
        print(url)
        driver.get(url)
        driver.implicitly_wait(3)
        driver.switch_to.frame("cafe_main")
        while 1:
            check = 1
            page_bar = driver.find_elements_by_css_selector('.prev-next > a')
            page = []
            for e in page_bar:
                if e.text != '이전':
                    page.append(e.text)

            print("page: ", page)
            for i in page:
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                article_list = soup.find_all('div', class_='article-board m-tcol-c')[1].find_all('a', class_='article')

                for j in range(len(article_list)):
                    element = article_list[j].get('href')
                    append('https://cafe.naver.com' + element)

                try:
                    # 다음 페이지로
                    if check == len(page):
                        check = 'stop'
                        break
                    elif (int(i) % 10) == 0:
                        driver.find_element_by_link_text('다음').click()
                        driver.implicitly_wait(3)
                    else:
                        driver.find_element_by_link_text(str(int(i) + 1)).click()
                        check += 1
                        driver.implicitly_wait(3)
                except Exception as error:  # 로딩 실패시 재시도
                    print(error)
                    pass
            if check == 'stop':
                break
        print('--> ', len(article_url), article_url)
    print("URL Crawling Completion")
    return article_url


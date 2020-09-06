from urllib.parse import quote_plus    # 한글 텍스트를 퍼센트 인코딩으로 변환
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 해당 태그를 기다림
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException    # 태그가 없는 예외 처리
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import random


def crawling_goobne(url, main_category, middle_category ):
    # \U는 유니코드로 인식되기 때문에 \\U와 같이 escape 처리했다.
    wd = webdriver.Chrome('C:\\Users\\hwang in beom\\Desktop\\chromedriver.exe')
    wd.get(url)

    RESULT_DIRECTORY = '../'
    results = []
    list_name = []

    # for i in range(1, int(last[0])+1):
        # script = 'movePage(%d)' % i
        # wd.execute_script(script)  # js 실행
        # time.sleep(1.5 + random.uniform(0.01, 0.1))              # 크롤링 로직을 수행하기 위해 5초정도 쉬어준다.

    html = wd.page_source
    bs = BeautifulSoup(html, 'html.parser')

    tags = bs.findAll('span', attrs={'class': 'inform pr10'})
    print(tags)
    for tag in tags:
        list_name.append(tag.get_text())
        # break


    table = pd.DataFrame(list_name)
    print(table)
    table.to_csv('{}-{}.csv'.format(main_category, middle_category), encoding='euc-kr', mode='w', errors=None,)
    # table.to_csv('가공식품-간편,즉석요리.csv', encoding='euc-kr', mode='w')



## HTTP GET Request 시작 url
url_str ='http://www.nsmall.com/CategoryDisplay?cate1Code=1583596&cate2Code=1583572&storeId=13001&langId=-9&catalogId=97001&selfId=1583635&menuUri=NSSubCategoryPageLayoutView&categoryId=1583635'
req = requests.get(url_str)
## HTML 소스 가져오기
html = req.text
# print(html)
bs = BeautifulSoup(html, 'html.parser')
# print(bs)
url_list = bs.find('li', attrs={'class': 'cate_List third'}).find('ul', attrs={'class': 'depth1'}).find_all("li")

for i in range(0,len(url_list)):
    start = (str(url_list[i]).find('href=')) + 6
    end = str(url_list[i]).find('"><span>')
    url_list[i] = ("http://www.nsmall.com/" + str(url_list[i])[start:end]).replace('amp;', '')
count = 0
for i in url_list:
    if count == 1:
        count += 1
        break
    count += 1
    url_str = 'http://www.nsmall.com/CategoryDisplay?cate1Code=1583596&cate2Code=1583572&storeId=13001&langId=-9&catalogId=97001&selfId=1583635&menuUri=NSSubCategoryPageLayoutView&categoryId=1583635'
    req = requests.get(url_str)
    ## HTML 소스 가져오기
    html = req.text
    # print(html)
    bs = BeautifulSoup(html, 'html.parser')
    pagging = bs.find('div', attrs={'class': 'lst_paging'})
    last = re.findall("\d+", str(pagging.find('a', attrs={'class': 'last'})))
    main_category = bs.find('li', attrs={'class': 'cate_List second'}).find('a', attrs={'href': '#;'}).get_text()
    middle_category = bs.find('li', attrs={'class': 'cate_List third'}).find('a', attrs={'href': '#;'}).get_text()
    main_category = main_category.replace('/', ',')
    middle_category = middle_category.replace('/', ',')
    crawling_goobne(url_str, main_category, middle_category)

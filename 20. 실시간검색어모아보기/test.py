from webdriver_manager.chrome import ChromeDriverManager
# conda install webdriver_manager
# conda install -c conda-forge webdriver-manager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from bs4 import BeautifulSoup
# pandas
import pandas as pd
import numpy as np

# crawling
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time

# word tokenize
# from konlpy.tag import Okt
from collections import Counter

# visualize and wordcloud
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
# from wordcloud import WordCloud

def scrap():
    font_path = "C:/Windows/fonts/Hancom Gothic Bold.ttf"
    font_name = font_manager.FontProperties(fname=font_path).get_name()

    plt.rc('font', family=font_name)

    pd.set_option("display.max_rows", 500)

    wd = webdriver.Chrome()

    # 네이버 영화
    url = "https://movie.naver.com/movie/point/af/list.naver?&page="

    title = []
    rank = []
    report = []

    N = 2

    for i in range(1, N + 1):
        wd.get(url + "%d" % (N + 1 - i))  # 댓글이 업데이트 될 수도 있기에 중복을 막고자 역순으로 진행
        html = wd.page_source
        soup = bs(html, 'html.parser')

        # 영화 제목
        tags = soup.select('tbody a.movie')
        for tag in tags:
            title.append(tag.get_text())

        # 영화 평점
        tags = soup.select('tbody div.list_netizen_score em')
        for tag in tags:
            rank.append(tag.get_text())

        # 영화 리뷰
        tags = soup.select('tbody a.report')
        for tag in tags:
            report.append(tag['onclick'].split("', '")[2])

        time.sleep(1)

        movie = pd.DataFrame({'title': title, 'rank': rank, 'report': report})

        movie['rank'] = movie['rank'].astype(int)

        movie.info()

        print(movie)


def main():
    url = "http://www.naver.com"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    time.sleep(5)

if __name__ == '__main__':

    scrap()
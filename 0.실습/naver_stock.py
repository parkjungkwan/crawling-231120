import pandas as pd
import requests
from bs4 import BeautifulSoup

class NaverStock:
    def __init__(self):
        self.code = pd.DataFrame({'name':[], 'code':[]})
        self.url = ''

    def krx_crawl(self):
        c = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]
        # print(c)
        c['종목코드'] = c['종목코드'].map('{:06d}'.format) # 005930 이 5930 으로 출력되는 것을 막는다
        k = c[['회사명','종목코드']]
        # print(k)
        self.code = k.rename(columns={'회사명': 'name', '종목코드': 'code'})
        print(self.code)


    def get_url(self, item_name):
        #c = self.code.query("name='{}'".format(item_name))['code'].to_string(index=False)
        c = f'https://finance.naver.com/item/sise_day.naver?code=005930&page=1'
        self.url = c
        return c


    def naver_crawl(self):
        headers = {'User-Agent': 'Mozilla/5.0'} # 헤더를 요구하는 사이트에 추가해 준다.
        req = requests.get(self.url, headers=headers)
        html = BeautifulSoup(req.text, 'lxml')
        pgrr = html.find('td', class_='pgRR')
        print(f" a태그 href 값 : {pgrr.a['href']}")
        s = pgrr.a['href'].split('=')
        last_page = s[-1]
        temp_page = 10

        df = None

        for i in range(1, int(temp_page)+1):
            req = requests.get(f'{self.url}&page={i}', headers=headers)
            df = pd.concat([df, pd.read_html(req.text, encoding='euc-kr')[0]])

        df.dropna(inplace=True)
        df.reset_index(drop=True, inplace=True)
        df.to_excel('./data/samsung_price.xlsx')



if __name__ == '__main__':

    n = NaverStock()

    while 1:
        menu = input('0-종료 1-kind 에서 종목코드 얻기 2-url 얻기 3-시세와 종가 엑셀로 저장')
        if menu == '0':
            print('프로그램 종료')
            break
        elif menu == '1':
            n.krx_crawl()

        elif menu == '2':
            item = input('검색하는 종목명을 입력')
            a = n.get_url(item)
            print(f'획득한 url {a}')

        elif menu == '3':
            n.naver_crawl()

        else:
            print('잘못된 값')
            continue


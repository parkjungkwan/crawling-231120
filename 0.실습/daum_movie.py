import requests
import requests as req
import json
import pandas as pd
from bs4 import BeautifulSoup as bs

class DaumMovie:
    def __init__(self):
        self.url = ''
        self.count = None # 크롤링결과 : {'count': 287, 'sum': 1118, 'id': 149761585}
        self.review_count = 0
        self.review_list = []

    def set_url(self, url):
        self.url = url

    def set_count(self):
        res = req.get(self.url)
        movie_code = '149761585'
        count_url = f"https://comment.daum.net/apis/v1/comments/on/{movie_code}/flags"
        count_res = req.get(count_url)
        self.count = json.loads(count_res.text)
        return self.count # 로직상 필요는 없지만  main 에서 print 하기 위해 리턴함

    def extract_count(self):
        self.review_count = self.count['count'] # {'count': 287, 'sum': 1118, 'id': 149761585}
        return self.review_count

    def set_review_list(self):
        for i in range(0, 1): # self.review_count 가 맞는데, 시간 관계상 2 회전으로 줄여서 구함
            res = requests.get(self.url)
            ls = json.loads(res.text)
            print(f' i 값 : {ls}')
            '''
            [{"rating": "1", "content": "3.72UBD 예상보다 많은 분들이 보셨네요.", "user": {"displayName": "The Force"}}]
            를 pretty json 사이트에서 돌리면, 다음과 같이 정리 되어 보여준다.불필요한 데이터는 제거함.
            [
              {
                "rating": "1",
                "content": "3.72UBD 예상보다 많은 분들이 보셨네요.",
                "user": {
                  "displayName": "The Force"
                }
              }
            ]
            '''
            for i, _ in enumerate(ls):
                review = ls[i]['content'] # pretty json 사이트에서 키값을추출함
                user = ls[i]['user']['displayName']
                rating = ls[i]['rating']
                self.review_list.append([user, rating, review])
            df = pd.DataFrame(self.review_list, columns=['user', 'rating','review'])
            df.to_excel('./data/daum_review.xlsx')



if __name__ == '__main__':
    d = DaumMovie()
    while 1:
        menu = input('0-종료 1-url등록 2-리뷰갯수 3-리뷰목록 ')
        if menu == '0' :
            print('프로그램 종료')
            break

        elif menu == '1':
            # url = input('수집하려는 url 입력') 원래는 수동으로 입력해야 하는데, 편의상 자동입력으로 대체
            url2 = 'https://comment.daum.net/apis/v1/posts/149761585/comments?parentId=0&offset=0&limit=10&sort=LATEST&isInitial=true&hasNext=true'
            d.set_url(url2)

        elif menu == '2':
            d.set_count()
            c = d.extract_count()
            print(f'리뷰의 총갯수 : {c}')

        elif menu == '3':
            d.set_review_list()

        else:
            print('잘못된 번호')
            continue


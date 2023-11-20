class MelonMusic:
    def __init__(self):
        url = 'https://www.melon.com/chart/index.htm?dayTime='
        headers = {'User-Agent': 'Mozilla/5.0'}
        class_name = []

    def set_url(self, url):
        self.url = f'{self.domain}/{url}'

    def get_url(self):
        return self.url


if __name__ == '__main__':
    m = MelonMusic()
    url = input('멜론에서 크롤링할 url 을 입력하세요.')
    m.set_url(url)
    u2 = m.get_url()
    print(f'당신이 원하는 대상은 {u2} 입니다.')
import qrcode

class QrMaker:
    def __init__(self):
        self.domain = ''

    def set_domain(self, domain):
        self.domain = domain

    def save_qr(self, title):
        qr_data = self.domain
        qr_img = qrcode.make(qr_data)

        save_path = f'./{title}.png'
        qr_img.save(save_path)

    def save_multi_qr(self, fname):
        with open(fname, 'rt', encoding='UTF8') as f:
            read_lines = f.readlines()

            for line in read_lines:
                line = line.strip()
                print(line)

                qr_data = line
                qr_img = qrcode.make(qr_data)

                save_path = f'./qrcode/' + qr_data + '.png'
                qr_img.save(save_path)

if __name__ == '__main__':
    q = QrMaker()
    while 1 :
        menu = input('0.종료 1:QR 1개생성 2:QR 여러개생성')
        if menu == '0':
            print('프로그램 종료')
            break
        elif menu == '1':
            domain = input('도메인 입력 :')
            # www.google.com
            q.set_domain(domain)
            title = input('파일명 입력 :')
            q.save_qr(title)
        elif menu == '2':
            fname = input('파일명 입력 :')
            # qr코드모음.txt
            q.save_multi_qr(fname)
        else:
            print('메뉴에 없는 번호입니다.')
            continue





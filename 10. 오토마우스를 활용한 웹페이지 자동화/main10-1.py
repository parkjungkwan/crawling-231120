import pyautogui
# pip install PyAutoGUI
# conda install -c conda-forge pyautogui
import time
import pyperclip

class Weather:
    def __init__(self):
        self.region = ''

    def set_region(self, region):
        self.region = region

    def _(self):
        while True:
            print(pyautogui.position())
            time.sleep(0.1)

    def naver_weather(self):
        pyautogui.moveTo(1241, 206, 0.2)
        pyautogui.click()
        time.sleep(0.5)

        pyperclip.copy(f"{self.region} 날씨")
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.5)

        pyautogui.write(["enter"])
        time.sleep(1)

        start_x = 992
        start_y = 220
        end_x = 1656
        end_y = 635
        pyautogui.screenshot(f'./{self.region} 날씨.png', region=(start_x, start_y, end_x - start_x, end_y - start_y))


if __name__ == '__main__':
    w = Weather()
    while 1:
        menu = input('0-종료 1-지역 입력 2-네이버날씨')
        if menu == '0':
            print('프로그램 종료')
            break
        elif menu == '1':
            region = input('지역이름')
            w.set_region(region)
        elif menu == '2':
            w.naver_weather()
        else:
            print('잘못된 번호')
            continue


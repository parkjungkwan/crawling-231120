import pandas as pd

class Certificate:
    def __init__(self):
        self.student_list = []

    def set_student_list(self, student):
        self.student_list.append(student)


    def save_to_excel(self):
        d = pd.DataFrame(self.student_list)

        df2 = pd.DataFrame([["홍길동", "1990.01.02", "2021-0001"],
                            ["김민준", "1990.05.06", "2021-0002"],
                            ["김철수", "2000.08.08", "2021-0003"],
                            ["김영희", "2000.09.09", "2021-0004"],
                            ["이서준", "2010.10.10", "2021-0005"],
                            ["장다인", "2017.12.12", "2021-0006"]])
        d.to_excel(r'./certificate/수료증명단.xlsx', index=False, header=False)

if __name__ == '__main__':
    c = Certificate()
    while 1:
        menu = input('0-종료 1-학생정보입력 2-엑셀저장')
        if menu == '0':
            print('프로그램 종료')
            break
        elif menu == '1':
            count = input('수료하는 인원 :')
            for i in range(int(count)):
                stu = []
                name = input('이름 : ')
                birth = input('생년월일 : ')
                c_number = input('수료증번호: ')
                stu.append(name)
                stu.append(birth)
                stu.append(c_number)
                c.set_student_list(stu)
        elif menu == '2':
            c.save_to_excel()
        else:
            print('잘못된 번호')
            continue




import pandas as pd

class Certificate:
    def __init__(self):
        self.student = []

    def set_student(self, name, birth, c_number):
        self.student = [name, birth, c_number]

    def get_student(self):
        return self.student


    def save_to_excel(self):
        df = pd.DataFrame([self.student])

        df2 = pd.DataFrame([["홍길동", "1990.01.02", "2021-0001"],
                            ["김민준", "1990.05.06", "2021-0002"],
                            ["김철수", "2000.08.08", "2021-0003"],
                            ["김영희", "2000.09.09", "2021-0004"],
                            ["이서준", "2010.10.10", "2021-0005"],
                            ["장다인", "2017.12.12", "2021-0006"]])

        print(df)
        df.to_excel(r'./certificate/수료증명단.xlsx', index=False, header=False)

if __name__ == '__main__':
    c = Certificate()
    ls = []
    for i in range(2):
        name = input('이름 : ')
        birth = input('생년월일 : ')
        c_number = input('수료증번호: ')
        c.set_student(name,birth,c_number)
        stu = c.get_student()
        ls.append(stu)
    for i in ls:
        print(i)

    df = pd.DataFrame(ls)
    df.to_excel(r'./certificate/테스트.xlsx', index=False, header=False)
    # c.save_to_excel()

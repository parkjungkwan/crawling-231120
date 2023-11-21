import googletrans 
# pip install googletrans==4.0.0-rc1

class Translator:
    def __init__(self):
        self.translator = googletrans.Translator()
        self.text = ''

    def set_text(self, text):
        self.text = text

    def en_to_kr(self):

        result2 = self.translator.translate(self.text, dest='ko', src='en')
        return result2
        print(f"I am happy => {result2.text}")

    def ko_to_en(self):
        result1 = self.translator.translate(self.text, dest='en', src='auto')
        return result1
        print(f"행복하세요 => {result1.text}")

if __name__ == '__main__':








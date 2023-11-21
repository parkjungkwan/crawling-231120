from gtts import gTTS
from playsound import playsound
# pip install playsound==1.2.2
class TextToSpeech:

    def __init__(self):
        self.text = ''

    def set_text(self, text):
        self.text = text


    def save_mp3(self, title):
        tts = gTTS(text=self.text, lang='ko')
        tts.save(f"./{title}.mp3")

if __name__ == '__main__':

    t = TextToSpeech()
    title = input('제목을 입력하시오')
    text = input('변환하려는 문장을 입력하시오.')
    t.set_text(text)
    t.save_mp3(title)

    playsound("./hi.mp3")

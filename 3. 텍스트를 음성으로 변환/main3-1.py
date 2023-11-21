from gtts import gTTS

class TextToSpeech:

    def __init__(self):
        self.text = ''

    def set_text(self, text):
        self.text = text


    def save_text(self):
        tts = gTTS(text=self.text, lang='ko')
        tts.save(r"./text.mp3")

if __name__ == '__main__':
    pass

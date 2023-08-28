from gtts import gTTS

text = "여기는 부소마고  "
tts=gTTS(text=text, lang='ko')
tts.save(r"C:\\Users\\user\\Desktop\\ttstest\\hi.mp3")

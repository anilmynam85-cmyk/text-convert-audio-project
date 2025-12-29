from gtts import gTTS
from playsound import playsound
audio="speech.mp3"
langvage="en"
sp=gTTS(text="Hello python  ",lang=langvage,slow=False)
sp.save(audio)
playsound(audio)
print("=======audio is playing=====")

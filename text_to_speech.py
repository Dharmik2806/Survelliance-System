from gtts import gTTS
import os

mytext="hello"

language='en'
output=gTTS(text=mytext, lang=language, slow=False)

output.save("output.mp3")

os.system("start output.mp3")
#!/usr/bin/env python3

from qutescript import userscript
from gtts import gTTS
import os

@userscript
def tts(request):
    request.send_command('search '+request.selected_text)
    myobj = gTTS(text=request.selected_text, lang='en', slow=False)
    myobj.save("tts.mp3")
    os.system("mpg321 tts.mp3")

if __name__ == '__main__':
    tts()

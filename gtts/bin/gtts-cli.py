#! /usr/bin/python

from gtts import gTTS
from gtts import __version__
import argparse

try:
    # TTSTF (Text to Speech to File)
    tts = gTTS(text="Eu vou tacar o peru na chuva para ela ir embora")
    tts.save("hello.mp3")
except Exception as e:
    print(str(e))

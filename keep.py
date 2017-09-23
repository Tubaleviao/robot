import speech_recognition as sr
import os

def show(resp):
	print(resp)
	os.system("espeak \""+resp+"\"")

r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.energy_threshold = 90000
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("...")
        audio = r.listen(source)
        print("Wait...")
        try:
            show(r.recognize(audio))
        except LookupError:
            print("Do again")
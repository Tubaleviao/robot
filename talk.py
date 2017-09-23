import speech_recognition as sr
import os
from gtts import gTTS
import win32api, win32con

def click(x,y):
	try:
		win32api.SetCursorPos((x,y))
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y)
	except Exception as e:
		print(str(e))

def search(words):
	if (words == "click"): 
		x, y = win32api.GetCursorPos()
		click(x,y)
	elif(words[0:5] == "click"):
		x = -1
		for i in range(7, len(words)):
			if (words[i].isspace()): # find the white space
				if(x < 0):
					x = int(words[6:i])
			elif(i == len(words)-1):
				y = int(words[len(str(x))+8:i+1])
				print(str(x)+" "+str(y))
				click(x,y)
	else: 
		repeat(words, False) # Google = True; Robot = False

def repeat(resp, google):
	print(resp)
	if (google):
		try:
			tts = gTTS(text=resp)
			tts.save("lastwords.mp3")
			os.system("D:/robot/mpg123/mpg123.exe lastwords.mp3")
		except Exception as e:
			print(str(e))
	else:
		os.system("espeak \""+resp+"\"")
	
r = sr.Recognizer()
m = sr.Microphone()
with m as source:
	r.energy_threshold = 400
	print("Set minimum energy threshold to {}".format(r.energy_threshold))
	while True:
		print("...")
		audio = r.listen(source)
		print("Wait...")
		try:
			search(r.recognize(audio))
		except IndexError:
			print("No internet connection")
		except LookupError:
			print("Do again")
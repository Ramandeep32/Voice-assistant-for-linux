import speech_recognition as serial 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence
import pyaudio
import webbrowser
import wolframalpha
import json
import operator
import datetime
import wikipedia
from twilio.rest import Client
from clint.textui import progress


def wishing():
	time = int(datetime.datetime.now().hour)
	if time>= 0 and time<12:
		print("Good Morning Sir/Ma'am !")

	elif time>= 12 and time<18:
		print("Good Afternoon Sir/Ma'am !")

	else:
		print("Good Evening Sir/Ma'am !")

	print("I am your Assistant: DoDo\n")   
	
def Instructions():
    print("--------------below instructions can be performed by me------------------")
    print("--> open file in current directory")    
    print("--> see current directory")    
    print("--> make directory")  
    print("--> remove directory")    
    print("--> create file")
    print("--> delete file")    
    print("--> Arithmatic Operation")    
    print("--> Show Calendar")    
    print("--> Today's date")    
    print("--> Search any topic on wikipedia")    
    print("--> Can show weather default(Current City)")    
    print("--> Can show weather of any city using location name") 
    print("--> Can show weather of any city using pincode of locaton") 
    print("--> Can play music")    
    print("--> Can open any site\n")    
    print("--------------------------------------------------------------------------")   

if __name__ == '__main__':
    rec = serial.Recognizer()
    pa = pyaudio.PyAudio()
    pa.get_default_input_device_info()
    wishing()
    Instructions()
    with serial.Microphone() as source:
        print("How can I Help you, Sir")
        while(1):
            print("Speak please!")
            audio_data = rec.record(source, duration=8)
            print("Recognizing...")
            
            try:
                text = rec.recognize_google(audio_data).lower()
                print("Speech to text: ",text)
                c=text.split()
                if "open file" in text:
                    cmd='ls'
                    os.system(cmd)
                elif("current directory" in text):
                    cmd='pwd'
                    os.system(cmd)
                elif("make directory" in text or "create directory" in text):
                    cmd='mkdir ' + c[-1]
                    os.system(cmd)    
                elif("remove directory" in text or "delete directory" in text):
                    cmd='rmdir ' + c[-1]
                    os.system(cmd)    
                elif("create file" in text or "make file" in text):
                    cmd='touch ' + c[-1]
                    os.system(cmd)  
                elif("remove file" in text or "delete file" in text):
                    cmd='rm ' + c[-1]
                    os.system(cmd)             
                elif "calculate" in text:
                    app_id = "AGQY38-9HYTAW5QL3"
                    c = wolframalpha.Client(app_id)
                    ind = text.lower().split().index('calculate')
                    text = text.split()[ind + 1:]
                    result = c.query(' '.join(text))
                    ans = next(result.results).text
                    print("The answer is " + ans)       
                elif("calendar" in text):
                    cmd='cal'
                    os.system(cmd)
                elif("date" in text):
                    cmd='date'
                    os.system(cmd) 
                elif 'wikipedia' in text:
                    print('Searching on Wikipedia..')
                    text = text.replace("wikipedia", "")
                    res = wikipedia.summary(text, sentences = 3)
                    print("According to Wikipedia:")
                    print(res)      
                elif 'weather' in text or 'whether' in text:
                    if(c[-1]=='weather'):
                        cmd = "curl wttr.in/jodhpur"
                    else:    
                        cmd = "curl wttr.in/"+c[-1]
                    os.system(cmd)    
                elif 'play music' in text or "play song" in text:
                    print("Here you go with music")
                    dir = "/home/harsh/Music"
                    songs = os.listdir(dir)
                    print(songs)
                    cmd='play *mp3'
                    os.system(cmd)   
                elif (c[0]=="open"):
                    cmd="xdg-open http://www."+c[-1]+".com"
                    os.system(cmd)

                # For Mathemetical operation
                else:
                    l = len(text)
                    str=""
                    a=""
                    b=""
                    c=1
                    for i in range(l):
                        if(text[i]==' '):
                            c+=1
                        elif(c==1):
                            str+=text[i]
                        elif(c==2):
                            a+=text[i]
                        elif(c==4):
                            b+=text[i]

                    if(str=="add"):
                        print(int(a)+int(b))
                    elif(str=="subtract"):
                        print(int(b)-int(a))
                    elif(str=="multiply"):
                        print(int(b)*int(a))
                    elif(str=="divide"):
                        print(int(a)/int(b))        
            except:
                print("couldn't listen properly")
import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
from random import choice
import os
from lxml import html
import requests
import json
import feedparser #hava  durumunu çekmek için


r=sr.Recognizer()

# locCode=EUR|TR|06420|ANKARA| > KITA|ULKE|POSTAKODU|IL 

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
            print(ask)

        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio,language='tr-TR')
        except sr.UnknownValueError:
            speak("ne dedin, anlamadım , acaba tekrar edermisin")
            print("OWL ASİSTAN = ne dedin, anlamadım , acaba tekrar edermisin")



        except sr.RequestError:
            speak('Sistemin çalışmıyor')
            print('OWL ASİSTAN = Sistemin çalışmıyor')


        return voice

def response(voice):
    if 'nasılsın' in voice:
        sozler = ["iyilik benden ya sen",
                "iyi ben peki ya sen",
                "iyi olduğumu duyunca sevineceğini biliyorum",
                "ben bir yapay zekadan ibaretim duygularım yok ama tüm yazılımım düzgün çalışıyor",
                
        ]
        secim=choice(sozler)#sozlerden birini karışık olarak seçilecek

        speak(secim)#seçilen söz seslendiriliecek
        print("OWL ASİSTAN = "+secim)#seçilen söz yazdırılacak

    if 'teşekkür ederim' in voice:
        print("OWL ASİSTAN = ne demek herzaman")
        speak("ne demek herzaman")
    
    if 'iyiyim' in voice:
        print("OWL ASİSTAN = iyi olmana sevindim senin için ne yapabilirim")
        speak("iyi olmana sevindim senin için ne yapabilirim")
    
    if 'kötüyüm' in voice:
        sozlerOlumsuz = ["üzüldüm senin adına yapabileceğim bir şey varmı",
                "sıkma canını benim yapabileceğim bir şey varmı",
                "boşver iyi olmaya bak senin için birşey yapabilirmiym",
                "ben bir yapay zekayım sadece sana yardımcı olabilirim bu konuda elimden birşey gelmez ama  istersen başka bir şey yapabilirim",
                
        ]
        secimolumsuz=choice(sozlerOlumsuz)#sozlerden birini karışık olarak seçilecek

        speak(secimolumsuz)#seçilen söz seslendiriliecek
        print("OWL ASİSTAN = "+secimolumsuz)

    if 'Fıkra anlat' in voice:
        fıkralar = ["Temel aldığı bir daktiloyu bozuk diye geri götürdü. Satıcı Neresi bozuk, dün aldığında sağlamdı.Temel:İki tane a yok, saat yazamıyorum.",
                "Karınca Ve FilBir gün bir karınca bir file aşık olmuş. Annesi bu durumu onaylamamış  Karınca Bana değil karnımdakine acı, demiş.",
                "Bektaşi'ye sormuşlar. Dünya öküzün boynuzlarının üstünde duruyormuş, ne diyorsun bu işe? Valla onu bilmem ama buna inanan öküzlerin olduğunu biliyorum, demiş.",
                "Temel'in eldivenle yazı yazdığını görenler sormuş Niye eldivenli yazıyorsun zor olmuyor mu?  Zorluğuna zor ama el yazımın tanınmasını istemeyrum.",
                
        ]
        secimfık=choice(fıkralar)#sozlerden birini karışık olarak seçilecek

        speak(secimfık)#seçilen söz seslendiriliecek
        print("OWL ASİSTAN = "+secimfık)

    



    if 'Sen kimsin' in voice:
        speak('Benim adım OWL asistan yani baykuş asistan demek 7 24 çalışıyorum')
        print('OWL ASİSTAN = Benim adım OWL asistan yani baykuş asistan demek 7 24 çalışıyorum')
        

    if 'saat kaç' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))
        print("OWL ASİSTAN = "+datetime.now().strftime('%H:%M:%S'))
    if 'arama yap' in voice:
        search = record('ne aramamı istersin')
        url ='https://google.com/search?q='+search
        webbrowser.get().open(url)
        speak(search+' için bulduğum sonuçlar')
        print("OWL ASİSTAN = "+search+' için bulduğum sonuçlar')
    
    if 'hava durumu' in voice:
        parse = feedparser.parse("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|71100|KIRIKKALE|")
        parse = parse["entries"][0]["summary"]
        parse = parse.split()
        havail=parse[2] 
        havadetay=parse[4]
        speak(havail+" için hava"+havadetay+" derece")
        print("OWL ASİSTAN = "+havail+" için hava"+havadetay+" derece")


    if 'güle güle' in voice:
        speak('görüşürüz')
        print('OWL ASİSTAN = görüşürüz')
        exit()

def speak(string):
    tts = gTTS(string,lang='tr')
    rand=random.randint(1,100)
    file= 'ses-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

speak('Seni dinliyorum Senin için ne yapabilirim')
print('OWL ASİSTAN = Seni dinliyorum Senin için ne yapabilirim')
time.sleep(1)
while 1:
    voice=record()
    print(voice)
    response(voice)

import speech_recognition as sr #çevrimiçi ve çevrim dışı bir şekilde çalışan konuşma tanıma kütüphanesi
from datetime import datetime #anlık zamanı öğrenmek için
import webbrowser # web browser açmak için
import time #bilgisayrı uyutmak için
from gtts import gTTS #text i ses e çevirmek için
from playsound import playsound#ses dosyasını çalmak için
import random#random bir sayı üretmek için
from random import choice#random bir değer seçmek için
import os#sistem ayarları değiştirmk için
from lxml import html#html dosyasını okumak için
import requests #istek göndermek için
import json # json dosyalarını okumak için
import feedparser #hava  durumunu çekmek için
import colorama #terminal ekranını özelleştirmek için
from colorama import Fore, Back, Style #Gerekli dosya ve sabitleri projemize dahil ettiğimize göre kullanım için gerekli init() fonksiyonunun çağırılması için.

r=sr.Recognizer()#speech recognition ile alınan sesi r adlı değikene atıyoruz
colorama.init()


def record(ask = False):#record adlı bir fonksiyon oluşturuyoruz ve varsayılan olarak ask =false olarak ayarlıyouz
    with sr.Microphone() as source: #mikrofandan gelen veriyi işlem yapabilmek için source e tanımlıyoruz
        if ask:
            speak(ask)
            print(Fore.BLUE)
            print(ask)

        audio = r.listen(source) # dinlenilen source u audio ya atıyoruz
        voice = ''
        try:#
            voice = r.recognize_google(audio,language='tr-TR')#Türkçe dinleme yapıp bunu voice e atıyoruz
        except sr.UnknownValueError:#gelen sesi tanımlayamazsa burası çalışıyor
            speak("ne dedin, anlamadım , acaba tekrar edermisin")
            print(Fore.GREEN)
            print("OWL ASİSTAN = ne dedin, anlamadım , acaba tekrar edermisin")



        except sr.RequestError:# eğerki sistemle alakalı bir hata alırsak burası çalışıyoruz
            speak('Sistemin çalışmıyor')
            print(Fore.GREEN)
            print('OWL ASİSTAN = Sistemin çalışmıyor')


        return voice #dinlediğimiz voice ı geri döndürüyoruz

def response(voice):#voice ile gelen veriyi sorgululamak için response adında bir fonkiyon
    if 'nasılsın' in voice:# eğer voice nin içinde nasılsın  diye bir değer varsa bunları yap
        #sözler adlı bir dizi tanımlıyoruz
        sozler = ["iyilik benden ya sen",
                "iyi ben peki ya sen",
                "iyi olduğumu duyunca sevineceğini biliyorum",
                "ben bir yapay zekadan ibaretim duygularım yok ama tüm yazılımım düzgün çalışıyor",
                
        ]
        secim=choice(sozler)#sozlerden birini karışık olarak seçilecek

        speak(secim)#seçilen söz seslendiriliecek
        print(Fore.GREEN)
        print("OWL ASİSTAN = "+secim)#seçilen söz yazdırılacak

    if 'teşekkür ederim'  in voice:# eğer voice nin içinde teşekkür ederim diye bir değer varsa bunları yap
        print(Fore.GREEN)
        print("OWL ASİSTAN = ne demek herzaman")#ekrana yazılacak veri
        speak("ne demek herzaman")#sesli bir şekilde söylenmesi için
    
    if 'iyiyim' in voice:# eğer voice nin içinde iyiyim diye bir değer varsa bunları yap
        print(Fore.GREEN)
        print("OWL ASİSTAN = iyi olmana sevindim senin için ne yapabilirim")#ekrana yazılacak veri
        speak("iyi olmana sevindim senin için ne yapabilirim")#sesli bir şekilde söylenmesi için
    
    if 'kötüyüm'  in voice:# eğer voice nin içinde kötüyüm diye bir değer varsa bunları yap
        #sozlerOlumsuz adlı bir dizi tanımlıyoruz
        sozlerOlumsuz = ["üzüldüm senin adına yapabileceğim bir şey varmı",
                "sıkma canını benim yapabileceğim bir şey varmı",
                "boşver iyi olmaya bak senin için birşey yapabilirmiym",
                "ben bir yapay zekayım sadece sana yardımcı olabilirim bu konuda elimden birşey gelmez ama  istersen başka bir şey yapabilirim",
                
        ]
        secimolumsuz=choice(sozlerOlumsuz)#sozlerden birini karışık olarak seçilecek

        speak(secimolumsuz)#seçilen söz seslendiriliecek
        print(Fore.GREEN)
        print("OWL ASİSTAN = "+secimolumsuz)#seçilen söz ekrana yazılması için

    if 'Fıkra anlat' in voice:# eğer voice nin içinde Fıkra anlat diye bir değer varsa bunları yap
        #fıkralar adlı bir dizi tanımlıyoruz
        fıkralar = ["Temel aldığı bir daktiloyu bozuk diye geri götürdü. Satıcı Neresi bozuk, dün aldığında sağlamdı.Temel:İki tane a yok, saat yazamıyorum.",
                "Karınca Ve FilBir gün bir karınca bir file aşık olmuş. Annesi bu durumu onaylamamış  Karınca Bana değil karnımdakine acı, demiş.",
                "Bektaşi'ye sormuşlar. Dünya öküzün boynuzlarının üstünde duruyormuş, ne diyorsun bu işe? Valla onu bilmem ama buna inanan öküzlerin olduğunu biliyorum, demiş.",
                "Temel'in eldivenle yazı yazdığını görenler sormuş Niye eldivenli yazıyorsun zor olmuyor mu?  Zorluğuna zor ama el yazımın tanınmasını istemeyrum.",
                "Bir deli hastenisnde herkes zıplıyor, Temel yerinden kımıldamıyormuş  Biz patlamış mısırız, ben tavanın altına yapışmışım.",
                "Küçük çocuk okulun ilk günü sonunda eve döner. Annesi sorar;  Bugün okulda ne öğrendiniz? Çocuk cevaplar; Yeterli değil, yarın tekrar gitmem gerek",

                
        ]
        secimfık=choice(fıkralar)#sozlerden birini karışık olarak seçilecek

        speak(secimfık)#seçilen söz seslendiriliecek
        print(Fore.GREEN)
        print("OWL ASİSTAN = "+secimfık)#seçilen söz ekrana yazılması için

    if 'Hikaye anlat' in voice:# eğer voice nin içinde hikaye anlat diye bir değer varsa bunları yap
        #fıkralar adlı bir dizi tanımlıyoruz
        hikayeler=[
                "Bir varmış bir yokmuş iki varmış üç yokmuş ve son",
                "Bir akıl hastanesini ziyareti sırasında, adamın biri sorar: Bir insanın akıl hastanesine yatıp yatmayacağını nasıl belirliyorsunuz?Doktor, Bir küveti su ile dolduruyoruz. Sonra hastaya üç şey veriyoruz. Bir kaşık, bir fincan, ve bir kova. Sonra da kişiye küveti nasıl boşaltmayı tercih ettiğini soruyoruz. Siz ne yapardınız?, der.Adam, Ooo! Anladım. Normal bir insan kovayı tercih eder. Çünkü kova, kaşık ve fincandan büyük. Hayır, der doktor, normal bir insan küvetin tıpasını çeker.",
                "Hintli  bir adam suda bata çıka ilerlemeye çalışırken yanına bir akrep gelir. Onu kurtarmaya karar verir ve parmağını akrebe uzatır ama akrep onu sokar. Hintli tekrar akrebi sudan kurtarmaya çalışır ama akrep onu tekrar sokar.Yakınlarındaki başka biri ona, sürekli onu sokmaya çalışan akrebi kurtarmaya çalışmaktan vazgeçmesini söyler. Ama Hintli adam şöyle der:Sokmak akrebin doğasında vardır. Benim doğamda ise sevmek var. Neden sokmak akrebin doğasında var diye kendi doğamda olan sevmekten vazgeçeyim? "
        ]
        secimhikaye=choice(hikayeler)#hikayelerden birini karışık olarak seçilecek

        speak(secimhikaye)#seçilen hikaye seslendiriliecek
        print(Fore.GREEN)
        print("OWL ASİSTAN = "+secimhikaye)#seçilen hikaye ekrana yazılması için

    
    if 'Neler yapabilirsin' in voice:# eğer voice nin içinde neler yapabilirsin diye bir değer varsa bunları yap
        speak('seninle sohbet edebilirim , saati söyleyebiilirim , hava durumunu söylerim ,senin yerine googleda arama yaparım ,canın sıkıldıysa fıkra anlatabilirim yada hikaye anlatabilirim , youtube dan birşeyler aratabilirim . peki sen ne yapmamı istersin')
        print(Fore.GREEN)
        print('seninle sohbet edebilirim , saati söyleyebiilirim , hava durumunu söylerim ,senin yerine googleda arama yaparım ,canın sıkıldıysa fıkra anlatabilirim yada hikaye anlatabilirim , youtube dan birşeyler aratabilirim . peki sen ne yapmamı istersin')

    if 'Sen kimsin'  in voice:# eğer voice nin içinde sen kimsin diye bir değer varsa bunları yap
        print(Fore.GREEN)
        speak('Benim adım OWL asistan yani baykuş asistan demek 7 24 çalışıyorum')#selendirelecek
        print('OWL ASİSTAN = Benim adım OWL asistan yani baykuş asistan demek 7 24 çalışıyorum')#ekrana yazılacak
        

    if 'saat kaç' in voice:# eğer voice nin içinde saat kaç diye bir değer varsa bunları yap
        speak(datetime.now().strftime('%H:%M:%S'))#datetime.now sayesinde anlık saati alıyoruz ve seslendiriyouz
        print(Fore.GREEN)
        print("OWL ASİSTAN = "+datetime.now().strftime('%H:%M:%S'))#datetime.now sayesinde anlık saati alıyoruz ve yazdırıyoruz

    if 'arama yap' in voice:# eğer voice nin içinde arama yap diye bir değer varsa bunları yap
        search = record('ne aramamı istersin')#record ile aranmasını istediğimiz kelimeyi yada cümleyi alıp search değişkenine tanımlıyouz
        url ='https://google.com/search?q='+search#https://google.com/search?q= adresine aldığımız search ı ekliyoruz ve url değişkenine tanımlıyouz
        webbrowser.get().open(url)#web browserı açıyouz ve  url değişkenini dönderiyouz
        speak(search+' için bulduğum sonuçlar')#sesli bir şekilde seslendirme yapıyouz
        print(Fore.GREEN)
        print("OWL ASİSTAN = "+search+' için bulduğum sonuçlar')#ekrana yazdırma yapıyouz
    
    if "YouTube'da ara" in voice:# eğer voice nin içinde arama yap diye bir değer varsa bunları yap
        searchy = record('ne aramamı istersin')#record ile aranmasını istediğimiz kelimeyi yada cümleyi alıp searchy değişkenine tanımlıyouz
        urly ='https://www.youtube.com/results?search_query='+searchy#https://google.com/search?q= adresine aldığımız searchy ı ekliyoruz ve urly değişkenine tanımlıyouz
        webbrowser.get().open(urly)#web browserı açıyouz ve  urly değişkenini dönderiyouz
        speak(searchy+' için bulduğum sonuçlar')#sesli bir şekilde seslendirme yapıyouz
        print(Fore.GREEN)
        print("OWL ASİSTAN = "+searchy+' için bulduğum sonuçlar')#ekrana yazdırma yapıyouz
    
    if 'hava durumu' in voice:# eğer voice nin içinde hava durumu diye bir değer varsa bunları yap
        #feedparser ile link deki veriyi çekip parçalıyouz bunuda parse değişkenine tanımlıyouz
        parse = feedparser.parse("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|71100|KIRIKKALE|")
        parse = parse["entries"][0]["summary"]
        parse = parse.split()
        havail=parse[2] #havaiiladlı adlı değişkene parsenin 3.değeri olan il adını tanımlıyoruz
        havadetay=parse[4] #havadetay adlı  değişkene parsenin 5. değeri olan dereceyi tanımlıyoruz
        speak(havail+" için hava"+havadetay+" derece")#sesli söyletiouz
        print(Fore.GREEN)
        print("OWL ASİSTAN = "+havail+" için hava"+havadetay+" derece")#ekrana yazdırıyouz
    


    if 'güle güle' in voice:# eğer voice nin içinde güle güle diye bir değer varsa bunları yap
        speak('görüşürüz')#sesli söyletiouz
        print(Fore.GREEN)
        print('OWL ASİSTAN = görüşürüz')#ekrana yazdırıyouz
        exit()# uygulamadan çıkış yapıyouz

def speak(string):#speak adlı bir fonksiyon oluştuyouz 
    tts = gTTS(string,lang='tr')#sesi text e türkçe olarak çevirip tts adlı değişkene tanımlıyouz
    rand=random.randint(1,100)#random 1 ve 100 arası bir sayı üretip rand adlı değişkene tanımlıyouz bunun amacı bir hata ile karşılaşıp mp3 dosyası silinmezse üsütne yazmasın diye
    file= 'ses-'+str(rand)+'.mp3'#.mp3 uzantılı bir ses dosyası oluşturuyoruz
    tts.save(file)#dosyayı kayıt ediyouz
    playsound(file)#dosyayı okutuyoyz
    os.remove(file)#dosyayı siliyouz




speak('Seni dinliyorum Senin için ne yapabilirim')#ilk açılışta asiatanın bizi karşılaması için
print(Fore.GREEN)
print('OWL ASİSTAN = Seni dinliyorum Senin için ne yapabilirim')#ilk açılışta asiatanın bizi karşılamasını yazdırmak için
time.sleep(1)#uygulamyı 1 saniye uyutuyouz dinlemede karışıklık olmaması için
while 1:#tek bir komut aldıktan sonra kapanmaması için sonsuz döngü oluşturuyoruz
    voice=record()
    print(Fore.BLUE)
    print(voice)
    response(voice)



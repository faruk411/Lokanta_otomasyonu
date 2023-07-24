from playsound import playsound
from gtts import gTTS
from abc import ABC, abstractmethod
import os
import matplotlib.pyplot as plt
from tkinter import*
import tkinter as tk

def konus(string):
    tts = gTTS(text=string, lang="tr")
    dosya = "cevap.mp3"
    tts.save(dosya)
    playsound(dosya)
    os.remove(dosya)
    print(string)
class KDV_hesabi:
    def __init__(self):
        self.yemeklist = [15,10,14,20,25,15,12,12,25,15]
        self.iceceklist = [8,8,5,60,4,4,16,17,12,15]
        self.tatlilist = [4,2,3,14,14,14,15,20,10,10]
    def yemek_kdv_hesapla(self):
        secim = int(input(" keşkek için 1 \n lahmacun için 2  \n orman kebabı için 3 \n abant kebebı için 4 \n bolu köftesi için 5 \n göbekdolması için 6 \n etli bamya için 7 \n bakla dolması için 8 \n paşa pilavı için 9 \n bakla çullaması için 10 \n"))
        secim -= 1
        print(self.yemeklist[secim] * 8 / 100)
    def icecek_kdv_hesapla(self):
        secim = int(input(" kola için 1 \n fanta için 2 \n ayran için 3 \n kımız için 4 \n su için 5 \n çay için 6 \n latte için 7 \n macchiato için 8 \n türk kahvesi için 9 \n visto için 10 "))
        secim -= 1
        print(self.iceceklist[secim] * 8 / 100)
    def tatli_kdv_hesapla(self):
        secim = int(input("baklava için 1 \n tulumba için 2 \n halka tatlısı için 3 \n cheesecake için 4 \n tramisu için 5\n trileçe için 6 \n kemalpaşa tatlısı için 7 \n fondü için 8 \n sütlaç için 9 \n künefe için 10 "))
        secim -= 1
        print(self.tatlilist[secim] * 8 / 100)
class Lokanta(ABC):
    @abstractmethod
    def __init__(self,isim):
        self.isim = isim
    @abstractmethod
    def isimgetir(self):
        return self.isim
    @abstractmethod
    def Getisim(self):
        print("Lokantanın ismi = ",self.isim)
class SiparisEt(Lokanta):
    def __init__(self, isim):
        super().__init__(isim)
        self.siparisler = []
        self.fiyatlartoplami = []
    def Getisim(self):
        return super().Getisim()
    def isimgetir(self):
        return super().isimgetir()
    def YemekSiparisi(self):
        self.yemek = int(input("hangi yiyeceği istersiniz ? "))
        if self.yemek == 1:
            konus(self.isim)
            konus("için 1 adet merzifon keşkeği gidiyor")
            self.siparisler.append("1X Merzifon keşkeği -----------15 TL")
            self.fiyatlartoplami.append(15)
            ahmet.zam(5)
        elif self.yemek == 2:
            konus(self.isim)
            konus("için bir adet Lahmacun .")
            self.siparisler.append("1X Lahmacun         -----------10 TL")
            self.fiyatlartoplami.append(10)
            mehmet.zam(5)
        elif self.yemek == 3:
            konus(self.isim)
            konus(" için bir adet Orman Kebabı .")
            self.siparisler.append("1X Orman kebabı     -----------14 TL")
            self.fiyatlartoplami.append(14)
            mehmet.zam(5)
        elif self.yemek == 4:
            konus(self.isim)
            konus("için 1 adet Abant kebabı")
            self.siparisler.append("1X Abant kebabı     -----------20 TL")
            self.fiyatlartoplami.append(20)
            mehmet.zam(5)
        elif self.yemek == 5:
            konus(self.isim)
            konus("için 1 adet Bolu Köftesi")
            self.siparisler.append("1X Bolu Köftesi     -----------25 TL")
            self.fiyatlartoplami.append(25)
            mehmet.zam(5)
        elif self.yemek == 6:
            konus(self.isim)
            konus(" için 1 adet Göbek Dolması")
            self.siparisler.append("1X Göbek Dolması    -----------15 TL")
            self.fiyatlartoplami.append(15)
            mehmet.zam(5)
        elif self.yemek == 7:
            konus(self.isim)
            konus(" için 1 adet Etli Bamya")
            self.siparisler.append("1X Etli Bamya       -----------12 TL")
            self.fiyatlartoplami.append(12)
            mehmet.zam(5)
        elif self.yemek == 8:
            konus(self.isim)
            konus("için 1 adet Bakla Dolması")
            self.siparisler.append("1X Bakla Dolması    -----------12 TL")
            self.fiyatlartoplami.append(12)
            ahmet.zam(5)
        elif self.yemek == 9:
            konus(self.isim)
            konus("için bir adet Paşa Pilavı")
            self.siparisler.append("1X Paşa Pilavı      -----------25 TL")
            self.fiyatlartoplami.append(25)
            mehmet.zam(5)
        elif self.yemek == 10:
            konus(self.isim)
            konus(",için 1 adet Bakla Çullaması")
            self.siparisler.append("1X Bakla Çullaması  -----------15 TL")
            self.fiyatlartoplami.append(15)
            ahmet.zam(5)
        else:
            konus("hatalı sipariş. tekrar deneyiniz")
    def IcecekSiparisEt(self):
        self.icecek = int(input("hangi içeceği istersiniz ? "))
        if self.icecek == 1:
            konus(self.isim)
            konus("için 1 adet Kola")
            self.siparisler.append("1X Kola            ------------8  TL")
            self.fiyatlartoplami.append(8)
            mehmet.zam(2)
        elif self.icecek == 2:
            konus(self.isim)
            konus("için bir adet Fanta")
            self.siparisler.append("1X Fanta           ------------8  TL")
            self.fiyatlartoplami.append(8)
            mehmet.zam(2)
        elif self.icecek == 3:
            konus(self.isim)
            konus("için 1 adet Ayran")
            self.siparisler.append("1X ayran           ------------5  TL")
            self.fiyatlartoplami.append(5)
            ahmet.zam(2)
        elif self.icecek == 4:
            konus(self.isim)
            konus("için bir adet Kımız")
            self.siparisler.append("1X Kımız           ------------60 TL")
            self.fiyatlartoplami.append(60)
            mehmet.zam(12)
        elif self.icecek == 5:
            konus(self.isim)
            konus("için 1 adet Su")
            self.siparisler.append("1X Su              ------------2  TL")
            self.fiyatlartoplami.append(2)
            ahmet.zam(5)
        elif self.icecek == 6:
            konus(self.isim)
            konus("için bir adet çay")
            self.siparisler.append("1X Çay             ------------4  TL")
            self.fiyatlartoplami.append(4)
            mehmet.zam(1)
        elif self.icecek == 7:
            konus(self.isim)
            konus("için bir adet Latte")
            self.siparisler.append("1X Latte          ------------16 TL")
            self.fiyatlartoplami.append(16)
            ahmet.zam(2)
        elif self.icecek == 8:
            konus(self.isim)
            konus(" için bir adet Macchiato")
            self.siparisler.append("1X Macchiato      ------------17 TL")
            self.fiyatlartoplami.append(17)
            ahmet.zam(2)
        elif self.icecek == 9:
            konus(self.isim)
            konus("için 1 adet türk kahvesi")
            self.siparisler.append("1X Türk kahvesi    -----------12 TL")
            self.fiyatlartoplami.append(12)
            ahmet.zam(5)
        elif self.icecek == 10:
            konus(self.isim)
            konus("için 1 adet Ice Tea")
            self.siparisler.append("1X Ice Tea        ------------15 TL")
            self.fiyatlartoplami(15)
            mehmet.zam(1)
        else:
            print("yanlış seçim yaptınız")
    def TatliSiparisEt(self):
        self.secenek = int(input("hangi tatlıyı istersiniz ? "))
        if self.secenek == 1:
            konus(self.isim)
            konus(" için 1 adet Baklava")
            self.siparisler.append("1X Baklava        ------------4  TL")
            self.fiyatlartoplami.append(4)
            mehmet.zam(6)
        elif self.secenek == 2:
            konus(self.isim)
            konus(" için 1 adet Tulumba")
            self.siparisler.append("1X tulumba        ------------4  TL")
            self.fiyatlartoplami.append(2)
            ahmet.zam(4)
        elif self.secenek == 3:
            konus(self.isim)
            konus(" için 1 adet Halka Tatlısı")
            self.siparisler.append("1X Halka tatlısı  ------------3  TL")
            self.fiyatlartoplami.append(3)
            ahmet.zam(6)
        elif self.secenek == 4:
            konus(self.isim)
            konus(" için 1 adet Cheesecake")
            self.siparisler.append("1X Cheesecake     ------------14 TL")
            self.fiyatlartoplami.append(14)
            mehmet.zam(5)
        elif self.secenek == 5:
            konus(self.isim)
            konus(" için 1 adet Tramisu")
            self.siparisler.append("1X Tramisu        ------------14 TL")
            self.fiyatlartoplami.append(14)
            mehmet.zam(4)
        elif self.secenek == 6:
            konus(self.isim)
            konus(" için 1 adet Trileçe")
            self.siparisler.append("1X Trileçe        ------------14 TL")
            self.fiyatlartoplami.append(14)
            ahmet.zam(4)
        elif self.secenek == 7:
            konus(self.isim)
            konus(" için 1 adet Kemalpaşa Tatlısı")
            self.siparisler.append("1X Kemalpaşa      ------------15 TL")
            self.fiyatlartoplami.append(15)
            mehmet.zam(2)
        elif self.secenek == 8:
            konus(self.isim)
            konus(" için 1 adet Fondü Tatlısı")
            self.siparisler.append("1X Fondü          ------------20 TL")
            self.fiyatlartoplami.append(20)
            mehmet.zam(4)
        elif self.secenek == 9:
            konus(self.isim)
            konus(" için 1 adet Sütlaç")
            self.siparisler.append("1X Sütlaç         ------------10 TL")
            self.fiyatlartoplami.append(10)
            ahmet.zam(4)
        elif self.secenek == 10:
            konus(self.isim)
            konus(" için 1 adet Künefe")
            self.siparisler.append("1X Künefe         ------------10 TL")
            self.fiyatlartoplami.append(10)
            ahmet.zam(2)
        else:
            print("yanlış sayı tuşladınız.")
    def Hesapiste(self):
        for i in range(len(self.siparisler)):
            print(self.siparisler[i])
        print("TOPLAM TUTAR = ",sum(self.fiyatlartoplami),"TL")
class Personel(Lokanta):
    def __init__(self, isim,soyisim,maaş,görev):
        super().__init__(isim)
        self.__soyisim = soyisim
        self.__maaş = maaş
        self.__görev = görev
    def gethepsi(self):
        return self.__soyisim, self.__maaş , self.__görev
    def maaşgoster(self):
        return self.__maaş
    def personelbilgisi(self):
        print("isim    :",self.isim)
        print("soyisim :",self.__soyisim)
        print("maaş    :",self.__maaş)
        print("görev   :",self.__görev)
    def Getisim(self):
        return super().Getisim()
    def isimgetir(self):
        return super().isimgetir()
    def zam(self,sayi):
        self.__maaş = self.__maaş + sayi
    def indirim(self,sayi):
        self.__maaş = self.__maaş - sayi
    def maaşgoster(self):
        print(self.isim,("adlı personelimizin maaşı : ",self.__maaş))
class MÖNNÜ(Lokanta):
    def __init__(self, isim):
         super().__init__(isim)
    def Getisim(self):
        return super().Getisim()
    def isimgetir(self):
        return super().isimgetir()
    @staticmethod
    def manümain():
        #tkinter modülü ile bir pencere oluşturduk
        p1=tk.Tk()
        #oluştruduğumuz pencerenin boyutunu ayarladık
        p1.geometry("700x500")
        #pencerenin arka planına resim ekledik
        t=PhotoImage(file="t1.png")
        #eklediğimiz resmi label(etikete aktardık)
        a=Label(p1,image=t)
        #labelin(etiketin konumunu ayarladık)
        a.place(x=0,y=0)
        #pencerenin içinde buton oluşturduk
        b1=Button(text="Yemek için tıklayın",font="arial 20",activebackground="red",background="yellow",)
        b1.pack()
        b2=Button(text="İçecek için tıklayın",font="arial 20",activeforeground="red",background="purple")
        b2.pack()
        b3=Button(text=" Tatlı  için  tıklayın ",font="arial 20",activebackground="red",background="pink")
        b3.pack()

        #butonla ile resim arasında bağ kurmak için event(olay nesnesi) komutunu kullandık

        def resim1(event):
            #matplotlib kütüphanesiyle resim ekledik
            resim = plt.imread("C:/Users/omerf/Desktop/pyhton/lokanta/proje-yemekkk.jpg")
            # imshow komutu ile görüntüyü ekrana aktardık
            plt.imshow(resim)
            #axis komutuyla resmin kenarlarındaki kordinat eksenleri sildik
            plt.axis("off")
            # show komutuyla resmi gösterdik
            plt.show()
            # buton ile resmin dahil olduğu fonksiyon ile bir bağ kurduk bu butona bastığımızda resmin gelmesini sağlayacak
        b1.bind("<Button-1>", resim1)

        def resim2(event):
            resim1 = plt.imread("C:/Users/omerf/Desktop/pyhton/lokanta/iiiiiiiiiiiiç.jpg")
            plt.imshow(resim1)
            plt.axis("off")
            plt.show()
        b2.bind("<Button-1>", resim2)

        def resim3(event):
            resim = plt.imread("C:/Users/omerf/Desktop/pyhton/lokanta/tatlı-14.jpg")
            plt.imshow(resim)
            plt.axis("off")
            plt.show()
        b3.bind("<Button-1>", resim3)
        p1.mainloop()
class Degerlendirmeformu:
    def __init__(self):
        pass
    def anketsorulari(self):
        cvpa = input("ahmet beyden memnun kaldınız mı? (e/h) ")
        if cvpa == "e":
            ahmet.zam(2)
        elif cvpa == "h":
            ahmet.indirim(25)
        cvpm = input("mehmet beyden memnun kaldınız mı? (e/h ")
        if cvpm == "e":
            mehmet.zam(2)
        elif cvpm == "h":
            mehmet.indirim(25)
        cvpy = input("şefimizden memnun kaldınız mı? (e/h) ")
        if cvpy == "e":
            yakup.zam(5)
        if cvpy == "h":
            yakup.indirim(30)
        cvph = input("baristamızdan memnun kaldınız mı? (e/h) ")
        if cvph == "e":
            hasan.zam(2)
        elif cvph == "h":
            hasan.indirim(25)
        cvpe = input("tatlıcımızdan memnun kaldınız mı? (e/h) ")
        if cvpe == "e":
            emirhan.zam(6)
        elif cvpe == "h":
            emirhan.indirim(80)
class Müdür(Lokanta):
    def __init__(self, isim):
        super().__init__(isim)
    def Getisim(self):
        return super().Getisim()
    def isimgetir(self):
        return super().isimgetir()
    def müdürgirişi(self):
        while True:
            sifre = int(input("şifreyi giriniz. (1) (çıkış için herhangi bir tuşa basın) "))
            if sifre == 1:
                konus("hoşgeldiniz Ömer bey")
                kararr = int(input("personelleriniz hakkında bilgi almak için 1'e , maaş ayarı yapmak için 2 ye basınız."))
                if kararr == 1:
                    ahmet.personelbilgisi()
                    print("- - - - - - - - - - - ")
                    mehmet.personelbilgisi()
                    print("- - - - - - - - - - - ")
                    yakup.personelbilgisi()
                    print("- - - - - - - - - - - ")
                    hasan.personelbilgisi()
                    print("- - - - - - - - - - - ")
                    emirhan.personelbilgisi()
                    krr = input(" maaş ayarı yapmak istiyor musunuz? (e/h)")
                    if krr == "e":
                        kararr = 2
                    else:
                        break
                if kararr == 2:
                    while True:
                        persomaaskarar = int(input("hangi personelimizin maaş ayarını yapmak istiyorsunuz ? \n garsonlar için 1 \n şef için 2 \n barista için 3 \n tatlıcı için 4 \n çıkış için 5"))
                        if persomaaskarar == 1:
                            garsokarar = int(input("hangi garsonumuzun maaş ayarını yapmak istiyorsunuz? ahmet bey için 1 \n mehmet bey için 2 \n "))
                            if garsokarar == 1:
                                zamindirim = int(input("zam mı yapacaksınız yoksa indirim mi? zam için 1 \n indirim için 2 \n"))
                                if zamindirim == 1:
                                    x = int(input("kaç lira zam yapacağız"))
                                    ahmet.zam(x)
                                    print("ahmet beyin maaşı ",ahmet.maaşgoster()," lira olmuştur")
                                elif zamindirim == 2:
                                    x = int(input("kaç lira indirim yapacaksınız"))
                                    ahmet.indirim(x)
                                    print("ahmet beyin maaşı ",ahmet.maaşgoster()," lira olmuştur")
                            if garsokarar == 2:
                                zamindirim = int(input("zam mı yapacaksınız yoksa indirim mi? \n zam için 1 indirim için 2 \n "))
                                if zamindirim == 1:
                                    x = int(input("ne kadar zam yapılacak? "))
                                    mehmet.zam(x)
                                    print("mehmet beyin maaşı ",mehmet.maaşgoster()," olmuştur.")
                                elif zamindirim == 1:
                                    x = int(input("kaç lira indirim yapacaksınız. "))
                                    mehmet.indirim(x)
                                    print("mehmet beyin maaşı ",mehmet.maaşgoster()," olmuştur.")
                        elif persomaaskarar == 2:
                            zamindirim = int(input("zam mı yapacaksınız yoksa indirim mi? zam için 1 \n indirim için 2 \n"))
                            if zamindirim == 1:
                                x = int(input("kaç lira zam yapacağız"))
                                yakup.zam(x)
                                print("yakup beyin maaşı ",yakup.maaşgoster()," lira olmuştur.")
                            elif zamindirim == 2:
                                x = int(input("kaç lira indirim yapacaksınız ? "))
                                yakup.indirim(x)
                                print("yakup beyin maaşı ",yakup.maaşgoster()," lira olmuştur.")
                        elif persomaaskarar == 3:
                            zamindirim = int(input("zam mı yapacaksınız yoksa indirim mi? zam için 1 \n indirim için 2 \n"))
                            if zamindirim == 1:
                                x = int(input("kaç lira zam yapacağız"))
                                hasan.zam(x)
                                print("hasan beyin maaşı ",hasan.maaşgoster()," lira olmuştur.")
                            elif zamindirim == 2:
                                x = int(input("kaç lira indirim yapacaksınız ? "))
                                hasan.indirim(x)
                                print("hasan beyin maaşı ",hasan.maaşgoster()," lira olmuştur.")
                        elif persomaaskarar == 4:
                            zamindirim = int(input("zam mı yapacaksınız yoksa indirim mi? zam için 1 \n indirim için 2 \n"))
                            if zamindirim == 1:
                                x = int(input("kaç lira zam yapacağız"))
                                emirhan.zam(x)
                                print("emirhan beyin maaşı ",emirhan.maaşgoster()," lira olmuştur.")
                            elif zamindirim == 2:
                                x = int(input("kaç lira indirim yapacaksınız ? "))
                                emirhan.indirim(x)
                                print("emirhan beyin maaşı ",emirhan.maaşgoster()," lira olmuştur.")
                        else:
                            break
            else:
                break
class window(Lokanta):
    def __init__(self, isim):
        super().__init__(isim)
    def isimgetir(self):
        return super().isimgetir()
    def Getisim(self):
        return super().Getisim()
    @classmethod
    def pencere(cls,event):
        p=tk.Tk()
        p.geometry("1000x1000")
        label=tk.Label(p,text="""
Bolu mutfağı Osmanlı döneminde meşhur olmaya başlandı. 
Bolu'nun yemeklerinin bu kadar meşhur olmasının nedenlerinden biri ;
Roma Bizans ve Osmanlı kültürlerine ev sahipliği yapmış olmasıdır. 
Bu da yemek çeşitliğini etkilemiştir. Hala bir çok yerde saray 
mutfaklarının yemekleri hakimdir. Sebze yemekleri pek tercih 
edilmez bu yörede.Aşçıları ile meşhur olan bolu dünyaca ünlü aşçılara
ev sahipliği yapar,özellikle Mengenli aşçılar dünyaca 
tanınmışlardır.Mengen'den yetişen aşçıların tarihi padişah mutfaklarına kadar 
dayanmaktadır. Atatürk'ün aşçısı da Mengenliydi. Günümüzde 
turistik tesislerin bir çoğunda Mengenli aşçılara rastlamak 
mümkündür. Aşçılık sanatı Mengen İlçesinin ata mesleğidir.
                                """,font="arial 20")
        label.place(x=10,y=10)
        p.mainloop()
    @classmethod
    def pencere1(cls,event):
        p1=tk.Tk()
        p1.geometry("800x800")
        label1=tk.Label(p1,text=""" 
Merzifon, M.Ö. 20 yıllarında, İmparator OGÜST tarafından
bayındır bir duruma getirilmiş ve adı FAZEMON NEOPOLİS 
olarak değiştirilmiştir. M.Ö. 5.yüzyılda FAZEMON NEOPOLİS,
Bizans topraklarına katılmış ve Merzifon adıyla anılmaya 
başlanmıştır. Amasya Tarihinin yazarı Hüseyin Hüsamettin 
Bey, Merzifon’un en az iki bin yıllık tarihi olduğundan söz 
eder. Merz sözcüğünün Farsa da SINIR, YEREL ve SESSİZLİK 
anlamına geldiğini, sonundaki FON takısının PONT sözcüğünün 
Arapçalaştırılmışı olduğunu söyler. Buna göre Merzifon, Pont 
Sınırı ya da Pont Karargâhı anlamına gelmektedir. 
Alman Bilginlerinden, Doğu Ülkeleri Tarihçisi MORTMAN, 
1850 yılında, Samsun üzerinden Merzifon’a uğramış, o da 
Merzifon’un en az iki bin yıllık bir geçmişi olduğunu ve eski 
çağlardaki adının PRAZEMON olduğunu yazmıştır.
""",font="arial 20")
        label1.place(x=10,y=10)
        p1.mainloop()
    def buton(self):
        p2=tk.Tk()
        p2.geometry("600x600")
        p2.title("Tarihçe")
        b1=Button(p2,text="      Bolu için basınız      ",font="arial 20",background="yellow")
        b1.pack()
        b2=Button(p2,text="Amasya(Merzifon) için basınız",font="arial 20",background="red")
        b2.pack()
        b1.bind("<Button-1>",w.pencere)
        b2.bind("<Button-1>",w.pencere1)
        p2.mainloop()
w=window("tarihçeler")
#tanımlanan personel isimleri:
ahmet = Personel("ahmet","köse",4250,"garson")
mehmet= Personel("mehmet","toprak",4250,"garson")
yakup = Personel("yakup","kara",5000,"şef")
hasan = Personel("hasan","kaya",4900,"barista")
emirhan = Personel("emirhan","çırpan",4250,"tatlıcı")
ahmet.gethepsi()
mehmet.gethepsi()
yakup.gethepsi()
hasan.gethepsi()
emirhan.gethepsi()
#1 adet form tanımlandı.
form = Degerlendirmeformu()
#1 adet menümüz mevcut.
menü = MÖNNÜ("menü")
#10 adet 1 listeye sırasıyla konmuş masa numaraları
masa1 = SiparisEt("masa 1")
masa2 = SiparisEt("masa 2")
masa3 = SiparisEt("masa 3")
masa4 = SiparisEt("masa 4")
masa5 = SiparisEt("masa 5")
masa6 = SiparisEt("masa 6")
masa7 = SiparisEt("masa 7")
masa8 = SiparisEt("masa 8")
masa9 = SiparisEt("masa 9")
masa10= SiparisEt("masa 10")
masalar = [masa1,masa2,masa3,masa4,masa5,masa6,masa7,masa8,masa9,masa10]
print("halihazırda masalarımız:")
for i in range(len(masalar)):
    print(masalar[i].isim)
    i += 1
kdv = KDV_hesabi()
ömerbey = Müdür("ömer")
while True:
    secim = int(input("siparişe başlamak için 1' i, kdv hesaplamak için 2'yi müdür girişi için 3'ü tuşlayınız = "))
    if secim == 1:
        while True:
            print("---------------------------------------------------------")
            masabilgisi = int(input("hangi masada oturacaksınız ? (çıkış için (0)) "))
            print("---------------------------------------------------------")
            if masabilgisi == 0:
                break
            masabilgisi -= 1
            secimm = int(input("\n-----------------------yemek sipariş etmek için 1 \niçecek sipariş etmek için 2 \ntatlı sipariş etmek için 3 ü \nsiparişiniz bittiyse 4 ü \nmenü için 5 i \nsiparişleri beklerken tarihçeye bakmak için 6 'yı \ntuşlayınız.\n----------------------------- "))
            while True:
                if secimm == 1:
                    masalar[masabilgisi].YemekSiparisi()
                    scm = int(input("------------- \n başka bir arzunuz ? \n----------- \n 1 = (devam etmek istiyorum) \n 2 = (içecek seçeceğim) \n 3 = (tatlı sipariş edeceğim) \n 4 = (hesabımı istiyorum) \n 5 = (menüye tekrar bakacağım) \n 6 = (tarihçeye bakmak isterim) \n ----------"))
                    if scm == 1:
                        True
                    elif scm == 2:
                        secimm = 2
                    elif scm == 3:
                        secimm = 3
                    elif scm == 4:
                        secimm = 4
                    elif scm == 5:
                        secimm = 5
                    elif scm == 6:
                        secimm = 6
                elif secimm == 2:
                    masalar[masabilgisi].IcecekSiparisEt()
                    scm = int(input("\n -------------- başka bir arzunuz ? \n----------- \n 1 = (devam etmek istiyorum) \n 2 = (yemek seçeceğim) \n 3 = (tatlı sipariş edeceğim) \n 4 = (hesabımı istiyorum) \n 5 = (menüye tekrar bakacağım) \n 6 = (tarihçeye bakmak isterim) \n -----------"))
                    if scm == 1:
                        True
                    elif scm == 2:
                        secimm = 1
                    elif scm == 3:
                        secimm = 3
                    elif scm == 4:
                        secimm = 4
                    elif scm ==5:
                        secimm = 5
                    elif scm == 6:
                        secimm = 6
                elif secimm == 3:
                    masalar[masabilgisi].TatliSiparisEt()
                    scm = int(input("başka bir arzunuz ? \n----------- \n 1 = (devam etmek istiyorum) \n 2 = (içecek seçeceğim) \n 3 = (yemek sipariş edeceğim) \n 4 = (hesabımı istiyorum) \n 5 = (menüye tekrar bakacağım) \n 6 = (tarihçeye bakmak isterim)"))
                    if scm == 1:
                        True
                    elif scm == 2:
                        secimm = 2
                    elif scm == 3:
                        secimm = 1
                    elif scm == 4:
                        secimm = 4
                    elif scm == 5:
                        secimm = 5
                    elif scm == 6:
                        secimm = 6
                elif secimm == 4:
                    masalar[masabilgisi].Hesapiste()
                    soru = input("anketimize katılmak ister misiniz? (e/h) ")
                    if soru == "e":
                        form.anketsorulari()
                        print("bizi seçtiğiniz için teşekkürler.")
                        break
                    if soru == "h":
                        print("bizi seçtiğiniz için teşekkürler.")
                        break
                elif secimm == 5:
                    menü.manümain()
                    scm = int(input("başka bir arzunuz ? \n----------- \n 1 = (devam etmek istiyorum) \n 2 = (içecek seçeceğim) \n 3 = (tatlı sipariş edeceğim) \n 4 = (hesabımı istiyorum) \n 5 = (menüye tekrar bakacağım) \n 6 = (tarihçeyi görmek isterim)"))
                    if scm == 1:
                        True
                    elif scm == 2:
                        secimm = 2
                    elif scm == 3:
                        secimm = 3
                    elif scm == 4:
                        secimm = 4
                    elif scm == 5:
                        secimm = 5
                    elif scm == 6:
                        secimm = 6
                elif secimm == 6:
                    w.buton()
                    scm = int(input("başka bir arzunuz ? \n----------- \n 1 = (devam etmek istiyorum) \n 2 = (içecek seçeceğim) \n 3 = (yemek sipariş edeceğim) \n 4 = (hesabımı istiyorum) \n 5 = (menüye tekrar bakacağım) \n 6 = (tarihçeyi görmek isterim) \n ------------"))
                    if scm == 1:
                        True
                    elif scm == 2:
                        secimm = 2
                    elif scm == 3:
                        secimm = 3
                    elif scm == 4:
                        secimm = 4
                    elif scm == 5:
                        secimm = 5
    elif secim == 2:
        while True:
            kdvsecim = int(input(" yiyecek kdv hesaplamak için 1 \n içecek kdv hesaplamak için 2 \n tatlı kdv hesaplamak için 3  \n çıkış için 4 ü \n tuşlayınız: \t"))
            if kdvsecim == 1:
                kdv.yemek_kdv_hesapla()
            elif kdvsecim == 2:
                kdv.icecek_kdv_hesapla()
            elif kdvsecim == 3:
                kdv.tatli_kdv_hesapla()
            elif kdvsecim == 4:
                break
            else:
                print("yanlış sayı girdiniz.")
    elif secim == 3:
        ömerbey.müdürgirişi()
    else:
        print("yanlış seçim yaptınız. ")
        break

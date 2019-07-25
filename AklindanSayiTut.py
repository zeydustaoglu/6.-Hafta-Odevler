# 6. HAFTA ODEVLER
#
# ODEV 1: Sayi Tahmin
# 		-Kullanicidan aklindan 0-100 araliginda bir sayi tutmasini isteyin.
# 		-Yazdiginiz kod ile bu sayiyi tahmin etmeye calisin.
# 		-Tahmin sonucunda, kullanicidan alacaginiz input, pc'nin tahmin ettigi sayi kullanicinin belirledigi
# 		 sayidan buyukse kullanici daha dusuk sayi tahmin etmelisin manasinda "-" seklinde olsun, pc'nin tahmin
# 		 ettigi sayi kullanicinin belirledigi sayidan kucukse "+" seklinde olsun.
# 		-Pc'nin tahmini dogru oldugunda da kullanicidan bunu belirtebilecegi bir input isteyin.
# 		-Gelistireceginiz algoritma sayesinde kullanicinin belirledigi sayiyi en az hamlede bilmeye calisin :)
#
# 		Ornek:
#
# 			 Kullanicinin aklindan tuttugu sayi: 56 (kullanicidan bunun icin bir input almayacagiz sadece
# 			 aklinizdan bir sayi belirlemis iseniz oyunumuza baslayabiliriz seklinde bir input alabiliriz.
# 			 Yani belirledigi sayiyi sisteme girmesini istemiyoruz.)
#
# 			 Pc'nin tahmini = 89
# 			 Kullanicinin inputu = -
# 			 Pc'nin tahmini = 45
# 			 Kullanicinin inputu = +
# 			 Pc'nin tahmini = 56
# 			 Kullanicinin inputu = "Enter"

oyuna_basla=input("Aklinizdan 0-100 arasi sayi tutun. Hazirsaniz baslamak icin 1e basin:")
import random
buyukmu=''
#kullanicidan alacagimiz inputu aktaracagimiz degisken
sayac=0
#programin sayiyi kacinci denemede bilecegini hesaplayacagimiz sayac

if oyuna_basla=="1":
    while True:
        if buyukmu=="":
            sayi = random.randint(1, 100)
            print("Tahmin ettiginiz sayi bu mu ? {} ".format(sayi))
            buyukmu = input("Tahmin ettiginiz sayi daha kucuk ise - daha buyuk ise + ya basin. Dogru ise d ye basin :")
            sayac+=1
        elif buyukmu == "-":
            sayi = random.randint(1, sayi)
            #kullanici - girerse yani aklimdaki sayi daha kucuk derse,1 ile onceki rastgele sayi arasinda yeni bir sayi olusturuyoruz
            print("Tahmin ettiginiz sayi bu mu ? {} ".format(sayi))
            buyukmu = input("Tahmin ettiginiz sayi daha kucuk ise - daha buyuk ise + ya basin. Dogru ise d ye basin :")
            sayac+=1
            continue
        elif buyukmu == "+":
            sayi = random.randint(sayi, 100)
            #kullanici + girerse yani aklimdaki sayi daha buyuk derse,onceki rastgele sayi ile 100 arasinda yeni bir sayi olusturuyoruz
            print("Tahmin ettiginiz sayi bu mu ? {} ".format(sayi))
            buyukmu = input("Tahmin ettiginiz sayi daha kucuk ise - daha buyuk ise + ya basin. Dogru ise d ye basin :")
            sayac+=1
            continue
        elif buyukmu=="d":
            #kullanicinin aklindaki sayiyi bulursak programdan cikiliyor
            print("Tahmin ettiginiz sayiyi {}. denemede bildim..".format(sayac))
            break
else:
    print("Oyundan cikiliyor.. Gule gule..")



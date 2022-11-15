# isim=input("isminizi Giriniz")
# yas=int(input("Yaşınızı Giriniz"))

# if isim =="HALİL" :
#     print("Merhaba Halil")
# elif yas < 12:
#     print("Sen Halit Değilsin")
# elif yas > 80:
#     print("Burda Ne İşin Var Moruk")    




# sayi=int(input("Lütfen Bir Sayı Giriniz"))
# islem=(sayi%2)

# if islem==0:
#    print("Seçilen Sayı Çift Sayıdır")

# elif islem  !=0 :
#     print("Seçilen Sayı Tek Sayıdır")




# harf=str(input("Lütfen Alfabeden Bir Harf Giriniz"))

# if harf ==("a" or "e" or "i" or "u") :
#     print("Girdiğiniz harf olan", harf, "sesli harfdir")
# elif harf !=("a" or "e" or "i" or "u")  :
#     print("Girdiğiniz harf olan", harf, "sessiz harfdir")    




aylar=str(input("Bir Ay Giriniz"))

if aylar ==(("Ocak" or "ocak") or "Mart" or "mart" or "Mayıs" or "mayıs" or "Temmuz" or "temmuz" or "Ağustos" or"ağustos" or "Ekim" or "ekim" or "Aralık" or "aralık"):        
   print("31 gündür")
elif aylar==("Şubat" and "şubat"):
    print("29 gündür")
else:
    print("30 gündür")    

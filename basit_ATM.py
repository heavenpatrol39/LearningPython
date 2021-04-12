# Basit ATM Ugulaması
# Sisteme şifre ile giriş yapılmaktadır. 
# Sistem şifresi = 8888
# Banka müşterisi bakiyesini görebilir.
# Para yatırma ve para çekme işlemi yapabilir.

import time # kurgumuzu daha gerçekçi kılmak sistemi beklemeye almak için time modülünü ekliyoruz.

sifre = ("8888") # şifrenin tupple da değilde veri tabanından geldiğini düşünelim.
bakiye = 0


mSifresi = input("Lütfen şifenizi girin.. : ") # Kullanıcı şifresi kontrol edilmek için mSifresi değişkenine alınır.


while True: # kullanıcı dönggüden çıkmak istemediği sürece devam edecektir.
   
    if mSifresi == sifre: #kullanıcı kontrolü
        print("Giiş Başarılı \nYönlendiriliyorsunuz...")
        time.sleep(1)
        print(f"Güncel Bakiyeniz :{bakiye}")
        
        islem = input("lütfen bir işlem seçin : \n(0) Çıkış \n(1) Para Yatırma \n(2) Para Çekme : \n") # İşlem menüsü
        if islem == "0":
            print("Sistemden Çıkışınız Gerçekleşiyor...")
            time.sleep(1)
            print("İyi Günler Dileriz..")
            break # Döngüyü sonlandırmak için

        elif islem == "1": # Hesaba para yatırma
            try:
                yatirilmakIstenen = int(input("Hesabınıza yatırmak istediğiniz miktar :"))
                bakiye += yatirilmakIstenen
                time.sleep(1)
                print(f"Güncel Bakiyeniz :{bakiye}")
            except ValueError:
                input("Yatırmak istediğiniz miktarı rakam ile giriniz : ")
                
        elif islem =="2": # Hesaptan para Çekme
            
            try:   # int değer kontrolü
                cekilmekIstenen = int(input("Hesabınıdan çekmek istediğiniz miktar :"))
                if cekilmekIstenen > bakiye:
                    input("hesabınızda olan miktardan daha fazlasını çekemezsiniz. \nYeni çekmek istediğiniz miktarı girin.. : ")
                    
                else: 
                    bakiye -= cekilmekIstenen
                    time.sleep(1)
                    print(f"Güncel Bakiyeniz :{bakiye}")
                    
            except ValueError: # int değer hatası
                input("Yatırmak istediğiniz miktarı rakam ile giriniz : ")
                
    else: # Hatalı şifre mesejı
        print("Yanlış şifre girdiniz.")
        mSifresi = input("Lütfen şifenizi girin.. : ")



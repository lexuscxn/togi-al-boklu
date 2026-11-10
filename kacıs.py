print("KAÇIŞ ODASI")
print("Bir odada kilitli kaldın. Kapıdan çıkmanın yolunu bul!")

anahtar = False
sifre_bilgisi = False
fener = False
harita = False
iksir = False
sandik_acildi = False
canavar_dost = False

oyun = True

while oyun:
    print("\nBulunduğun yerdesin. Etrafında üç kapı var:")
    print("1- Sol kapı (Çalışma odası)")
    print("2- Orta kapı (Ana çıkış kapısı)")
    print("3- Sağ kapı (Karanlık tünel)")
    print("4- Envantere bak")
    print("5- Oyundan çık")

    secim = input("Ne yapmak istiyorsun? (1-5): ")

    if secim == "1":
        print("\nSol kapıdan çalışma odasına girdin.")
        
        oda1 = True
        while oda1:
            print("\nÇalışma odasındasın:")
            print("1- Masanın çekmecesine bak")
            print("2- Kitaplığı incele")
            print("3- Dolaba bak")
            print("4- Sandığı açmayı dene")
            print("5- Geri dön")

            s1 = input("Seçimin: ")

            if s1 == "1":
                if not anahtar:
                    print("Çekmeceden paslı bir anahtar çıktı.")
                    anahtar = True
                else:
                    print("Çekmece boş.")

            elif s1 == "2":
                if not harita:
                    print("Kitapların arasında eski bir harita buldun.")
                    harita = True
                else:
                    print("Başka kitap yok.")

            elif s1 == "3":
                if not fener:
                    print("Dolapta el feneri buldun.")
                    fener = True
                else:
                    print("Dolap boş.")

            elif s1 == "4":
                if sandik_acildi:
                    print("Sandık zaten açık.")
                elif anahtar:
                    print("Anahtarla sandığı açtın, içinden şifre çıktı: 246")
                    sifre_bilgisi = True
                    sandik_acildi = True
                else:
                    print("Sandık kilitli, anahtar lazım.")

            elif s1 == "5":
                print("Çalışma odasından çıktın.")
                oda1 = False
            else:
                print("Yanlış tuş.")

    elif secim == "2":
        print("\nOrta kapının önüne geldin.")
        
        oda2 = True
        while oda2:
            print("\nÇıkış kapısındasın:")
            print("1- Şifreyi gir")
            print("2- Anahtarı dene")
            print("3- Geri dön")

            s2 = input("Seçimin: ")

            if s2 == "1":
                tahmin = input("Şifreyi yaz: ")
                if tahmin == "246" and sandik_acildi:
                    print("Kapı açıldı! Başarıyla kaçtın!")
                    oyun = False
                    oda2 = False
                elif tahmin == "010101":
                    print("Gizli geçit açıldı, kaçtın!")
                    oyun = False
                    oda2 = False
                else:
                    print("Yanlış şifre!")

            elif s2 == "2":
                if anahtar:
                    print("Anahtar buradaki kilide uymuyor.")
                else:
                    print("Anahtarın yok.")

            elif s2 == "3":
                print("Geri döndün.")
                oda2 = False
            else:
                print("Yanlış tuş.")

    elif secim == "3":
        print("\nSağ kapıdan karanlık bir yere girdin.")
        
        oda3 = True
        while oda3:
            print("\nTüneldesin:")
            print("1- İlerlemeye çalış")
            print("2- Geri dön")

            s3 = input("Seçimin: ")

            if s3 == "1":
                if not fener:
                    print("Çok karanlık! Ayağın takıldı ve bir iksir buldun.")
                    iksir = True
                else:
                    print("Fenerle ilerledin, karşına canavar çıktı.")
                    cevap = input("Canavar bilmece sordu (Gündüz kaybolan şey?): ").lower()
                    if cevap == "yıldız" or cevap == "yildiz":
                        print("Canavar geçmene izin verdi. Kod: 010101")
                        sifre_bilgisi = True
                    else:
                        print("Canavar seni korkuttu, geri kaçtın.")

            elif s3 == "2":
                print("Geri döndün.")
                oda3 = False
            else:
                print("Yanlış tuş.")

    elif secim == "4":
        print("\n--- Envanter ---")
        print("Anahtar:", anahtar)
        print("Fener:", fener)
        print("Harita:", harita)
        print("İksir:", iksir)
        print("Şifre bilgisi:", sifre_bilgisi)

    elif secim == "5":
        print("Oyundan çıkıldı.")
        oyun = False

    else:
        print("Geçersiz seçim.")
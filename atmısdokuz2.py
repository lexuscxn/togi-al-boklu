diploma = input("Üniversite diplomasına sahip misiniz? (Evet/Hayır olarak cevaplayınız.): ")
dil = input("İngilizce biliyor musunuz? (Evet/Hayır olarak cevaplayınız.): ")

if diploma == "Evet" and dil == "Evet":
    print("Mülakata girmeye hak kazandınız.")
else:
    print("Üzgünüz, bu iş için uygun değilsiniz.")
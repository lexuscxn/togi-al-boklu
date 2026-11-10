sicaklik = int(input("Lütfen hava sıcaklığını giriniz: "))

if sicaklik <= 0:
    print("Bugün hava çok soğuk.")

if sicaklik > 0 and sicaklik < 20:
    print("Bugün hava ılık.")

if sicaklik >= 20:
    print("Bugün hava sıcak.")
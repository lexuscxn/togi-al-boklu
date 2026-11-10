print("Basit Hesap Makinesi")

sayi1 = float(input("birinci sayıyı giriniz:"))
islem = input("işlem seçin (+, -, *, /): ")
sayi2 = float(input("ikinci sayıyı giriniz:"))

if islem == "+":
    sonuc = sayi1 + sayi2
elif islem == "-":
    sonuc = sayi1 - sayi2
elif islem == "*":
    sonuc = sayi1 * sayi2
elif islem == "/":
    if sayi2 != 0:
        print("Bir sayı sıfıra bölünemez!")
    else:
        sonuc = sayi1 / sayi2
else:
    print("Gecersiz işlem girdin")

if islem in ("+", "-", "*") or (islem == "/" and sayi2 != 0):
    print("Sonuç:", sonuc)
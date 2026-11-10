import random


print("tas-kagıt-makas oyunu")
oyuncu=input("tahmin giriniz:")
bilgisayar="taş"

if bilgisayar==oyuncu:
    print("berabere")
if bilgisayar=="taş" and oyuncu=="kagıt":
    print("oyuncu kazandı")
if bilgisayar=="taş" and oyuncu=="makas":
    print("bilgisayar kazandı")
if bilgisayar=="makas" and oyuncu=="kagıt":
    print("oyuncu kazandı")
if bilgisayar=="makas" and oyuncu=="taş":
    print("bilgisayar kazandı")
if bilgisayar=="kagıt" and oyuncu=="makas":
    print("bilgisayar kazandı")
if bilgisayar=="kagıt" and oyuncu=="taş":
    print("oyuncu kazandı")
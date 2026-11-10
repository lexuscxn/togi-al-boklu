print("merhaba kozmos resturantina hosgeldiniz")

name = input("lutfen adinizi giriniz: ")
lastname = input ("lutfen soyadinizi giriniz: ")
print(f"hosgeldiniz {name} {lastname}!")
print("\nlutfen menuden yemek seciniz: ")
print("\n1. pizza 165tl")
print("2. hamburger 200tl")
print("3. salata 100tl")
print("4.siparisi tamamla")

sum = 0 
while True:
    choice = input("\nseciminizi yapiniz (1-4): ")
    if choice =="1":
        print("\npizza sepete eklendi.")
        sum = sum + 165
    elif choice == "2":
        print("\nhamburger sepete eklendi.")
        sum = sum + 200
    elif choice == "3":
        print("\nsalata sepete eklendi.")
        sum = sum + 100
    elif choice == "4":
        print("\nislemi tamamla.")
        break

print(f"\ntoplam tutar: {sum}tl")
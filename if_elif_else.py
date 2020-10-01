# IF elif else
print("""
iSLEM SECIN
1. TOPLAMA
2. CIKARMA
3. CARPMA
4. BOLME
""")
# kullanicidan 2 sayi aliyoruz
islem=int(input("Bir islem seciniz: "))
sayi1=int(input("1-ci sayiyi girin: "))
sayi2=int(input("2-ci sayiyi girin: "))

if islem==1: # eger islem 1-e esitse
    print(sayi1+sayi2) # iki sayiyi topla
elif islem==2: # islem 2 ise
    print(sayi1-sayi2) # sayilari cikar
elif islem==3: # islem 3 ise
    print(sayi1*sayi2) # sayilari carp
elif islem==4: # islem 4 ise
    print(sayi1/sayi2) # sayilari bol
else: # hicbiri degilse
    print("Gecersiz islem") # ekrana bu basilacak



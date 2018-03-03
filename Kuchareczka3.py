#Kalkulator kucharza
#import
import tkinter as tk

#powitanie
print("Witaj Kuchareczko")

#definicje
i=1
mieszanka = []
ingrd = []
masa = []

#skrypt start
sklad = input("Wpisz pierwszy składnik: ")
ilosc = input("Wpisz ilosc pierwszego składnika (w ml): ")
mieszanka.append(sklad)
mieszanka.append(ilosc)
ingrd.append(sklad)
masa.append(int(ilosc))
print(mieszanka)
pytanie = input("Czy chcesz dodać kolejny składnik? (T/N)")
while pytanie in ["t" , "T"]:
    sklad = input("Wpisz kolejny składnik: ")
    if sklad in ["białka" , "białko"]:
        ilosc = input("Wpisz ilosc jajek: ")
        mieszanka.append(sklad)
        mieszanka.append(ilosc)
        ingrd.append(sklad)
        masa.append(int(ilosc)*25)
        print(mieszanka)
        pytanie = input("Czy chcesz dodać kolejny składnik? (T/N)")
    elif sklad in ["żółtka", "żółtko"]:
        ilosc = input("Wpisz ilosc jajek: ")
        mieszanka.append(sklad)
        mieszanka.append(ilosc)
        ingrd.append(sklad)
        masa.append(int(ilosc)*20)
        print(mieszanka)
        pytanie = input("Czy chcesz dodać kolejny składnik? (T/N)")
    elif sklad in ["jajka", "jajko"]:
        ilosc = input("Wpisz ilosc jajek: ")
        mieszanka.append(sklad)
        mieszanka.append(ilosc)
        ingrd.append(sklad)
        masa.append(int(ilosc)*45)
        print(mieszanka)
        pytanie = input("Czy chcesz dodać kolejny składnik? (T/N)")
    else:
        ilosc = input("Wpisz ilosc składnika (w ml): ")
        mieszanka.append(sklad)
        mieszanka.append(ilosc)
        ingrd.append(sklad)
        masa.append(int(ilosc))
        print(mieszanka)
        pytanie = input("Czy chcesz dodać kolejny składnik? (T/N)")

else:
    print(mieszanka)
    masa2 = input("Wpisz docelową objętość masy (w ml): ")
    masa_sum = sum(masa)
    prop = int(masa2)/masa_sum

print(prop)
masa_end = [i * prop for i in masa]
for i in masa_end:
    print(round(i))
    print(ingrd[masa_end.index(i)])

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
sklad = input("Wpisz kolejny składnik (lub 'koniec' aby zakończyć dodawnie): ")
dodawanie=1
while dodawanie == 1:
    if sklad in ["białka" , "białko"]:
        ilosc = input("Wpisz ilosc jajek: ")
        mieszanka.append(sklad)
        mieszanka.append(ilosc)
        ingrd.append(sklad)
        masa.append(int(ilosc)*25)
        print(mieszanka)
        sklad = input("Wpisz kolejny składnik (lub 'koniec' aby zakończyć dodawnie): ")
    elif sklad in ["żółtka", "żółtko"]:
        ilosc = input("Wpisz ilosc jajek: ")
        mieszanka.append(sklad)
        mieszanka.append(ilosc)
        ingrd.append(sklad)
        masa.append(int(ilosc)*20)
        print(mieszanka)
        sklad = input("Wpisz kolejny składnik (lub 'koniec' aby zakończyć dodawnie): ")
    elif sklad in ["jajka", "jajko"]:
        ilosc = input("Wpisz ilosc jajek: ")
        mieszanka.append(sklad)
        mieszanka.append(ilosc)
        ingrd.append(sklad)
        masa.append(int(ilosc)*45)
        print(mieszanka)
        sklad = input("Wpisz kolejny składnik (lub 'koniec' aby zakończyć dodawnie): ")
    elif sklad in ["koniec"]:
        print(mieszanka)
        dodawanie = 0
        masa2 = input("Wpisz docelową objętość masy (w ml): ")
    else:
        ilosc = input("Wpisz ilosc składnika (w ml): ")
        mieszanka.append(sklad)
        mieszanka.append(ilosc)
        ingrd.append(sklad)
        masa.append(int(ilosc))
        print(mieszanka)
        sklad = input("Wpisz kolejny składnik (lub 'koniec' aby zakończyć dodawnie): ")
masa_sum = sum(masa)
prop = int(masa2)/masa_sum

print(prop)
masa_end = [i * prop for i in masa]
for i in masa_end:
    if ingrd[masa_end.index(i)] in ["jajko", "jajka"]:
        print(round(i)/45)
        print(ingrd[masa_end.index(i)])
    elif ingrd[masa_end.index(i)] in ["żółtka", "żółtko"]:
        print(round(i)/20)
        print(ingrd[masa_end.index(i)])
    elif ingrd[masa_end.index(i)] in ["białka" , "białko"]:
        print(round(i)/25)
        print(ingrd[masa_end.index(i)])
    else:
        print(round(i))
        print(ingrd[masa_end.index(i)])

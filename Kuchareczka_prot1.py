#Kalkulator kucharza
import tkinter as tk
print("Witaj Kuchareczko")
#def pytanie as
 #   input("Czy chcesz dodać kolejny składnik? (T/N)")

#def zmienna as
    
var1 = input("Składnik 1 (w ml): ")
#return pytanie
#if pytanie == "T" or "t"
#   
var2 = input("Składnik 2 (w ml): ")
var3 = input("Składnik 3 (w ml): ")

suma1 = int(var1) + int(var2) + int(var3)
print("Całkowita suma masy: %d" % suma1)
suma2 = input("Podaj żądaną ilość masy (w ml): ")
prop = int(suma2)/suma1
print (prop)
var21 = round(int(var1) * prop)
var22 = round(int(var2) * prop)
var23 = round(int(var3) * prop)
print("Potrzebujesz %d składnik1, %d składnik2 oraz %d składnik3" % (int(var21), int(var22), int(var23)))

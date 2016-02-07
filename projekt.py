#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 16:55:38 2016

@author: Kasia Dziegiel, Magda Szpor, Agnieszka Szymczuk
"""
#IMPORTUJEMY BIBLIOTEKI: DO OBLICZEN NUMERYCZNYCH, DO RYSOWANIA ORAZ DO ANALIZY OBRAZU
import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import match_template
#from imread import imread, imsave
from skimage.color import rgb2gray
from skimage.data import imread

#WCZYTYWANIE OBRAZKOW, KTORE BEDZIEMY ODCZYTYWAC
#PRZEKONWERTOWUJEMY OBRAZKI Z KOLOROWYCH NA CZARNOBIALE I ODWRACAMY(TWORZYMY NEGATYW) 
image_khufu = rgb2gray(np.invert(imread('chufu.jpg')))
image_kliopatra = rgb2gray(np.invert(imread('kleopatra.jpg')))
image_ptolemeus = rgb2gray(np.invert(imread('ptolemeusz.jpg')))
#WCZYTYWANIE WZORCOW - LITERY EGIPSKIE
wzor_u = rgb2gray(np.invert(imread('wzorzec_u.JPG')))
wzor_kh = rgb2gray(np.invert(imread('wzorzec_kh.JPG')))
wzor_f = rgb2gray(np.invert(imread('wzorzec_f.JPG')))

wzor_a = rgb2gray(np.invert(imread('wzorzec_a.JPG')))
wzor_i = rgb2gray(np.invert(imread('wzorzec_i.JPG')))
wzor_k = rgb2gray(np.invert(imread('wzorzec_k.JPG')))
wzor_l = rgb2gray(np.invert(imread('wzorzec_l.JPG')))
wzor_m = rgb2gray(np.invert(imread('wzorzec_m.JPG')))
wzor_o = rgb2gray(np.invert(imread('wzorzec_o.JPG')))
wzor_p = rgb2gray(np.invert(imread('wzorzec_p.JPG')))
wzor_r = rgb2gray(np.invert(imread('wzorzec_r.JPG')))

wzor_s = rgb2gray(np.invert(imread('wzorzec_s.JPG')))
wzor_t = rgb2gray(np.invert(imread('wzorzec_t.JPG')))

#LISTA POMOCNICZA W KTOREJ PRZETRZYMYWAC BEDZIEMY ZNALEZIONE HIEROGLIFY/LITERY WRAZ Z ICH POZYCJAMI
slowo=[]
#SLOWNIK EGIPSKO-POLSKI 
slowniczek={'khufu':"Cheops" , 'ptolmiis':"Ptolemeusz", 'kliopatra':"Kleopatra"}

#FUNKCJA PRZESZUKUJACA OBRAZ. NALEZY PODAC JEJ WZORZEC, OBRAZ NA KTORYM BEDZIE SZUKAC, TOLERANCJE Z PRZEDZIALU OD ZERA DO 1
def wykrywacz(image_wzor,image_obraz,tolerancja,litera_egipska):
    #Tworzenie okienka do wyswietlania wzorca i obrazow na nim odnalezionych  
    fig = plt.figure(figsize=(12, 5))
    #Podzial okienka  na dwa obszary   
    ax1 = plt.subplot(1, 2, 1)
    ax2 = plt.subplot(1, 2, 2)
    
    #Result to wynik operacji porownywania wzorca z podstawowym obrazem, jego wynikiem jest lista, w ktorej znajduje sie wspolczynnik korelacji dla poszczegolnych pikseli obrazu podstawowego
    result= match_template(image_obraz, image_wzor)
    #Pomocnicza zmienna w ktorej przechowywana bedzie kopia result, na ktorej bedziemy operowac    
    result2=result
    #wysokosc i szerokosc wzoru    
    hwzor, wwzor = image_wzor.shape
    #lista w ktorej  bedziemy zapisywac znalezione hieroglify    
    literka=[]
    #listy, w ktorej zapisywac bedziemy wspolrzedne znalezionych hieroglifow
    x1=[]
    y1=[]
    #Indeks elementu listy result2, ktory posiada najwyzsza wartosc korelacji(czyli jest najbardziej prawdopodobne ze w tym miejscu znajduje sie hieroglif)
    ij=np.unravel_index(np.argmax(result2), result.shape)
    #pobranie skladowych indeksu i odwrocenie ich kolejnosci
    x, y= ij[::-1]        
    #dodanie do list wspolrzednych indeksu najwyzszej wartosci result   
    x1.append(x)
    y1.append(y)
    #do listy literka dodajemy wartosc wspolrzednej x (by pozniej posortowac odpowienio hieroglify), literke oraz informacyjnie wartosc w result 
    literka.append([x , litera_egipska,np.max(result2)])
    #zerujemy najwieksza wartosc  w result by znalezc kolejna najwieksza wartosc w innymm miejscu
    result2[ij]=0    
    #na wszelki wypadek gdyby najwyzsza wartosc okazala sie byc w poblizu starej wartosci, zerujemy rowniez elementy obok
    result2[(y,x-1)]=0
    result2[(y,x+1)]=0    

    i = 0
    #w pierwszej czesci okienka bedziemy pokazywac wzor    
    ax1.imshow(image_wzor)
    ax1.set_axis_off()
    ax1.set_title('template')
    #w drugiej czesci okienka bedziemy pokazywac obraz, na ktorym szukami wzoru
    ax2.imshow(image_obraz)
    ax2.set_axis_off()
    ax2.set_title('image')

    #rysujemy prostokat o wymiarach naszego wzoru w miejscu gdzie pojawil sie nasz najbardzije prawdopodobny element
    rect = plt.Rectangle((x, y), wwzor, hwzor, edgecolor='r', facecolor='none')
    ax2.add_patch(rect)
    #Tworzymy nowe okienko, w ktorym wyswietlimy 'result' czyli wynik porownywania
    fig, ax = plt.subplots(figsize=(12,1))
    ax.imshow(result)
    plt.show()
    
    #Petla, w ktorej bedziemy powtarzac wszystkie powyzsze operacje az do momentu w ktorym wspolczynnik korelacji bedzie nizszy niz nasza tolerancja
    while (np.max(result2) > tolerancja):
        ij=np.unravel_index(np.argmax(result2), result.shape)
        x, y= ij[::-1]
        x1.append(x)
        y1.append(y)
        
        literka.append([x , litera_egipska,np.max(result2)])
        
        result2[ij]=0

        result2[(y,x-1)]=0
        result2[(y,x+1)]=0    

 
        i=i+1
        rect = plt.Rectangle((x1[i], y1[i]), wwzor, hwzor, edgecolor='r', facecolor='none')
        ax2.add_patch(rect)
    #po wyjsciu z petli wszystkie zebrane elementy w liscie literka przypisujemy do globalnej listy slowo    
    slowo.extend(literka)
    
#PROGRAM GLOWNY
#Wywolywanie funkcji dla odpowiednich obrazow i wzorow
#Nalezy odkomentowac odpowiednie czesci 

#--------------------------------------------------------

##CHEOPS
#
p=wykrywacz(wzor_u, image_khufu, 0.87, 'u')
p2=wykrywacz(wzor_kh, image_khufu, 0.99, 'kh')
p3=wykrywacz(wzor_f, image_khufu, 0.95, 'f')

#--------------------------------------------------------

##KLEOPATRA

#p4=wykrywacz(wzor_a, image_kliopatra, 0.92, 'a')
#p5=wykrywacz(wzor_i, image_kliopatra, 0.95, 'i')
#p6=wykrywacz(wzor_k, image_kliopatra, 0.99, 'k')
#p7=wykrywacz(wzor_l, image_kliopatra, 0.99, 'l')
#p8=wykrywacz(wzor_t, image_kliopatra, 0.97, 't')
#p9=wykrywacz(wzor_o, image_kliopatra, 0.95, 'o')
#p10=wykrywacz(wzor_p, image_kliopatra, 0.95, 'p')
#p11=wykrywacz(wzor_r, image_kliopatra, 0.95, 'r')

#--------------------------------------------------------

###PROMETEUSZ
#
#p12=wykrywacz(wzor_p, image_ptolemeus, 0.98, 'p')
#p13=wykrywacz(wzor_s, image_ptolemeus, 0.98, 's')
#p14=wykrywacz(wzor_t, image_ptolemeus, 0.98, 't')
#p15=wykrywacz(wzor_o, image_ptolemeus, 0.95, 'o')
#p16=wykrywacz(wzor_l, image_ptolemeus, 0.95, 'l')
#p17=wykrywacz(wzor_m, image_ptolemeus, 0.97, 'm')
#p17=wykrywacz(wzor_i, image_ptolemeus, 0.845, 'i')

print("")
print("Znalezione:")
print(slowo)
print("")
#Sortowanie listy - domyslnie sortowanie przechodzi po wspolrzednych x
slowo.sort()

literki=[]
#Z posortowanej listy slowo wyciagamy element odpowiadajacy literze alfabetu ktorej odpowiada hieroglif
for i in range(len(slowo)):
    literki.append(slowo[i][1])
print(" ")
print("Znalezione literki (PO SORTOWANIU) :")
print(literki)

print(" ")
#laczenie elementow listy w wyraz
slowko= '' .join(literki)
print("Po egipsku:")
print(slowko)
print(" ")
print("Po polsku:")
#tlumaczenie ze slownika slowniczek
print(slowniczek[slowko])

plt.show()

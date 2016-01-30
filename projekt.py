# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 16:55:38 2016

@author: kasia dziegiel, magda szpor, agnieszka szymczuk
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import match_template
#from imread import imread, imsave
from skimage.color import rgb2gray
from skimage.data import imread

#WCZYTYWANIE OBRAZKA
image_khufu = rgb2gray(np.invert(imread('chufu.jpg')))
image_kliopatra = rgb2gray(np.invert(imread('kleopatra.jpg')))
image_ptolemeus = rgb2gray(np.invert(imread('ptolemeusz.jpg')))
#WCZYTYWANIE WZORU
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


slowo=[]
slowniczek={'khufu':"Cheops" , 'ptolmiis':"Ptolemeusz", 'kliopatra':"Kleopatra"}

def wykrywacz(image_wzor,image_obraz,tolerancja,litera_egipska):
    fig = plt.figure(figsize=(12, 5))
    ax1 = plt.subplot(1, 2, 1)
    ax2 = plt.subplot(1, 2, 2)
    
    result= match_template(image_obraz, image_wzor)
    result2=result
    hwzor, wwzor = image_wzor.shape
    literka=[]
    x1=[]
    y1=[]
    ij=np.unravel_index(np.argmax(result2), result.shape)
    prog=np.argmin(result2)+tolerancja
    x, y= ij[::-1]        
    x1.append(x)
    y1.append(y)
    literka.append([x , litera_egipska,np.argmax(result2), np.argmin(result2)])
    result2[ij]=0    

    result2[(0,x-1)]=0
    result2[(0,x+1)]=0
    
#    result2[(1,x)]=0
#    result2[(1,x+1)]=0
#
#    result2[(0,x-2)]=0
#    result2[(0,x+2)]=0  
    
    i = 0
    ax1.imshow(image_wzor)
    ax1.set_axis_off()
    ax1.set_title('template')
    
    ax2.imshow(image_obraz)
    ax2.set_axis_off()
    ax2.set_title('image')
    rect = plt.Rectangle((x, y), wwzor, hwzor, edgecolor='r', facecolor='none')
    ax2.add_patch(rect)
    fig, ax = plt.subplots(figsize=(12,1))
    ax.imshow(result)
    plt.show()
    
    while (np.argmax(result2) > prog):
        ij=np.unravel_index(np.argmax(result2), result.shape)
        x, y= ij[::-1]
        x1.append(x)
        y1.append(y)
        
        literka.append([x , litera_egipska,np.argmax(result2), np.argmin(result2)])
        
        result2[ij]=0
        result2[(0,x-1)]=0
        result2[(0,x+1)]=0 
        
#        result2[(1,x)]=0
#        result2[(1,x-1)]=0
#        result2[(1,x+1)]=0
#         
#        result2[(0,x-2)]=0
#        result2[(0,x+2)]=0  


 
        i=i+1
        rect = plt.Rectangle((x1[i], y1[i]), wwzor, hwzor, edgecolor='r', facecolor='none')
        ax2.add_patch(rect)
        
    slowo.extend(literka)
    
#PROGRAM GLOWNY

##CHEOPS
#p=wykrywacz(wzor_u, image_khufu, 200, 'u')
#p2=wykrywacz(wzor_kh, image_khufu, 20, 'kh')
#p3=wykrywacz(wzor_f, image_khufu, 8000, 'f')

#KLEOPATRA
p4=wykrywacz(wzor_a, image_kliopatra, -47000, 'a')
p5=wykrywacz(wzor_i, image_kliopatra, 55000, 'i')
p6=wykrywacz(wzor_k, image_kliopatra, 80000, 'k')
p7=wykrywacz(wzor_l, image_kliopatra, 8000, 'l')
p8=wykrywacz(wzor_t, image_kliopatra, 80000, 't')
p9=wykrywacz(wzor_o, image_kliopatra, 80000, 'o')
p10=wykrywacz(wzor_p, image_kliopatra, 200000, 'p')
p11=wykrywacz(wzor_r, image_kliopatra, 80000, 'r')

###PROMETEUSZ
#p12=wykrywacz(wzor_p, image_ptolemeus, 200000, 'p')
#p13=wykrywacz(wzor_s, image_ptolemeus, 200000, 's')
#p14=wykrywacz(wzor_t, image_ptolemeus, 80000, 't')
#p15=wykrywacz(wzor_o, image_ptolemeus, 80000, 'o')
#p16=wykrywacz(wzor_l, image_ptolemeus, 8000, 'l')
#p17=wykrywacz(wzor_m, image_ptolemeus, 2000, 'm')
#p17=wykrywacz(wzor_i, image_ptolemeus, 41000, 'i')

print("")
print("Znalezione:")
print(slowo)
print("")
slowo.sort()

literki=[]

for i in range(len(slowo)):
    literki.append(slowo[i][1])
print(" ")
print("Znalezione literki (PO SORTOWANIU) :")
print(literki)

print(" ")

slowko= '' .join(literki)
print("Po egipsku:")
print(slowko)
print(" ")
print("Po polsku:")
print(slowniczek[slowko])

plt.show()

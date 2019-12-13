# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 10:30:00 2019

@author: Милена Владимировна
"""

""
import matplotlib.pyplot as plt
from skimage  import measure
import numpy as np
from scipy.ndimage  import binary_dilation
from skimage.filters  import threshold_otsu
from skimage.measure  import label, regionprops

#считаем буквы с отверстиями, О и 8
def count_holes(symbol):
#   hasattr проверяет есть ли такой арибут у объекта и возвращает правда или ложь
    if hasattr(symbol, "image"):
        image=symbol.image
    else:
        image=symbol
    image=~image
    zones=np.ones((image.shape[0]+2,image.shape[1]+2))
#    достраивает края 1ками 
    zones[1:-1,1:-1]=image
    zl=label(zones)
#    print("Hotes:",np.max(zl)-1)
    return  np.max(zl)-1

#определим по площаи внутренних дырок
def is_D_or_P(symbol):
#   hasattr проверяет есть ли такой арибут у объекта и возвращает правда или ложь
    if hasattr(symbol, "image"):
        image=symbol.image
    else:
        image=symbol
    image=~image
    zones=np.ones((image.shape[0]+2,image.shape[1]+2))
    
#    достраивает края 1ками 
    zones[1:-1,1:-1]=image
    zl=label(zones)
    flag=0
    for xarea in (regionprops(zl)):
        if flag==1:
            result_area=xarea.bbox_area
#           P
            if (50 < result_area < 80):
                return 1
#           D
            elif(170 < result_area < 200):
                return 2   
        flag+=1
    return 0



#заливы
def count_bays(symbol):
    image=symbol.image
    zones=np.ones((image.shape[0]+2,image.shape[1]+2))
#    достраивает края 1ками 
    zones[1:-1,1:-1]=image
    
#считаем вертикальные палочки        
def has_vline(symbol):
    image=symbol.image
#    инвертируем
    holes =~image.copy()
    lb=label(holes)
    return np.max(lb)


def is_D(symbol):
#    print(symbol.bbox_area , symbol.label)
    return 1



def is_A(symbol):
    image = symbol.image
    zones = image.copy()
    zones[-1,:]=1
    holes=count_holes(zones)
#    если две дырки,то возврашаем истину
    return holes==2

def recognize(symbol):
    holes=count_holes(symbol)
    if holes==2:
        if has_vline(symbol):
            return "B"
        else:
            return "8"
    elif holes == 1:
        if has_vline(symbol):
            result=is_D_or_P(symbol)
            if (result==1):
                return "P"
            elif (result==2):
                return "D"
        elif is_A(symbol):
            return "A"
        else:
            return "0"
    elif holes == 0:
        if  np.all(symbol.image):
            return "-"
        elif has_vline(symbol):
            return "1"
        else:
            bays=count_bays(symbol)
            if bays == 4 :
                return "X"
            elif bays == 5:
                return "W"     
            else:
                arr = symbol.image
                ratio = arr.shape[0] / arr.shape[1]
                if 0.8 < ratio<1.2:
                    return "*"
                elif 1.6 < ratio <2.2:
                    return "/"
        return ""
        
               

img=plt.imread("D:\\ИГУ\\3курс\\Компьютерное зрение\\big_alphabet.png")


gray=np.average(img,2)
gray[gray>0]=1
gray=gray.astype("uint8")

#thresh=threshold_otsu(gray)
#img=gray<thresh

#img=binary_dilation(img, iterations=2)

lb=label(gray)
total=np.max(lb)
print("All:", lb.max())

symbols=regionprops(lb)

recon={"":0}

for symbol in symbols:
    sym=recognize(symbol)
    if sym not in recon:
        recon[sym]=1
# встретили первый раз ,тогда добавляем в словарик
    else:
        recon[sym]+=1
print("Recognition rate: {}".format((total-recon[""])/total))

plt.figure()
plt.imshow(lb)   
plt.show()

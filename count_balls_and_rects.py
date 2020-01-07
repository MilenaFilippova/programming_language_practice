#Определить сколько фигур каждого цвета имеется на изображении. Программа должна выдавать общее количество фигур на изображении 
#и отдельно для прямоугольников и кругов количество по цвету.

import matplotlib.pyplot as plt
import numpy as np
import math
from skimage import filters
from skimage.measure  import label, regionprops
from skimage import color




image=plt.imread("D:\\ИГУ\\3курс\\Компьютерное зрение\\balls_and_rects.png")
#переводим rgb в hsv(за цвет отвечает одно число,а не три)
image = color.rgb2hsv(image)[:,:,0]
uniq = np.unique(image)
uniq=uniq*10
#округляем уникальные значения с помощью ceil
#uniq = mat.ceil(uniq)
uniq = np.ceil(uniq)
#получаем количство цветов объединяя значения по группам
uniq = np.unique(uniq)
#uniq=uniq.astype("uint32")
print("unique values of  colors: " + str(uniq))

image2=image * 10
image2=np.ceil(image2)


#сделаем словари и в каждом будем считать цвета для отдельных фигур
count_circle_colors = {}
count_rect_colors = {}
count_all_figures=0
k = 0
for color in uniq:
    image3 = image2.copy()
    image3[image3 != color] = 0
    count_circle_colors[str(k)] = 0
    count_rect_colors[str(k)] = 0
   
    
    LB = label(image3)
    figures = regionprops(LB)
    for obj in figures:
#        print (obj.image)
#        если все True, считаем фигуру такого цвета
        if np.all(obj.image):
            count_circle_colors[str(k)] += 1
            count_all_figures+=1
        else:
            count_rect_colors[str(k)] += 1
            count_all_figures+=1
            
    k += 1




print("Circle:" + str(count_circle_colors))
print("Rect:" + str(count_rect_colors))
print("Count all figurs:"+str(count_all_figures))


plt.figure(figsize=(8,8))
plt.plot(uniq,'o')
#plt.imshow(image)
plt.show()

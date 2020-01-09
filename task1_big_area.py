#На изображении (task1.png) найти объект с самой большой внутренней площадью(т.е. площадь без
#учета точек периметра).

import matplotlib.pyplot as plt
import numpy as np
from skimage import filters
from skimage.filters  import threshold_isodata, threshold_otsu
from skimage.measure  import label, regionprops
from skimage import color

image=plt.imread("D:\\ИГУ\\3курс\\Компьютерное зрение\\task1.png")

gray = np.average(image, 2)
thresh1 = threshold_otsu(gray)
thresh2 = threshold_isodata(gray)
temp1 = gray > thresh1
temp2 = gray < thresh2
img = temp1 + temp2
LB=label(img)

objs=regionprops(LB)
max_area_in=0
max_area_all=0
for obj in objs:
    print( str(obj.label) +" "+ str(obj.area))
    area=obj.area-obj.perimeter
    if max_area_in<area:
        max_area_in=area
        max_area_all=obj.area
        

    
print("Max internal area= " + str(max_area_in) + " ; All area of this figure: "+ str(max_area_all))
plt.subplot(121)
plt.imshow(image)

plt.subplot(122)
plt.imshow(LB)
plt.colorbar() 
plt.show()

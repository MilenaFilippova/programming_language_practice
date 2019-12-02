# Применяя операции морфологического анализа и соответствующие структурирующие элементы необходимо определить общее количество объектов на бинарном изображении (ps.npy.txt) 
# и количество объектов для каждого вида по отдельности.

import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import morphology
from scipy.ndimage  import binary_opening
from skimage.measure  import label

image=np.load("D:\\ИГУ\\3курс\\Компьютерное зрение\\ps1.npy.txt")
image = image.astype("uint8")

hor_all = np.array(
   [[1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]])

hor_top = np.array(
   [[1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]])

hor_bottom = np.array(
   [[1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1]])

vert_right = np.array(
   [[1, 1, 1, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [1, 1, 1, 1]])

vert_left = np.array(
    [[1, 1, 1, 1],
     [0, 0, 1, 1],
     [0, 0, 1, 1],
     [0, 0, 1, 1],
     [1, 1, 1, 1]])

    
LB=label(image)
LB_max=LB.max()
print ("Number of objects:" + str(LB_max))

#будем формировать изображения только с одним оъектом
img_hor_all = label(binary_opening(image, hor_all,1))
img_hor_top = label(binary_opening(image, hor_top,1))
img_hor_bottom = label(binary_opening(image, hor_bottom,1))
img_vert_right = label(binary_opening(image, vert_right,1))
img_vert_left = label(binary_opening(image, vert_left,1))


#считаем сколько объектов получилось на каждом изображении
count_hor_all = img_hor_all.max()
#убираем дублирование,чтобы не посчитать объекты с дырками в цельных объектах еще раз
count_hor_top = img_hor_top.max() - count_hor_all 
count_hor_bottom = img_hor_bottom.max() - count_hor_all 
count_vert_right = img_vert_right.max()
count_vert_left  = img_vert_left.max() 


test = LB_max-count_hor_all - count_hor_top - count_hor_bottom - count_vert_right
if count_vert_left == test :
    print("count_hor_all =",count_hor_all, "\ncount_hor_top =", count_hor_top, 
      "\ncount_hor_bottom =", count_hor_bottom, "\ncount_vert_right =",count_vert_right,
      "\ncount_vert_left =", count_vert_left)
else:
    print("Failed to determine. Check your masks")
    

plt.imshow(LB)
plt.colorbar()
plt.show()

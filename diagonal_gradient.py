#Написать программу для генерации двухмерного массива значения которого вычисляются как линейный градиент от одного цвета к другому.
#Градиент должен быть повернут на 45 градусов, т.е. идти из левого верхнего угла в правый нижний.


import matplotlib.pyplot as plt
import numpy as np


size = 100
image = np.zeros((size, size, 3), dtype="uint8")

#два цвета для градиента
left_color = (255, 128, 0)
right_color = (0, 128, 255)


#кол-во цветов больше размера массива,потому что меняется по диагонали
#находим их количество
n = image.shape[0]
k = n * 2 - 1

#распределяем цвета для перелива
R = np.linspace(left_color[0], right_color[0], k, dtype="uint8")
G = np.linspace(left_color[1], right_color[1], k, dtype="uint8")
B = np.linspace(left_color[2], right_color[2], k, dtype="uint8")

#заносим в массив сочитание RGB
all_colors = list(zip(R, G , B))
 
#идем по всему изображению и закрашиваем ячейки
for x in range(n):
    for y in range(n):
        #если сложить индексы ячеек ,то получим необходимый индекс цвета,
        #который должен быть в этой ячейке
        result = x + y
        image[x, y] = all_colors[result]


plt.figure(figsize=(10, 10))
plt.imshow(image)
plt.show()

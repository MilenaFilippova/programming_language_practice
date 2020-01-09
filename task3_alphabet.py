#На изображении (task3.png) определить сколько раз встречается каждый символ.


import numpy as np
import matplotlib.pyplot as plt
from skimage import measure
from skimage.measure import label, regionprops
from scipy.ndimage import morphology
from skimage.filters import threshold_otsu





def count_holes(symbol):
    if hasattr(symbol, "image"):
        image = symbol.image
    else:
        image = symbol
    image = ~image
    zones = np.ones((image.shape[0] + 2,
                    image.shape[1] + 2))
    zones[1:-1, 1:-1] = image
    zl = label(zones)
    return np.max(zl) - 1

def count_bays(symbol):
    image = symbol.image
    zones = ~image.copy()
    zl = label(zones)
    return np.max(zl)

def has_vline(symbol):
    image = symbol.image
    lines = np.sum(image, 0) // image.shape[0]
    return 1 in lines

def is_L(symbol):
    image = symbol.image
    lines = np.sum(image, 0) // image.shape[0]
    if lines[0]==1:
        return 1
    else:
        return 0

def is_D(symbol):
    image = symbol.image
    zones = image.copy()
    y = zones.shape[0]/2
    y = int(y) 
    zones[y, :] = 1
    holes = count_holes(zones)
    return holes == 2


def recognize(symbol):
    holes = count_holes(symbol)
    if holes == 1:
        if(is_D(symbol)):
            return "D"
        else:
            return "R"
    elif holes == 0:
        bays = count_bays(symbol)
        if bays == 3:
                return "K"
        elif has_vline(symbol):
            if is_L(symbol):
                return "L"
            else:
                return "J"
    else:
        return ""


img = plt.imread("task3.png")
gray = np.average(img, 2)
gray[gray > 0] = 1
gray = gray.astype("uint8")

LB = label(gray)
total = LB.max()
print("total" + str(total))
sym=0
symbols = regionprops(LB)
recon = {"" : 0}
for symbol in symbols:
    sym = recognize(symbol)
    if sym not in recon:
        recon[sym] = 1
    else:
        recon[sym] += 1
        

print("Recognition rate: {}".format((total - recon[""]) / total))
print(recon)


#plt.imshow(gray, cmap="gray")
plt.figure()
plt.imshow(LB)
plt.show()

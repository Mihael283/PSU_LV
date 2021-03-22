from matplotlib import pyplot as plt
from skimage.transform import resize
import matplotlib.image as mpimg
import numpy as np
import skimage.io

img = skimage.io.imread('LV2\ziger.png', as_gray=True)
plt.figure(1)

for i in range(len(img)):
    img[i]+=40
    if (img[i]>255).any():
        img[i]=255
    
img1 = np.rot90(img,3) #zakrenuta slika

img2 = np.fliplr(img) #zrcaljena slika


img1_1 = [[img[j][i] for j in range(len(img))] for i in range(len(img[0]))]
img1_1 = np.fliplr(img1_1)

img3 = img[::5,::5]


plt.imshow(img3, cmap='gray', vmin=0, vmax=255)
plt.show()

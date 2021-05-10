import numpy as np

from sklearn.metrics import pairwise_distances_argmin
from sklearn.utils import shuffle

def quantize(raster, n_colors):
    width, height, depth = raster.shape
    reshaped_raster = np.reshape(
        raster, (width * height, depth))

    palette = shuffle(reshaped_raster)[:n_colors]
    labels = pairwise_distances_argmin(
        reshaped_raster, palette)

    quantized_raster = np.reshape(
        palette[labels], (width, height, palette.shape[1]))

    return quantized_raster

import scipy.misc

raster = scipy.misc.imread('example.png')
from skimage import color

lab_raster = color.rgb2lab(rgb_raster)
rgb_raster = color.lab2rgb(lab_raster) * 255).astype('uint8')

import matplotlib.pyplot as plt

plt.imshow(rgb_raster / 255.0)
plt.draw()
plt.show()
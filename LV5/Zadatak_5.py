
from skimage import io
from sklearn.cluster import KMeans
import numpy as np

image = io.imread('example.png')
io.imshow(image)
io.show()

rows = image.shape[0]
cols = image.shape[1]

image = image.reshape(rows*cols, 3)

kmeans = KMeans(n_clusters=3)
kmeans.fit(image)

compressed_image = kmeans.cluster_centers_[kmeans.labels_]
compressed_image = np.clip(compressed_image.astype('uint8'), 0, 255)

compressed_image = compressed_image.reshape(rows, cols, 3)

io.show()

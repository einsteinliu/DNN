import cPickle, gzip, numpy
import matplotlib.pyplot as plt
from matplotlib import cm
from PIL import Image

# Load the dataset
f = gzip.open('mnist.pkl.gz', 'rb')
train_set, valid_set, test_set = cPickle.load(f)
f.close()

imData = numpy.ndarray(shape=(28,28), dtype=int, order='F')
for x in range(0,28):
    for y in range(0,28):
        imData[x][y] = train_set[0][5][y+28*x]*255

plt.imsave('example.png',imData, cmap = cm.gray)
from skimage import data, io, filters
from skimage.transform import resize

url = 'paisagem.jpg'
boxl = 2

image = io.imread(url)

width, heigth, s = image.shape

def getPixel(img, x, y):
    pixelColor = img[x,y]
    return pixelColor

for i in range(0, width):
    for j in range(0, heigth):
        if i >= 0 and j >= 0 and i <= width and j <= heigth:
            image[i,j] = getPixel(image, i, j)

io.imshow_collection((io.imread(url),image))
io.show()
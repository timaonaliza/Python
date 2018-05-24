from skimage import data, io, filters

def getPixelColor(img, x, y):
    '''
        usar threading;
        conferir OutOfRange;
        calcular cor;
        retornar cor;
    '''
    return (0,0,0) #(R,G,B)


image = data.chelsea()
width, heigth, s = image.shape

for i in range(0, width):
    for j in range(0, heigth):
        image[i,j] = getPixelColor(image, i, j)

io.imshow_collection((data.chelsea(),image))
io.show()

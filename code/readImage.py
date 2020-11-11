from os.path import dirname, abspath
from PIL import Image
import numpy as np

LOWEST_VALUE = 30;

d = dirname(dirname(abspath(__file__)))
im = np.array(Image.open(d + '\\images\\nightSky2.jfif'))



'''
This function checks the neighbouring pixels of the selected pixel to see if it is the last pixel in its cluster
'''
def checkNeighbourPixels(topPixel, rightPixel, bottomPixel, leftPixel, bottomLeftPixel, topRightPixel, bottomRightPixel, topLeftPixel):

    if(nonBlackPixel(topPixel)):
        return True
    elif(nonBlackPixel(rightPixel)):
        return True
    elif(nonBlackPixel(bottomPixel)):
        return True
    elif(nonBlackPixel(leftPixel)):
        return True
    elif(nonBlackPixel(topRightPixel)):
        return True
    elif(nonBlackPixel(bottomLeftPixel)):
        return True
    elif(nonBlackPixel(bottomRightPixel)):
        return True
    elif(nonBlackPixel(topLeftPixel)):
        return True
    return False

def nonBlackPixel(pixel):
    if(pixel[0] > LOWEST_VALUE or pixel[1] > LOWEST_VALUE or pixel[2] > LOWEST_VALUE):
        return True
    else:
        return False

def checkHowManyNonBlackPixels(image):
    count = 0
    imageSize = image.shape
    for x in range(imageSize[1]):
        for y in range(imageSize[0]):
            currentPixel = image[y][x]
            if(currentPixel[0] > LOWEST_VALUE or currentPixel[1] > LOWEST_VALUE or currentPixel[2] > LOWEST_VALUE):
                count += 1
    return count

print(type(im))
print(im.dtype)
print(im.shape)

imageSize = im.shape
starCount = 0

for x in range(imageSize[1]):
    for y in range(imageSize[0]):
        currentPixel = im[y][x]
        if(nonBlackPixel(currentPixel) and (y>0 and x>0) and (y<imageSize[0]-1 and x<imageSize[1]-1)):
            
            # get the directly neighbouring pixels
            topPixel = im[y-1][x]
            rightPixel = im[y+1][x]
            bottomPixel = im[y][x+1]
            leftPixel = im[y][x-1]

            # get the diagonally neighbouring pixels
            bottomLeftPixel = im[y-1][x-1]
            topRightPixel = im[y+1][x+1]
            bottomRightPixel = im[y-1][x+1]
            topLeftPixel = im[y+1][x-1]

            # if one of the neighbouring pixels is non black then we can black out the current pixel
            if(checkNeighbourPixels(topPixel, rightPixel, bottomPixel, leftPixel, bottomLeftPixel, topRightPixel, bottomRightPixel, topLeftPixel)):
                im[y][x] = (0,0,0)
            else:
                starCount += 1

print("Star Count: " + str(starCount))


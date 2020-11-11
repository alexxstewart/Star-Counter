import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))
#print(d + '\images\stars.png')

img=mpimg.imread(d + '\\images\\stars.png')
imgplot = plt.imshow(img)
plt.show()
i = 0
for x in img:
    print(i + 1)
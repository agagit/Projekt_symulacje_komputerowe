import numpy as np
import matplotlib.pyplot as plt

from skimage import data
from skimage.feature import match_template
#from imread import imread, imsave

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#from skimage import data
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label
from skimage.morphology import closing, square
from skimage.measure import regionprops
from skimage.color import label2rgb, rgb2gray
from skimage.data import imread

#WCZYTYWANIE OBRAZKA
image = imread('o.jpg')
image = np.invert(image)
image = rgb2gray(image)
# apply threshold
thresh = threshold_otsu(image)
bw = closing(image > thresh, square(3))

# remove artifacts connected to image border
cleared = bw.copy()
clear_border(cleared)

# label image regions
label_image = label(cleared)
borders = np.logical_xor(bw, cleared)
label_image[borders] = -1
image_label_overlay = label2rgb(label_image, image=image)

fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 6))
ax.imshow(image_label_overlay)

for region in regionprops(label_image):

    # skip small images
    if region.area < 100:
        continue

    # draw rectangle around segmented coins
    minr, minc, maxr, maxc = region.bbox
    rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                              fill=False, edgecolor='red', linewidth=2)
    ax.add_patch(rect)

plt.show()


#WCZYTYWANIE WZORU
wzor = imread('wzor.jpg')
wzor = np.invert(wzor)
wzor = rgb2gray(wzor)

#POROWNYWANIE WZORU Z OBRAZKIEM
result = match_template(image, wzor)
result2=result

fig = plt.figure(figsize=(12, 5))
ax1 = plt.subplot(1, 3, 1)
ax2 = plt.subplot(1, 3, 2 )
ax3 = plt.subplot(1, 3, 3, sharex=ax2, sharey=ax2)




ax1.imshow(wzor)
ax1.set_axis_off()
ax1.set_title('template')



#WYSZUKIWANIE NAJWIEKSZYCH WARTOSCI


ax2.imshow(image)
ax2.set_axis_off()
ax2.set_title('image')
hwzor, wwzor = wzor.shape

ij = np.unravel_index(np.argmax(result2), result.shape)
x, y = ij[::-1]

rect = plt.Rectangle((x, y), wwzor, hwzor, edgecolor='r', facecolor='none')
ax2.add_patch(rect)

result2[ij]=0


#kl[0]=np.unravel_index(np.argmax(result2), result.shape)
#z, m= kl[::-1]


i = 0
while (np.argmax(result2) > 5000):
    
    ij=np.unravel_index(np.argmax(result2), result.shape)
    x, y= ij[::-1]
    result2[ij]=0
    i=i+1
    rect = plt.Rectangle((x, y), wwzor, hwzor, edgecolor='r', facecolor='none')
    ax2.add_patch(rect)








# highlight matched region

#rect = plt.Rectangle((x[0], y[0]), wwzor, hwzor, edgecolor='r', facecolor='none')
#rect2 = plt.Rectangle((z, m), wwzor, hwzor, edgecolor='r', facecolor='none')
#ax2.add_patch(rect)
#ax2.add_patch(rect2)






ax3.imshow(result)
ax3.set_axis_off()
ax3.set_title('`match_template`\nresult')
# highlight matched region
ax3.autoscale(False)
#ax3.plot(x, y, 'o', markeredgecolor='r', markerfacecolor='none', markersize=10)


plt.show()

#kanal red
#image[0:39 , 0:46, 0]




fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(result)

plt.show()



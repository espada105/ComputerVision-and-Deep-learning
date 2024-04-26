import cv2 as cv
import numpy as np
import time
def gray1(bgr_img):
    g = np.zeros([bgr_img.shape[0],bgr_img.shape[1]])
    for r in range(bgr_img.shape[0]):
        for c in range(bgr_img.shape[1]):
            g[r,c]=0.114*bgr_img[r,c,0]+0.587*bgr_img[r,c,1]+0.299 * bgr_img[r,c,2]
    return np.uint8(g)


img = cv.imread('usagi.jpg')

start = time.time()
gray1(img)
print('My time1:', time.time()-start)

start = time.time()
cv.cvtColor(img,cv.COLOR_BGR2GRAY)
print('My time2:', time.time()-start)
import cv2 as cv

img = cv.imread('rose.png')
patch = img[250:350,170:270,:]

img = cv.rectangle(img,(170,250),(270,350),(255,0,0),3)

patch1 = cv.resize(patch,dsize=(0,0),fx=5,fy=5,interpolation=cv.INTER_NEAREST)
patch2 = cv.resize(patch,dsize=(0,0),fx=5,fy=5,interpolation=cv.INTER_LINEAR)
patch3 = cv.resize(patch,dsize=(0,0),fx=5,fy=5,interpolation=cv.INTER_CUBIC)

cv.imshow('Original',img)
cv.imshow('resize nearest',patch1)
cv.imshow('resize bilinear',patch2)
cv.imshow('resize bicubic',patch3)

cv.waitKey()
cv.destroyAllWindows()

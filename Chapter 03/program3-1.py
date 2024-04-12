import cv2 as cv
import sys
img = cv.imread('usagi.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다')

cv.imshow('origin_img',img)
cv.imshow('upper left half',img[0:img.shape[0]//2, 0:img.shape[1]//2,:])
cv.imshow('center half',img[0:img.shape[0]//4:3*img.shape[0]//4, img.shape[1]//4:3*img.shape[1]//4,:])

cv.imshow('R',img[:,:,2])
cv.imshow('G',img[:,:,1])
cv.imshow('B',img[:,:,0])

cv.waitKey()
cv.destroyAllWindows()
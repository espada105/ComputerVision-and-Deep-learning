import cv2 as cv
import sys

img = cv.imread('우사기.webp')

if img is None:
    sys.exit('파일을 찾을 수 없습니다')

cv.rectangle(img, (130, 30), (1000, 200), (0, 0, 255), 2)
cv.putText(img, 'HAHAHAHAHAHAHAHAHAHAHAHAHAH', (830, 24), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

cv.imshow('Draw', img)
cv.waitKey(0)  # 사용자가 키 입력을 대기합니다. 0은 무한 대기를 의미합니다.
cv.destroyAllWindows()

import cv2
import sys

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    sys.exit('카메라 연결 실패')

while True:
    ret, frame = cap.read()

    if not ret:
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break

    cv2.imshow('Video display', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

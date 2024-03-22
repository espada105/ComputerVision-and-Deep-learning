import cv2 as cv
import numpy as np
import datetime

def main():
    # 카메라 연결
    cap = cv.VideoCapture(0)

    # 카메라가 열리지 않았을 때 처리
    if not cap.isOpened():
        print('카메라 연결 실패')
        return

    # 비디오 저장을 위한 설정
    fps = 1  # 1초에 1프레임
    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    out = None  # VideoWriter 객체를 담을 변수

    # 사진을 저장할 빈 리스트 생성
    frames = []

    while True:
        ret, frame = cap.read()

        if not ret:
            print('프레임 획득에 실패하여 루프를 나갑니다.')
            break

        cv.imshow('Camera', frame)

        key = cv.waitKey(1) & 0xFF  # 키보드 입력을 기다림

        # q를 입력하면 사진을 찍음
        if key == ord('q'):
            frames.append(frame)
            print('사진을 찍었습니다.')

            # 사진을 파일로 저장
            filename = f"photo_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.jpg"
            cv.imwrite(filename, frame)
            print(f"사진을 {filename}으로 저장했습니다.")

        # w를 입력하면 카메라를 종료하고 비디오를 생성
        elif key == ord('w'):
            if len(frames) > 0:
                # 비디오 파일 생성 및 프레임 저장
                out = cv.VideoWriter('output.avi', cv.VideoWriter_fourcc(*'XVID'), fps, (width, height))
                for img in frames:
                    out.write(img)
                out.release()  # 비디오 파일 닫기
                print('비디오를 저장했습니다.')
            else:
                print('찍은 사진이 없습니다.')

            break

    # 카메라 리소스 해제
    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()

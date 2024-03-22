import cv2 as cv
import os

def main():
    # 비디오 저장을 위한 설정
    fps = 1  # 1초에 1프레임

    # 사진이 저장된 디렉토리
    photo_directory = "./photo_/"

    # 비디오 저장을 위한 VideoWriter 객체 생성
    width, height = 0, 0
    out = None

    # 저장된 사진 파일들을 읽어옴
    photos = [photo_directory + f for f in os.listdir(photo_directory) if f.endswith('.jpeg')]

    if not photos:
        print('저장된 사진이 없습니다.')
        return

    # 첫 번째 사진을 기준으로 비디오의 크기 설정
    first_photo = cv.imread(photos[0])
    height, width, _ = first_photo.shape

    # 비디오 파일 생성 및 프레임 저장
    out = cv.VideoWriter('output.avi', cv.VideoWriter_fourcc(*'XVID'), fps, (width, height))
    for photo in photos:
        img = cv.imread(photo)
        out.write(img)

    # 비디오 파일 닫기
    out.release()
    print('비디오를 저장했습니다.')

if __name__ == "__main__":
    main()

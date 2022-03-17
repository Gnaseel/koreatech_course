# 실행 명령어 : python main.py
from copy import copy
import cv2
import numpy as np
import time
def q3_1():

    img = cv2.imread("Lenna.png")

    # grayscale로 변경
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 임계값 적용해서 이진화
    _ , dst = cv2.threshold(img, 100, 120, cv2.THRESH_BINARY)    

    # 이미지 출력
    cv2.imshow("img", img)
    cv2.imshow("dst", dst)
    cv2.waitKey(0)
    return

def q3_2():
    
    img = cv2.imread("Lenna.png")

    # grayscale로 변경
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 임계값 적용해서 삼진화
    dst = np.where(img < 150, 0, img)
    dst = np.where(((150<=dst) & (dst < 200)), 100, dst)
    dst = np.where(200<=dst, 255, dst)

    # 이미지 출력
    cv2.imshow("img", img)
    cv2.imshow("dst", dst)
    cv2.waitKey(0)
    return
    
def q3_3():
    # 비디오 읽기
    cap = cv2.VideoCapture('Cat.mp4')
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        otsu_frame = frame.copy()

        # grayscale 변경
        otsu_frame = cv2.cvtColor(otsu_frame, cv2.COLOR_BGR2GRAY)

        # 이진화
        _ , otsu_frame = cv2.threshold(otsu_frame, 100, 255, cv2.THRESH_OTSU)    

        # 원본, otsu 이진화 처리 추가한 이미지 출력
        cv2.imshow('frame',frame)
        cv2.imshow('otsu_frame',otsu_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    return

def main():

    # 실습문제 3-1
    q3_1()
    # 실습문제 3-2
    # q3_2()
    # 실습문제 3-3
    # q3_3()
    return

if __name__=="__main__":
    main()
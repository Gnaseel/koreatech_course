# 실행 명령어 : python main.py
from copy import copy
import cv2
import numpy as np
import time
import glob
import os
def q4_1():

    img = cv2.imread("Lenna.png")

    # grayscale로 변경
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gaussian_blur_img_list = []
    median_blur_img_list = []
    for sdv in range (1, 5, 1):
        # 가우시안 블러 적용
        gaussian_blur_img_list.append(cv2.GaussianBlur(img, (0, 0), sdv))
        # 미디안 블러 적용
        median_blur_img_list.append(cv2.medianBlur(img, sdv//2*10+1))

    # 이미지 출력
    cv2.imshow("img", img)
    for idx, blur_img in enumerate(gaussian_blur_img_list):
        cv2.imshow("{}_g_blur_img".format(idx), blur_img)
    for idx, blur_img in enumerate(median_blur_img_list):
        cv2.imshow("{}_m_blur_img".format(idx), blur_img)
    cv2.waitKey(0)
    return

def q4_2():
    
    img = cv2.imread("Lenna.png")

    # grayscale로 변경
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 소벨 필터 적용
    sobel_img = cv2.Sobel(img, -1, 1, 1)
    # 캐니 에지 디텍터 적용
    canny_img = cv2.Canny(img, 150, 200)
    
    # 이미지 출력
    cv2.imshow("img", img)
    cv2.imshow("sobel_img", sobel_img)
    cv2.imshow("canny_img", canny_img)
    cv2.waitKey(0)
    return
    
def q4_3():
    # 비디오 읽기
    cap = cv2.VideoCapture('Cat.mp4')
    
    # 비디오 저장 파라미터
    w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    fps = cap.get(cv2.CAP_PROP_FPS)
    out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h), isColor = False)
    while(cap.isOpened()):
        ret, frame = cap.read()
        if frame is None:
            break
        # grayscale 변경
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        # 가우시안 블러 적용
        gaussian_img = cv2.GaussianBlur(gray_img, (0, 0), 5)
        # 미디안 블러 적용
        median_img = cv2.medianBlur(gaussian_img, 21)
        # 캐니 에지 디텍터 적용
        canny_img = cv2.Canny(median_img, 50, 55)

        # 원본, otsu 이진화 처리 추가한 이미지 출력
        cv2.imshow('raw',frame)
        cv2.imshow('gaussian_img',gaussian_img)
        cv2.imshow('median_img',median_img)
        cv2.imshow('canny_img',canny_img)

        # 동영상 저장
        out.write(canny_img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    return

# lane_img_path -> 차선이미지 폴더 경로 (한글 포함시 오류)
def q4_4(lane_image_path = "C:\\Users\\admin\\Documents\\course\\computer_vision\\Original\\Lane1"):

    #차선인식을 위한 파일 목록 읽기
    file_path_list = glob.glob(os.path.join(lane_image_path, '*'))
    cv2.waitKey(0)
    for img_path in file_path_list:
        img  = cv2.imread(img_path)

        # grayscale 변환
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #ROI 마스크 생성
        mask_img = np.zeros(gray_img.shape, dtype = np.uint8)
        mask_img = getROI(mask_img)

        # 가우시안 블러 적용
        gaussian_img = cv2.GaussianBlur(gray_img, (0, 0), 1)
        # 캐니 에지 디텍터 적용
        canny_img = cv2.Canny(gaussian_img, 70, 100)

        # ROI 적용
        roi_img = canny_img * mask_img

        # 원본, otsu 이진화 처리 추가한 이미지 출력
        cv2.imshow('raw',img)
        cv2.imshow('gaussian_img',gaussian_img)
        cv2.imshow('canny_img',canny_img)
        cv2.imshow('roi_img',roi_img)
        time.sleep(0.03)
        cv2.waitKey(1)
    return

def getROI(mask_img):
    re_img = mask_img.copy()
    delta_height=10
    dx=17
    for idx, height in enumerate(range(260, 481, delta_height)):
        width = (70 + dx*idx)
        if width > 360:
            width =360
        re_img[height:height+delta_height, 360-width:360+width ] = 1
    return re_img


def main():

    # 실습문제 4_1
    # q4_1()
    # 실습문제 4_2
    # q4_2()
    # 실습문제 4_3
    # q4_3()
    # 실습문제 4_3
    q4_4()
    return

if __name__=="__main__":
    main()
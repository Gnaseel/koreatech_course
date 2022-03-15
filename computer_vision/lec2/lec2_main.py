import cv2
import numpy as np

def main():
    # 이미지 입력
    file_name = "Lenna.png"
    img_path =file_name
    img = cv2.imread(img_path)
    
    # 이미지 읽기 실패
    if type(img) != np.ndarray:
        print("Img Not found")
        return

    # Lenna 출력
    cv2.imshow("lenna", img)
    # Gray Lenna 출력
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray_lenna", gray_img)
    
    cv2.waitKey(0)
    return

if __name__=="__main__":
    main()
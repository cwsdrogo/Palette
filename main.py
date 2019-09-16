import cv2 as cv
import numpy as np

def nothing(tmp):
    pass

#  使用numpy初始化一个图片数组，注意类型的声明
img = np.ones([480, 480, 3], dtype=np.uint8)
img[:] = 255
cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.createTrackbar('R', 'image', 255, 255, nothing)
cv.createTrackbar('G', 'image', 255, 255, nothing)
cv.createTrackbar('B', 'image', 255, 255, nothing)

while(1):
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):
        break
    #  获取滑块位置
    r = cv.getTrackbarPos('R', 'image')
    g = cv.getTrackbarPos('G', 'image')
    b = cv.getTrackbarPos('B', 'image')
    img[:] = [b, g, r]

cv.destroyAllWindows()
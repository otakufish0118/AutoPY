import time
import cv2 as cv
from matplotlib import pyplot as plt

def compare():
    im = cv.imread("cap.png")
    template = cv.imread("mjcap.png")
    w = template.shape[1]
    h = template.shape[0]

    t1 = time.time()

    res = cv.matchTemplate(im, template, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

    top_left = max_loc[0], max_loc[1]
    bottom_right = (max_loc[0] + w, max_loc[1] + h)
    im2 = im.copy()
    cv.rectangle(im2, top_left, bottom_right, color=(0,255,0), thickness=2)

    t2 = time.time()
    print("總耗時{0}秒".format(round(t2-t1, 5)))

# BGR to RGB
    im2_2 = im2[:,:,[2,1,0]]
    temp2 = template[:,:,[2,1,0]]
#    plt.subplot(131), plt.imshow(res, cmap = "gray")
#    plt.title("Matching Resault"), plt.xticks([]), plt.yticks([])
    plt.subplot(121), plt.imshow(im2_2)
    plt.title("Detected Point"), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(temp2)
    plt.title("Template"), plt.xticks([]), plt.yticks([])

    plt.show()

#compare()

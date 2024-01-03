import os
import cv2
import numpy as np
import math
import time
try:
    import imutils
except:
    os.system("pip install imutils")
    import imutils



def crop_contours(image, contour):
    x, y, w, h = cv2.boundingRect(contour)
    result = image[y:y+h, x:x+w]
    return result


def FindArea(contours,hierarchy,src):
    min_area = 20000
    max_area = 90000
    output = []
    for index, cnt in enumerate(contours):
        if hierarchy[0, index, 2] == -1:
            continue;
        area = cv2.contourArea(cnt)
        if area >= min_area  and area <= max_area:
            # cv2.drawContours(src, [cnt], -1, (0,0,255),1, cv2.LINE_AA)
            cropped_part = crop_contours(src, cnt)
            output.append(cropped_part)
    return  output




list_path_temp = r"C:\Users\HPR\OneDrive\data\logo\logoBanVe"
list_path_src = r"C:\Users\HPR\OneDrive\data\logo\NORTHRUP"
list_temp = {}
list_src  = []
check =  []
method = eval("cv2.TM_CCOEFF_NORMED")
resutl = {}

for folder_name in os.listdir(list_path_src):
            folder_path = os.path.join(list_path_src, folder_name)
            if os.path.isdir(folder_path):
                image_files = [f for f in os.listdir(folder_path) if f.endswith(('_1.jpg', '_1.png', '_1.jpeg'))]
                for sr in image_files:
                    image_path = folder_path+"\\"+sr
                    list_src.append(image_path)

if os.path.isdir(list_path_temp):
    logo_file = [f for f in os.listdir(list_path_temp) if f.endswith(('.jpg', '.png', '.jpeg'))]
    for lg in logo_file:
        logo_path = list_path_temp +"\\"+lg
        list_temp[lg] = logo_path


for idx,image in enumerate(list_src):
    sr = cv2.imread(image)
    height, width, _ = sr.shape
    sr = sr[height-height//4:,width-width//4:, :]
    sr = cv2.pyrDown(sr)

    flag  = False

    img_src = cv2.cvtColor(sr, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(img_src, (3, 3), 0)
    _, edges_src = cv2.threshold(blurred, 220, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy_src = cv2.findContours(edges_src, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    box = FindArea(contours, hierarchy_src, sr)
    cv2.imshow(f"edges_src {idx}",edges_src)
    if not box:
        print("miss box")
        continue
    for tag,template in list_temp.items():
        temp = cv2.imread(template)
        temp = cv2.pyrDown(temp)
        cv2.imshow("temp",temp)
        for area in box:
            try:
                res = cv2.matchTemplate(area,temp,method)
                minval, maxval, minloc, maxloc = cv2.minMaxLoc(res)
                if (maxval >= 0.5):
                        resutl[tag] = image
                        # cv2.imshow("temp", temp)
                        # cv2.imshow("sr", area)
                        print(f"contract {idx}th : ",tag)
                        flag = True
                        break
            except:
                    pass
        if flag:
            break
print(resutl)
cv2.waitKey(0)
cv2.destroyAllWindows()

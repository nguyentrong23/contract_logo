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


def padding(img,size):
    top, bottom, left, right = size, size,0,0
    border_color = [0, 0, 0]
    image_with_padding = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=border_color)
    return image_with_padding

# def matching(edges_src,edges_tem,template,object,min_thresh,sr0):
#     method = eval("cv2.TM_CCOEFF_NORMED")
#     h, w = edges_tem.shape[:2]
#     topleft = [0, 0]
#     y_size = max(h, w)
#     x_size = edges_src.shape[1]
#     angel_target = []
#     mean_target = []
#     for angle_t in template.values():
#         for index, (mean, angles) in enumerate(object.items()):
#             # angle = angles - angle_t
#             angle = angles
#             rotated_src = imutils.rotate(edges_src,angle)
#             roi_x = 0
#             roi_y = int(mean[1] - y_size/2)
#             roi_y = max(roi_y, 0)
#             # Tạo ROI (Region of Interest)
#             roi = rotated_src[roi_y:roi_y + y_size, roi_x:x_size]
#             # cv2.imshow('roi', roi)
#             if(roi_y+y_size) > edges_src.shape[0]:
#                 size = roi_y+y_size - edges_src.shape[0]
#                 roi =  padding(roi, size)
#                 roi_y = roi_y - size
#             res = cv2.matchTemplate(roi, edges_tem, method)
#             min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#             if max_val >= min_thresh:
#                 print(max_val)
#                 # sr0 = imutils.rotate(sr0, angle)
#                 topleft = max_loc
#                 topleft = (topleft[0], topleft[1] + roi_y)
#                 bottomright = (topleft[0] + w, topleft[1] + h)
#                 # cv2.rectangle(sr0, topleft, bottomright, (0, 255, 255), 1)
#                 center_x = (topleft[0] + bottomright[0]) // 2
#                 center_y = (topleft[1] + bottomright[1]) // 2
#                 # sr0 = imutils.rotate(sr0, -angle)
#
#                 m_target = (center_x, center_y)
#                 m_target = rotate_point_in_image(sr0, m_target, -angle)
#                 cv2.circle(sr0, (m_target[0], m_target[1]), 3, (0, 255, 255), -1)
#                 mean_target.append(m_target)
#                 angel_target.append(angles)
#     sr0 = cv2.pyrDown(sr0)
#     cv2.imshow('Original Image', sr0)
#     cv2.imshow(' Image', edges_tem)
#     cv2.waitKey(0)
#     # end_time = time.time()
#     # execution_time = end_time - start_time
#     # print(f"Thời gian chạy: {execution_time} giây")
#     # cv2.imwrite("kt_mean.png",sr0)
#     return  angel_target,mean_target


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
    sr = cv2.pyrDown(sr)
    for tag,template in list_temp.items():
        temp = cv2.imread(template)
        temp = cv2.pyrDown(temp)
        res = cv2.matchTemplate(sr,temp, method)
        minval, maxval, minloc, maxloc = cv2.minMaxLoc(res)
        if (maxval >= 0.8):
            resutl[tag] = image
            print(maxval)
            print(idx,tag)

print(resutl)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
from paddleocr import PaddleOCR, draw_ocr
import numpy as np

img_path = 'customer/BLUE/BLUE_1.png'
img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

ocr = PaddleOCR(use_angle_cls=True, lang='en')
result = ocr.ocr(img_path, cls=True)
sorted_result = sorted([word_info for line in result for word_info in line], key=lambda x: x[0][0][0])
boxes = [word_info[0] for word_info in sorted_result]

# Draw bounding boxes on the image
image_with_boxes = draw_ocr(img, boxes)
cv2.imshow('Original Image', image_with_boxes)
cv2.waitKey(0)
cv2.destroyAllWindows()



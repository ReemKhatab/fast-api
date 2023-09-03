from ultralytics import YOLO


model = YOLO('runs/train/exp10/weights/best.pt')

result = model('mydatasets/license_plates/test/images/car4.jpg')

import cv2 as cv

cv.imshow(result)
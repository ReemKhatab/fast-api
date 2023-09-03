import sys
import cv2
img=cv2.imread(r"C:\Users\Reem\yolov5\runs\detect\exp2\man.jpg",cv2.IMREAD_ANYCOLOR)
while True:
    cv2.imshow("man", img)
    cv2.waitKey(0)
    sys.exit() # to exit from all the processes
 
cv2.destroyAllWindows() # destroy all windows

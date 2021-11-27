from cv2 import cv2
import numpy as np 

image_directory="/.../.../"
image=cv2.imread(image_directory,0)
cv2.imshow("Before Histogram Equalization",image)
rows=image.shape[0]
cols=image.shape[1]
frequency=np.zeros((256,1))
for i in range(0,rows):
    for j in range(0,cols):
        frequency[image[i,j],0]=frequency[image[i,j],0]+1
cumulative_frequency=np.zeros((256,1))
cumulative_frequency[0,0]=frequency[0,0]
for i in range(1,256):
    cumulative_frequency[i,0]=frequency[i,0]+cumulative_frequency[i-1,0]
normalized_frequency=cumulative_frequency/cumulative_frequency[255,0]
for i in range(255,0,-1):
    if frequency[i,0]!=0:
        maximum_gray_level=i
        break
new_pixel=normalized_frequency*maximum_gray_level
for i in range(0,256):
    new_pixel[i,0]=round(new_pixel[i,0])
for i in range(0,rows):
    for j in range(0,cols):
        image[i,j]=new_pixel[image[i,j],0]

cv2.imshow("After Histogram Equalization",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

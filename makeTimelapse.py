import cv2
import numpy as np 
import glob

img_array = []
filenames = glob.glob('images/*.jpg')
filenames.sort()

print(filenames[0])
img = cv2.imread(filenames[0])
height, width, layers = img.shape
size = (width,height)

print(size)
for filename in filenames:
    img = cv2.imread(filename)
    img_array.append(img)

out = cv2.VideoWriter('OFWebcamTimelapse.avi',cv2.VideoWriter_fourcc(*'DIVX'), 1, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
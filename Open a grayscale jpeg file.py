#locate your current directory
import os
cwd = os.getcwd()
cwd
#change directory to the folder where jpeg image "test" is located. This could be any image you have saved in the directory location.
os.chdir('C:/Users/Desktop/OpenCV')
#import packages cv2, numpy and matplotlib
import cv2
import numpy as np
from matplotlib import pyplot as plt
#read image
img = cv2.imread('test.jpg',cv2.IMREAD_GRAYSCALE)
      cv2.imshow('image',img)
      cv2.waitKey(0)
      cv2.destroyAllWindows()
# Above code helps open image in gray color, if you want to view image in Color, do this
import cv2
import numpy as np
from matplotlib import pyplot as plt
# read image
img = cv2.imread('watch.jpg', 1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

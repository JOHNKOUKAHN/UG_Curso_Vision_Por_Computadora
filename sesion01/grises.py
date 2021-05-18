import cv2
import numpy as np

grises=np.zeros((1,256))

for i in range(0,255):
	grises[0,i] = i

cv2.imwrite("grises.jpg",grises)	

	

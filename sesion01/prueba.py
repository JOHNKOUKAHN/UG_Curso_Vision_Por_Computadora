import cv2
import numpy as np

negro=np.zeros((600,600,3))
for i in range(0,299):
	for j in range(0,299):
		negro[i,j,0]=128
		negro[i,j,1]=100
		negro[i,j,2]=128

for i in range(299,599):
	for j in range(0,299):
		negro[i,j,0]=0
		negro[i,j,1]=128
		negro[i,j,2]=0

for i in range(0,299):
	for j in range(299,599):
		negro[i,j,0]=0
		negro[i,j,1]=0
		negro[i,j,2]=128

for i in range(299,599):
	for j in range(299,599):
		negro[i,j,0]=1
		negro[i,j,1]=1
		negro[i,j,2]=1

imagen= cv2.imread('color2.jpg',0)
'''for i in range(imagen.shape[0]):
	for j in range(imagen.shape[1]):
		imagen[i,j,2]=0
		imagen[i,j,1]=0'''
cv2.imwrite('color2.jpg',negro)
cv2.imshow('original',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np
'''#leer un imagen
imagen = cv2.imread('censura.jpg')

for i in range(imagen.shape[0]):
	for j in range(imagen.shape[1]):
		#Eliminar la parte verde de la imagen
		imagen[i,j,0]=0
		#Eliminar la parte roja de la imagen
		imagen[i,j,2]=0
'''
#crear una imagen
imagen = np.zeros((600,600,3))

for i in range(0,299):
	for j in range(0,299):
		imagen[i,j,0]=255
		imagen[i,j,1]=0
		imagen[i,j,2]=255
for i in range(0,299):
	for j in range(300,599):
		imagen[i,j,0]=0
		imagen[i,j,1]=255
		imagen[i,j,2]=255

for i in range(300,599):
	for j in range(0,299):
		imagen[i,j,0]=255
		imagen[i,j,1]=0
		imagen[i,j,2]=0

for i in range(300,599):
	for j in range(300,599):
		imagen[i,j,0]=255
		imagen[i,j,1]=255
		imagen[i,j,2]=255


#mmostrar la imagen en pantalla
cv2.imshow('imagen',imagen)
#esperar entrada del teclado
cv2.waitKey(0)
#Limpiar la pantalla
cv2.destroyAllWindows()

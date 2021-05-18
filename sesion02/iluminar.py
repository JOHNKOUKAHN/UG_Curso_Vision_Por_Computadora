import cv2
import copy
import time

imagen = cv2.imread('censura.jpg',0)
copia = copy.copy(imagen)

aumentos = [-50, -40, -30, -10, 0, 10, 20, 30, 40, 50]
for t in range(len(aumentos)):
	for i in range(imagen.shape[0]):
		for j in range(imagen.shape[1]):
			copia[i,j] = imagen[i,j] + aumentos[t]		

	cv2.imshow('imagen',copia)
	cv2.waitKey(0)
#mmostrar la imagen en pantalla
'''cv2.namedWindow('imagen', cv2.WINDOW_NORMAL)
cv2.resizeWindow('imagen', 600, 400)
cv2.imshow('imagen',imagen)'''
#esperar entrada del teclado

#Limpiar la pantalla
cv2.destroyAllWindows()

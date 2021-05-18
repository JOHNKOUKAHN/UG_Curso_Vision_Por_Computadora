import cv2

imagen = cv2.imread('oscura1.jpg',0)
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Original', 600, 400)
cv2.imshow('Original',imagen)

maximo = 0
minimo = 255
for i in range(imagen.shape[0]):
	for j in range(imagen.shape[1]):
		if(imagen[i,j] > maximo ):
			maximo = imagen[i,j]
		if(imagen[i,j] < minimo ):
			minimo = imagen[i,j]

for i in range(imagen.shape[0]):
	for j in range(imagen.shape[1]):
		imagen[i,j] = (255 / maximo - minimo ) * (imagen[i,j] - minimo)

#mmostrar la imagen en pantalla
cv2.namedWindow('imagen', cv2.WINDOW_NORMAL)
cv2.resizeWindow('imagen', 600, 400)
cv2.imshow('imagen',imagen)
#esperar entrada del teclado
cv2.waitKey(0)
#Limpiar la pantalla
cv2.destroyAllWindows()

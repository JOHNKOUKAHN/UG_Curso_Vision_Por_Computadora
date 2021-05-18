import cv2

imagen = cv2.imread('oscura1.jpg')
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Original', 800, 600)
cv2.imshow('Original',imagen)

aumento = 45
for i in range(imagen.shape[0]):
	for j in range(imagen.shape[1]):
		imagen[i,j,0]= imagen[i,j,0] + aumento
		imagen[i,j,1]= imagen[i,j,1] + aumento
		imagen[i,j,2]= imagen[i,j,2] + aumento


#mmostrar la imagen en pantalla
cv2.namedWindow('imagen', cv2.WINDOW_NORMAL)
cv2.resizeWindow('imagen', 800, 600)
cv2.imshow('imagen',imagen)
#esperar entrada del teclado
cv2.waitKey(0)
#Limpiar la pantalla
cv2.destroyAllWindows()

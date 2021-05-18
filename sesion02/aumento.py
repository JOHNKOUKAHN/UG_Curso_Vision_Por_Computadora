import cv2

imagen = cv2.imread('oscura1.jpg',0)

cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Original', 600, 400)
#mmostrar la imagen en pantalla
cv2.imshow('Original',imagen)

for i in range(imagen.shape[0]):
	for j in range(imagen.shape[1]):
		imagen[i,j] = imagen[i,j] - 30 


cv2.namedWindow('Aumentada', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Aumentada', 600, 400)
#mmostrar la imagen en pantalla
cv2.imshow('Aumentada',imagen)
#esperar entrada del teclado
cv2.waitKey(0)
#Limpiar la pantalla
cv2.destroyAllWindows()


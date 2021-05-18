import cv2

imagen = cv2.imread('oscura1.jpg')




imagen[0,0,0] = 0
imagen[0,0,1] = 0
imagen[0,0,2] = 0

imagen[0,1,0] = 255
imagen[0,1,1] = 255
imagen[0,1,2] = 255

for i in range(imagen.shape[0]):
	for j in range(imagen.shape[1]):
		suma = imagen[i,j,0] + imagen[i,j,1] + imagen[i,j,2]
		promedio = suma / 3

		imagen[i,j,0] = promedio
		imagen[i,j,1] = promedio
		imagen[i,j,2] = promedio  

cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Original', 600, 400)
#mmostrar la imagen en pantalla
cv2.imshow('Original',imagen)		

minimo = 255
maximo = 0

for i in range(imagen.shape[0]):
	for j in range(imagen.shape[1]):
		if(imagen[i,j,0] > maximo):
			maximo = imagen[i,j,0]
		if(imagen[i,j,0] < minimo):
			minimo = imagen[i,j,0]

print('Maximo = ' + str(maximo))
print('Minimo = ' + str(minimo))


for i in range(imagen.shape[0]):
	for j in range(imagen.shape[1]):

		imagen[i,j,0] = (255/ (maximo - minimo)) * (imagen[i,j,0] - minimo)
		imagen[i,j,1] = (255/ (maximo - minimo)) * (imagen[i,j,1] - minimo)
		imagen[i,j,2] = (255/ (maximo - minimo)) * (imagen[i,j,2] - minimo)



cv2.namedWindow('ajustada', cv2.WINDOW_NORMAL)
cv2.resizeWindow('ajustada', 600, 400)
#mmostrar la imagen en pantalla
cv2.imshow('ajustada',imagen)
#esperar entrada del teclado
cv2.waitKey(0)
#Limpiar la pantalla
cv2.destroyAllWindows()

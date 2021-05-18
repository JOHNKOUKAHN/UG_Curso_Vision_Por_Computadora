import cv2


def EsSangre(valorB,valorG,valorR):
	if(valorB < 30 and valorG < 30 and valorR > 150):
		return True
	else:
		return False


imagen = cv2.imread('censura.jpg')


for i in range(50,230):
	for j in range(50,400):
		if(EsSangre(imagen[i,j,0],imagen[i,j,1],imagen[i,j,2])):

			imagen[i,j,0]=200
			imagen[i,j,1]=200
			imagen[i,j,2]=200



#mmostrar la imagen en pantalla
cv2.imshow('imagen',imagen)
#esperar entrada del teclado
cv2.waitKey(0)
#Limpiar la pantalla
cv2.destroyAllWindows()

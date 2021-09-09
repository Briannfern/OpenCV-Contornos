import cv2
path= r'C:\Users\brian\OneDrive\Documentos\PYTHON PRACTICAS\python para no matematicos\Proyecto\contorno.jpg'
imagen=cv2.imread(path) # lee la imagen 
 # Primero se pasa la imagen a blanco y negro.
grises= cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY) 
'''
El método cvtColor se utiliza para convertir una imagen de un espacio de color a otro (1,2) 1 es la variable, 2 es el metodo del color.
Una imagen se divide en 3 canales, Rojo, verde y azul que van de 0 a 255

'''
# se aplica el umbral
_,umbral= cv2.threshold(grises,100,255,cv2.THRESH_BINARY)

'''
# El guion bajo es una variable ficticia, ultilizada debido a que el metodo devuelve 2 salidas.
# threshold se utiliza para aplicar el umbral. El método devuelve dos salidas. El primero es el umbral que se utilizó y el segundo resultado es la imagen de umbral .
# El primer argumento es la imagen de origen, que debería ser una imagen en escala de grises
#  El segundo argumento es el valor de umbral que se utiliza para clasificar los valores de píxeles
# El tercer argumento es el valor máximo que se asigna a los valores de píxeles que superan el umbra
'''
#Contorno
contorno,jerarquia= cv2.findContours(umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

'''
 
# Los contornos son una herramienta útil para el análisis de formas y la detección y reconocimiento de objetos.
# antes de encontrar contornos, aplique el umbral o la detección de bordes astutos.
# findContours (1,2,3) el primero es la imagen de origen, 2 modo de recuperacion del contorno, 3 metodo de aproximacion de contorno.
'''

# OPERACION PARA MOSTRAR LA IMAGEN
cv2.drawContours(imagen,contorno,-1,(251,63,52),5)
'''
Su primer argumento es la imagen de origen,
el segundo argumento son los contornos
el tercer argumento es el índice de contornos (útil cuando se dibujan contornos individuales. Para dibujar todos los contornos, pase -1)
el cuarto color
el ultimo es el grosor

'''

#cv2.imshow('imagen en grises',grises)  #primer avance.
# inshow sirve para mostrar una imagen, (1,2) 1 es el titulo de la ventana que muestra la imagen, el 2 es la variable que quiero mostrar.
cv2.imshow('imagen original',imagen)
#cv2.imshow('imagen umbral',umbral) # segundo avance.
cv2.waitKey(0)   #Declaracion para que el modo de la ventana permanezca estatica o visible. El valor 1 es para camara web o video.
cv2.destroyAllWindows() # Destruye todas las ventanas que estan abiertas.



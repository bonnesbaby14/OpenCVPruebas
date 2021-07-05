import sys
import cv2 as cv
import numpy as np
from funciones import dibujar
#convertir una imgaen en gris__________________________
#imagen = cv.imread("uno.png",0)

#cv.imshow("prueba de imagen", imagen)
#cv.imwrite("imgaengris.png",imagen);

#cv.waitKey(0)

#cv.destroyAllWindows();

#capturar desde una camara__________________--


#captura=cv.VideoCapture(0);
#salida=cv.VideoWriter("videosalida.mp4", cv.VideoWriter_fourcc(*'XVID'),20.0,(640,480))
#while(captura.isOpened()):
 #   ret,imagen=captura.read()
  #  if ret==True:
   #     cv.imshow("video",imagen)
    #    salida.write(imagen)
     #   if cv.waitKey(1)==ord("a"):
            #break
#captura.release()
#salida.release()
#cv.destroyAllWindows()


#detectar colores
"""
captura=cv.VideoCapture(0)

redBajo1 = np.array([0, 70, 20], np.uint8)
redAlto1 = np.array([8, 255, 255], np.uint8)

redBajo2=np.array([175, 70, 20], np.uint8)
redAlto2=np.array([179, 255, 255], np.uint8)



while(captura.isOpened()):
    ret,imagen=captura.read()
    if ret==True:
        
        frameHSV=cv.cvtColor(imagen,cv.COLOR_BGR2HSV)
        maskRed1 = cv.inRange(frameHSV, redBajo1, redAlto1)
        maskRed2 = cv.inRange(frameHSV, redBajo2, redAlto2)
        
        maskRed = cv.add(maskRed1, maskRed2)
        
        maskRedvis=cv.bitwise_and(imagen,imagen,mask=maskRed)
        cv.imshow('Colores rojo', maskRedvis)
        cv.imshow("Original",imagen)
        
  
        if cv.waitKey(1)==ord("a"):
            break
captura.release()
cv.destroyAllWindows()

"""

#detectar coloresy contornealos con cordenadas
captura=cv.VideoCapture(0)

redBajo1 = np.array([0, 50, 20], np.uint8)
redAlto1 = np.array([8, 255, 255], np.uint8)

redBajo2=np.array([175, 50, 20], np.uint8)
redAlto2=np.array([179, 255, 255], np.uint8)

azulBajo=np.array([100, 100, 20], np.uint8)
azulAlto=np.array([125, 255, 255], np.uint8)

amarilloBajo=np.array([15, 100, 20], np.uint8)
amarilloAlto=np.array([45, 255, 255], np.uint8)

while(captura.isOpened()):
    ret,imagen=captura.read()
    if ret==True:
        
        frameHSV=cv.cvtColor(imagen,cv.COLOR_BGR2HSV)
        
        maskAzul= cv.inRange(frameHSV,azulBajo,azulAlto)
        maskAmarillo= cv.inRange(frameHSV,amarilloBajo,amarilloAlto)
        
        maskRed1 = cv.inRange(frameHSV, redBajo1, redAlto1)
        maskRed2 = cv.inRange(frameHSV, redBajo2, redAlto2)
        
        maskRed = cv.add(maskRed1, maskRed2)

        dibujar(maskAzul,(255,0,0),cv,imagen)
        dibujar(maskAmarillo,(0,255,255),cv,imagen)
        dibujar(maskRed,(0,0,255),cv,imagen)
        
        
        
        
        
        
     
       # cv.imshow('Colores rojo', maskRedvis)
        cv.imshow("Original",imagen)
        
  
        if cv.waitKey(1)==ord("a"):
            break
captura.release()
cv.destroyAllWindows()
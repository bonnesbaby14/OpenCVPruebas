import sys
import cv2 as cv
import numpy as np

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



while(captura.isOpened()):
    ret,imagen=captura.read()
    if ret==True:
        
        frameHSV=cv.cvtColor(imagen,cv.COLOR_BGR2HSV)
        maskRed1 = cv.inRange(frameHSV, redBajo1, redAlto1)
        maskRed2 = cv.inRange(frameHSV, redBajo2, redAlto2)
        
        maskRed = cv.add(maskRed1, maskRed2)
        
        maskRedvis=cv.bitwise_and(imagen,imagen,mask=maskRed)
        
        
        contornos,_=cv.findContours(maskRed, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        
        
        for c in contornos:
            area=cv.contourArea(c)
            if area>5000:
                M=cv.moments(c)
                if(M["m00"]==0):M["m00"]=1
                x=int(M["m10"]/M["m00"])
                y=int(M["m01"]/M["m00"])
                cv.circle(imagen,(x,y), 7, (255,0,0))
                
                nuevoContorno=cv.convexHull(c)
                cv.drawContours(imagen, [nuevoContorno], 0, (255,0,0),3)        
        
     
       # cv.imshow('Colores rojo', maskRedvis)
        cv.imshow("Original",imagen)
        
  
        if cv.waitKey(1)==ord("a"):
            break
captura.release()
cv.destroyAllWindows()
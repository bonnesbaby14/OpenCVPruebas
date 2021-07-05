#funciones para cada color


def dibujar(mask, color,cv,imagen):
    contornos,_=cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        
        
    for c in contornos:
        area=cv.contourArea(c)
        if area>2000:
            M=cv.moments(c)
            if(M["m00"]==0):M["m00"]=1
            x=int(M["m10"]/M["m00"])
            y=int(M["m01"]/M["m00"])
            cv.circle(imagen,(x,y), 7, (255,0,0))
              
                
            font=cv.FONT_HERSHEY_SIMPLEX
            
            cv.putText(imagen,'{},{}'.format(x,y), (x+10,y), font, 0.75,(0,255,0),1,cv.LINE_AA)
                
            nuevoContorno=cv.convexHull(c)
            cv.drawContours(imagen, [nuevoContorno], 0, color,3)        
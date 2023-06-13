import cv2
import numpy as np
from threading import Timer

def Pass():
    pass

def Menu():
    a=input("Introduzca modo de operacion\n1) Tomar foto y cerrar\n2) Introducir numero maximo de fotos antes de cerrar\n3) Funcionamiento continuo\n>")
    if (a=="1"):
        iniciar_detectando(1)
    elif (a=="2"):
        b=input("Introduzca el numero maximo de fotos\n>")
        iniciar_detectando(int(b))
    elif(a=="3"):
        iniciar_detectando(0)


def iniciar_detectando(max):
    cap = cv2.VideoCapture(1)
    i=0
    j=0
    b=False
    c=False
    sonrisa = cv2.CascadeClassifier('haarcascade_smile.xml')
    flash= np.ones((300, 300, 3), np.uint8) * 255
    while True:
        
        ret,frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame2=frame.copy()

        toy = sonrisa.detectMultiScale(gray,
        scaleFactor = 3,
        minNeighbors = 31,
        minSize=(40,48))
        for (x,y,w,h) in toy:
            
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),6)
            cv2.putText(frame,'Sonrisa',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)
            i+=1
        if i>40: 
            j+=1
            try:
                cv2.imwrite('fotos/foto{}.jpg'.format(j),frame2)
                print('Foto tomada: ', 'foto{}.jpg'.format(j))
                i=0
                frame=flash
                b=True
            except:
                print('Foto no almacenada')
                i=0
            if(j>0):
                if(j==max):
                    c=True
                    break
        cv2.imshow('frame',frame)
        if c:
            break
        if b:
            t = Timer(2, Pass)  
            t.start()
            b=False

        if cv2.waitKey(1) == ord('x'):
            break
    cap.release()
    cv2.destroyAllWindows()

Menu()
#iniciar_detectando(0)
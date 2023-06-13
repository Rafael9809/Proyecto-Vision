import threading
import time
import datetime
import logging
import pwm
import detectando

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] (%(threadName)-s) %(message)s')

tiempo_ini = datetime.datetime.now()

class Hilos(threading.Thread):
    def __init__(self, target1, nombre):
#         tstr="{0}.iniciar_{0}".format(target1)
#         print(tstr)
        threading.Thread.__init__(self, name=nombre, target=target1, args=())
# t1=threading.Thread(name="hilo_pwm",target=pwm.iniciar_pwm, args=())
# t2=threading.Thread(name="hilo_camara",target=detectando.iniciar_detectando, args=())
t1= Hilos(pwm.iniciar_pwm,"HILO_PWM")
t2= Hilos(detectando.iniciar_detectando,"HILO_Detectando")


t1.start()
t2.start()

t1.join()
t2.join()


tiempo_fin = datetime.datetime.now()

#print("Tiempo transcurrido: "+str(tiempo_fin.second-tiempo_ini.second))
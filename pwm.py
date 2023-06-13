import RPi.GPIO as GPIO  
import time
import logging

def iniciar_pwm():
    logging.info("Iniciado log en pwm")
    GPIO.setmode(GPIO.BOARD)  
                               
    GPIO.setwarnings(False)
    GPIO.setup(32, GPIO.OUT) 
    pwmx = GPIO.PWM(32, 50)    
    GPIO.setup(33, GPIO.OUT)
    pwmy = GPIO.PWM(33, 50)  

    # main loop of program
    #print("\nPress Ctl C to quit \n") 
    dc=60                               
    pwmx.start(50)
    pwmy.start(50)
    pwmx.ChangeDutyCycle(5)
    pwmy.ChangeDutyCycle(5)
    boolxd=True
    while boolxd:
        #pass
     try:
         cambio1=input('Ingrese dirección\nIzquierda (I), Derecha (D), Centro (C), \nPara cambiar a maxima velocidad presione "M"\nPara salir presione "S"\n>')
         if cambio1=='I':
             pwmx.ChangeDutyCycle(5)
             pwmy.ChangeDutyCycle(7)
         elif cambio1=='D':
             pwmx.ChangeDutyCycle(7)
             pwmy.ChangeDutyCycle(5)
         elif cambio1=='C':
             pwmx.ChangeDutyCycle(8)
             pwmy.ChangeDutyCycle(8)
         elif cambio1=='M':
             pwmx.ChangeDutyCycle(10)
             pwmy.ChangeDutyCycle(10)
         elif cambio1=='S':
             boolxd=False
         else:
             print('Opcion incorrecta\n')
                     
    #   while True:                     
    #     for dc in range(0, 101, 5):   
    #       pwm.ChangeDutyCycle(dc)
    #       time.sleep(0.05)             
    #       print(dc)
    #     for dc in range(95, 0, -5):    
    #       pwm.ChangeDutyCycle(dc)
    #       time.sleep(0.05)             
    #       print(dc)
     except KeyboardInterrupt:
          print("Ctl C pressed - ending program")

    pwmx.stop()
    pwmy.stop()
    GPIO.cleanup()
    
iniciar_pwm()


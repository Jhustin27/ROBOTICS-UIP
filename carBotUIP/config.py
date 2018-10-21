import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
class CarRobot:
    Motor1A = 16
    Motor1B = 18
    Motor1E = 22
    
    Motor2A = 23
    Motor2B = 21
    Motor2E = 19
    # Establecemos el tiempo en 5 defecto
    tiempo = 1
    nombre = ''
    def __init__(self, nombre, tiempo = None):
        print("Configurando CarRobot me llamo {}".format(nombre))
        if tiempo is not None:
            self.tiempo = tiempo
        if nombre is not None:
            self.nombre = nombre
        self.encender()

    def encender(self):
        """ Encendiendo CarRobot """
        print(self.encender.__doc__)        
        GPIO.cleanup()
        self.salir()
        # Configuracion de pines
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.Motor1A,GPIO.OUT)
        GPIO.setup(self.Motor1B,GPIO.OUT)
        GPIO.setup(self.Motor1E,GPIO.OUT)
        
        GPIO.setup(self.Motor2A,GPIO.OUT)
        GPIO.setup(self.Motor2B,GPIO.OUT)
        GPIO.setup(self.Motor2E,GPIO.OUT)
        sleep(self.tiempo)
 
    def adelante(self):
        """ Acelerando CarRobot"""
        print(self.adelante.__doc__)
        GPIO.output(self.Motor1A,GPIO.HIGH)
        GPIO.output(self.Motor1B,GPIO.LOW)
        GPIO.output(self.Motor1E,GPIO.HIGH)
        
        GPIO.output(self.Motor2A,GPIO.HIGH)
        GPIO.output(self.Motor2B,GPIO.LOW)
        GPIO.output(self.Motor2E,GPIO.HIGH)
    
        sleep(self.tiempo)

    def atras(self):
        """ Retrocediendo CarRobot"""
        print(self.atras.__doc__)
        GPIO.output(self.Motor1A,GPIO.LOW)
        GPIO.output(self.Motor1B,GPIO.HIGH)
        GPIO.output(self.Motor1E,GPIO.HIGH)
        
        GPIO.output(self.Motor2A,GPIO.HIGH)
        GPIO.output(self.Motor2B,GPIO.HIGH)
        GPIO.output(self.Motor2E,GPIO.LOW)
    
        sleep(self.tiempo)

    #Motores derechos
    def ir_derecha(self):
        """ Girando CarRobot hacia la Derecha"""
        print(self.ir_derecha.__doc__)
        GPIO.output(self.Motor1A,GPIO.LOW)
        GPIO.output(self.Motor1B,GPIO.LOW)
        GPIO.output(self.Motor1E,GPIO.LOW)
        
        GPIO.output(self.Motor2A,GPIO.HIGH)
        GPIO.output(self.Motor2B,GPIO.LOW)
        GPIO.output(self.Motor2E,GPIO.HIGH)
        
        sleep(self.tiempo)

    #Motores Izquierdos
    def ir_izquierda(self):
        """ Girando CarRobot hacia la Izquierda"""
        print(self.ir_izquierda.__doc__)
        GPIO.output(self.Motor1A,GPIO.HIGH)
        GPIO.output(self.Motor1B,GPIO.LOW)
        GPIO.output(self.Motor1E,GPIO.HIGH)
        
        GPIO.output(self.Motor2A,GPIO.LOW)
        GPIO.output(self.Motor2B,GPIO.LOW)
        GPIO.output(self.Motor2E,GPIO.LOW)
        
        sleep(self.tiempo)

    def apagar(self):
        """ Apagando CarRobot """
        print(self.apagar.__doc__,self.nombre)
        GPIO.output(self.Motor1E,GPIO.LOW)
        GPIO.output(self.Motor2E,GPIO.LOW)
        #GPIO.cleanup() 
        sleep(self.tiempo)

    def salir(self):
        """ Desconentando CarRobot """
        print(self.salir.__doc__, self.nombre)
        GPIO.cleanup()

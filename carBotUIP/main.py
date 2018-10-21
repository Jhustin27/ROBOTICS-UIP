from config import CarRobot
from bot import bot_init
import os
def main():
    try:
        bot_init()
    except KeyboardInterrupt:
        carRobot.salir()
        os.system('clear')
        print("Saliendo del carRobot con ChatBot")
    except Exception as error:
        print(error)
   
    


if __name__ == '__main__':
     main()

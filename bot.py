import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep

print("Initiating...")

#Definir la clase del bot
class DiingoBot:

    #Inicializador de la clase
    def __init__(self, speed=.7, click_speed=.7):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ""
        self.last_message = ""

    #Método para que el programa detecte los puntos con mensajes nuevos
    #Solo funciona en modo oscuro whatsapp
    def navigation(self):
        try:
            pos = pt.locateOnScreen("assets/new_message.png", confidence = .7)
            pt.moveTo(pos[0:2], duration=self.speed)
            pt.moveRel(-100, 0, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception: ', e)

startBot = DiingoBot(speed=.7, click_speed=.7)
sleep(4)
startBot.navigation()

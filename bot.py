import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep
from responses import Responses

mouse = Controller()
res = Responses()

print("Initiating...")

#Definir la clase del bot
class DiingoBot:

    #Inicializador de la clase
    def __init__(self, speed=.7, click_speed=.7):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ""
        self.last_message = ""
        self.message_point = -1
    #Método para que el programa detecte los puntos con mensajes nuevos
    #Solo funciona en modo oscuro whatsapp
    def navigation(self):
        try:
            pos = pt.locateOnScreen("assets/new_message.png", confidence = .7)
            pt.moveTo(pos[0:2], duration=self.speed)
            pt.moveRel(-100, 0, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception: (navigation)', e)

    def box_input(self):
        try:
            pos = pt.locateOnScreen("assets/file.png", confidence = .7)
            pt.moveTo(pos[0:2], duration=self.speed)
            pt.moveRel(100, 15, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception: (box_input) ', e)
    
    def get_message(self):
        try:
            pos = pt.locateOnScreen("assets/file.png", confidence = .7)
            pt.moveTo(pos[0:2], duration=self.speed)
            #pt.moveRel(890, -50, duration=self.speed)
            pt.moveRel(45, -50, duration=self.speed)
        except Exception as e:
            print('Exception: (get_message) ', e)
        
    def closeRespondBox(self):
        try:
            pos = pt.locateOnScreen("assets/closeRespond.png", confidence = .8)
            pt.moveTo(pos[0:2], duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
            pt.moveRel(30, 30, duration=self.speed)
        except Exception as e:
            print('Exception: (closeRespondeBox)', e)

    def copy_message(self):
        pt.doubleClick(interval=.3)
        #sleep(self.speed)
        mouse.click(Button.left, 3)
        sleep(self.speed)
        pt.keyDown('ctrl')
        pt.press('c')
        pt.keyUp('ctrl')

        self.message = pc.paste()
        print('Message: ', self.message)
    
    def send_message(self):
        try:
            self.message_point += 1
            bot_reply = res.response(self.message)
            print(bot_reply)
            pt.typewrite(bot_reply, interval=.01)
            pt.typewrite('\n')

            self.last_message = self.message

        except Exception as e:
            print('Exception: (send_message) ', e)
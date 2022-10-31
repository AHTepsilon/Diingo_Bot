import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep
from responses import response

mouse = Controller()

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
            pt.moveRel(850, -50, duration=self.speed)
            #pt.moveRel(50, -50, duration=self.speed)
        except Exception as e:
            print('Exception: (get_message) ', e)

    def copy_message(self):

        
        pt.doubleClick(interval=.3)
        sleep(self.speed)
        mouse.click(Button.left, 3)
        sleep(self.speed)
        pt.keyDown('ctrl')
        pt.press('c')
        pt.keyUp('ctrl')
        #mouse.click(Button.right, 1)
        #sleep(self.speed)
        #pt.moveRel(30, -260, duration=self.speed)
        #mouse.click(Button.left, 1)
        #sleep(1)

        self.message = pc.paste()
        print('Message: ', self.message)
    
    def send_message(self):
        try:
            if self.message != self.last_message:
                self.message_point += 1
                bot_reply = response(self.message, self.message_point)
                print(bot_reply)
                pt.typewrite(bot_reply, interval=.01)
                pt.typewrite('\n')

                self.last_message = self.message
            else:
                print('Nothing new...')
        except Exception as e:
            print('Exception: (send_message) ', e)

startBot = DiingoBot(speed=.7, click_speed=.7)
sleep(4)

while True:
    startBot.navigation()
    startBot.get_message()
    startBot.copy_message()
    startBot.box_input()
    startBot.send_message()

    sleep(10)
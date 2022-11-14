from bot import DiingoBot
from time import sleep

newBot = DiingoBot(speed=.7, click_speed=.7)
sleep(4)

while True:
    newBot.navigation()
    newBot.get_message()
    newBot.closeRespondBox()
    newBot.copy_message()
    newBot.box_input()
    newBot.send_message()

    sleep(10)
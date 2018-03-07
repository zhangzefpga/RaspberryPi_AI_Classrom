#Expert System Game Demo
#Hardware : Raspberry Pi,led*3,key*4
#Linux Version : Raspbian
#Python Version : 3.5

import RPi.GPIO as GPIO
import time
from random import randint

led_tie = 4        #tie led
led_p_win = 17     #player win led
led_p_lose = 27    #player lose led

key_paper = 12     #paper key
key_scissors = 16  #scissors key
key_rock = 20      #rock key
key_exit = 21      #exit key

paper = 1
rock = 2
scissors = 3 

#Setup GPIUO pins
#Set the BCM mode
GPIO.setmode(GPIO.BCM)    

GPIO.setwarnings(False)   

#Outputs
GPIO.setup(led_tie,GPIO.OUT)
GPIO.setup(led_p_win,GPIO.OUT)
GPIO.setup(led_p_lose,GPIO.OUT)

#Ensure all LEDs are off to start
GPIO.output(led_tie,GPIO.LOW)
GPIO.output(led_p_win,GPIO.LOW)
GPIO.output(led_p_lose,GPIO.LOW)

#Inputs
GPIO.setup(key_paper,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(key_scissors,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(key_rock,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(key_exit,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

global player
player = False

#Setup the callback functions
def paper(channel):
    global player
    player = 1
    print("player=paper")

def rock(channel):
    global player
    player = 2
    print("player=rock")

def scissors(channel):
    global player
    player = 3
    print("player=scissors")

def quit(channel):    #don't use "exit(channel)"
    print("exit!")
    exit()
    
#Add event detection and callback assignments
GPIO.add_event_detect(key_paper, GPIO.RISING, callback=paper)
GPIO.add_event_detect(key_scissors, GPIO.RISING, callback=scissors)
GPIO.add_event_detect(key_rock, GPIO.RISING, callback=rock)
GPIO.add_event_detect(key_exit, GPIO.RISING, callback=quit)

#computer random pick
computer = randint(1,3)

print("Game Start! rock, paper or scissors?")
while True:
    
    if player == computer:   
        GPIO.output(led_tie,GPIO.HIGH)
        print("Tie!Computer = Player" )
        time.sleep(3)
        GPIO.output(led_tie,GPIO.LOW)
        player = 0
    elif player == 2:
        if computer == 1:
            GPIO.output(led_p_lose,GPIO.HIGH)
            print("Player Lose! Computer is paper!")
            time.sleep(3)
            GPIO.output(led_p_lose,GPIO.LOW)
            player = 0
        else:
            GPIO.output(led_p_win,GPIO.HIGH)
            print("Player Win! Computer is scissors!")
            time.sleep(3)
            GPIO.output(led_p_win,GPIO.LOW)
            player = 0
    elif player == 1:
        if computer == 3:
            GPIO.output(led_p_lose,GPIO.HIGH)
            print("Player Lose! Computer is scissors!")
            time.sleep(3)
            GPIO.output(led_p_lose,GPIO.LOW)
            player = 0
        else:
            GPIO.output(led_p_win,GPIO.HIGH)
            print("Player Win! Computer is rock!")
            time.sleep(3)
            GPIO.output(led_p_win,GPIO.LOW)
            player = 0
    elif player == 3:
        if computer == 2:
            GPIO.output(led_p_lose,GPIO.HIGH)
            print("Player Lose! Computer is rock!")
            time.sleep(3)
            GPIO.output(led_p_lose,GPIO.LOW)
            player = 0
        else:
            GPIO.output(led_p_win,GPIO.HIGH)
            print("Player Win! Computer is paper!")
            time.sleep(3)
            GPIO.output(led_p_win,GPIO.LOW)
            player = 0
        
    computer = randint(1,3)
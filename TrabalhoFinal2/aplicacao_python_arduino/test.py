from asyncio.windows_events import NULL
import pyfirmata
import time
from ast import If, While
from pickle import TRUE
from tkinter import *
from pyfirmata import Arduino, SERVO
from time import sleep

board = pyfirmata.Arduino('COM3')
pin = 9
board.digital[pin].mode = SERVO
it = pyfirmata.util.Iterator(board)  
it.start()  

blk = TRUE

def rotateServo(pin , angle): #Posicionar o servo 
    board.digital[pin].write(angle)

def servoctrl(angle):
    if angle == "":
        rotateServo(pin, "0")
    else:
        rotateServo(pin, angle)

def ledon (p):
    board.digital[p].write(1)

def ledoff (p):
    board.digital[p].write(0)

def Blink():
    global blk
    blk = TRUE

    global alarm
    alarm = "Ligado!"
    print(alarm)

    while blk == TRUE :
        board.digital[4].write(1)
        sleep(0.1)
        board.digital[4].write(0)
        sleep(0.1)

def Blinkoff():

    global alarm
    alarm = "Desligado!"
    print(alarm)

    global blk
    blk = FALSE
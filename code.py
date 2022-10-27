from tkinter import *
import time
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.GPIO)

tinker = tkinter.Tk()
tinker.title("Morse Code")
myFont = tkinter.font.Font(family = 'Helvetica', 
size=14, weight="bold")
name = tkinter.StringVar()

morse_dict = {
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..'
}

led = LED(9)


def text_to_morse(string):
    morse_stirng=""
    for c in string:
        morse_stirng += morse_dict[c.upper()]
        morse_stirng+=' '
    return morse_stirng
    

def morse():
    led.off()
    string1 = entry.get()
    if string1.count(string1) > 12:
        exit()
    else:
        print(string1)
        morse_code = text_to_morse(string1)
        print(morse_code)
        for c in morse_code:
            for morse in c:
                if morse == '.':
                    led.on()
                    time.sleep(0.3)
                    led.off()
                elif morse =='-':
                    led.on()
                    time.sleep(0.6)
                    led.off()
            time.sleep(1)
        

def exit():
    led.off()
    GPIO.cleanup()
    tinker.destroy()

entry_label = tkinter.Label(tinker , text= 'Name', font=myFont)
entry = Entry(tinker, textvariable=name, font=myFont, width=30)
b = Button(tinker, text="MORSE CODE", font=myFont, bg='bisque2', height=1, width=25 )

entry_label.grid(row=0, column=3)
entry.grid(row=1, column=3)
b.grid(row=2, column=3)

tinker.protocol("WM_DELETE_WINDOW", exit)
tinker.mainloop()



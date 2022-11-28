##libraries
from tkinter import *
import time
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.GPIO)

##creating a GUI instance
tinker = tkinter.Tk()
##title of the GUI
tinker.title("Morse Code")
##selecting a font for the GUI
myFont = tkinter.font.Font(family = 'Helvetica', 
size=14, weight="bold")
##creating a string based variable for the GUI. The user input woudl be stored here.
name = tkinter.StringVar()

##a dictionary, containing each english alphabet and its corresponding morse code
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

##defining a LED.
led = LED(9)

##text to morse function: Takes in a simple string consisting of english alphabets, and converts the string to morse code using the morse dictionary. The new morse 
##string created is returned.
def text_to_morse(string):
    morse_stirng=""
    for c in string:
        morse_stirng += morse_dict[c.upper()]
        morse_stirng+=' '
    return morse_stirng
    

##main function: 






def morse():
    ## user input is taken, led is initially set to off.
    led.off()
    string1 = entry.get()
    ## if the number of characters in the string surpasses 12, we simply exit
    if string1.count(string1) > 12:
        exit()
    else:
        ## we print the input, corresponding morse code
        print(string1)
        morse_code = text_to_morse(string1)
        print(morse_code)
        ## then, using the led, we blink the morse code string.
        for c in morse_code:
            for morse in c:
                ## for each dot, we turn the LED on for 0.3 s, 
                if morse == '.':
                    led.on()
                    time.sleep(0.3)
                    led.off()
                ##for each dash, we turn it on for 0.6s
                elif morse =='-':
                    led.on()
                    time.sleep(0.6)
                    led.off()
            ## between each letter we put a delay of 1 second
            time.sleep(1)
        
###simple exit function which destroys the GUI instance, turns off the led and sets all GPIO pins to default, i.e., input mmode
def exit():
    led.off()
    GPIO.cleanup()
    tinker.destroy()

##entry label entry widget
entry_label = tkinter.Label(tinker , text= 'Name', font=myFont)
## entry widget to take in the user input
entry = Entry(tinker, textvariable=name, font=myFont, width=30)
##button to begin the process
b = Button(tinker, text="MORSE CODE", font=myFont, bg='bisque2', height=1, width=25 )

##layout of GUI
entry_label.grid(row=0, column=3)
entry.grid(row=1, column=3)
b.grid(row=2, column=3)

## if the user clicks on the cross button to exit, we catch the event and run the exit function to cleanly exit
tinker.protocol("WM_DELETE_WINDOW", exit)
## loop for running the GUI
tinker.mainloop()



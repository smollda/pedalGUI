import serial
import serial.tools.list_ports
import time
import tkinter
from tkinter import *

ser = serial.Serial()
def quit():
    global tkTop
    ser.write(bytes('L', 'UTF-8'))
    tkTop.destroy()

def set_button1_state():
        global b
        b += 1
        #varLabel.set("LED ON ")
        ser.write(bytes('H', 'UTF-8'))
        cc=str(ser.readline())
        print(cc[2:][:-5])
        varLabel.set(cc[2:][:-5])
        
    

def set_button2_state():
        varLabel.set("LED OFF")
        ser.write(bytes('L', 'UTF-8'))

tkTop = tkinter.Tk()
tkTop.geometry('300x600')
tkTop.title("IoT24hours")

def on_select(selection):
    # open the port and command it to start the LED blinking here
    
    print(selection.name)
    ser.port = selection.name
    ser.baudrate = 19200
    ser.open()
    if ser.is_open:
        print ("Port otevřen")
    

ports = serial.tools.list_ports.comports()
default = StringVar(tkTop, "Please Select Port")
OptionMenu(tkTop, default, *ports, command=on_select).pack()

label3 = tkinter.Label(text = 'Building Python GUI to interface an arduino,'
                      '\n and control an LED',font=("Courier", 12,'bold')).pack()
tkTop.counter = 0
b = tkTop.counter

varLabel = tkinter.IntVar()
tkLabel = tkinter.Label(textvariable=varLabel, )
tkLabel.pack()

varLabel2 = tkinter.IntVar()
tkLabel2 = tkinter.Label(textvariable=varLabel2, )
tkLabel2.pack()

button1 = tkinter.IntVar()
button1state = tkinter.Button(tkTop,
    text="ON",
    command=set_button1_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button1state.pack(side='top', ipadx=10, padx=10, pady=15)

button2 = tkinter.IntVar()
button2state = tkinter.Button(tkTop,
    text="OFF",
    command=set_button2_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5
)
button2state.pack(side='top', ipadx=10, padx=10, pady=15)

tkButtonQuit = tkinter.Button(
    tkTop,
    text="Quit",
    command=quit,
    height = 4,
    fg = "black",
    width = 8,
    bg = 'yellow',
    bd = 5
)
tkButtonQuit.pack(side='top', ipadx=10, padx=10, pady=15)
tkinter.mainloop()
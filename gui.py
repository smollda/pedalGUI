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
        if not ser.is_open:
            varLabel.set("COM port not open!")
        #varLabel.set("LED ON ")
        ser.write(bytes('k', 'UTF-8'))

        cc=str(ser.readline())
        cc2=str(ser.readline())
        cc3=str(ser.readline())
        cc4=str(ser.readline())
        varLabel.set("Calibrating ...")
        varLabel2.set("Press all 3 pedals multiple times during the next 10 seconds \n (brake pedal to the maximum desired value)")
        tkTop.update_idletasks()
        time.sleep(10)
        varLabel.set(" ")
        varLabel2.set("Done  \n")

        
tkTop = tkinter.Tk()
tkTop.geometry('600x300')
tkTop.title("pedalBoard control")

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
if not ports:
     OptionMenu(tkTop, default, 'No port found', command=on_select).pack()
else:
    OptionMenu(tkTop, default, *ports, command=on_select).pack()


varLabel = tkinter.StringVar()
tkLabel = tkinter.Label(textvariable=varLabel, )
tkLabel.pack()


varLabel2 = tkinter.StringVar()
varLabel2.set(" \n")
tkLabel2 = tkinter.Label(textvariable=varLabel2, )
tkLabel2.pack()

button1 = tkinter.IntVar()
btn_text = tkinter.StringVar()
button1state = tkinter.Button(tkTop,    
    textvariable=btn_text,
    command=set_button1_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
btn_text.set("Calibrate")
button1state.pack(side='top', ipadx=40, padx=10, pady=15)

# button2 = tkinter.IntVar()
# button2state = tkinter.Button(tkTop,
#     text="Calibrate Fanatec shifter",
#     command=set_button2_state,
#     height = 4,
#     fg = "black",
#     width = 8,
#     bd = 5
# )
# button2state.pack(side='top', ipadx=40, padx=10, pady=15)



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
tkButtonQuit.pack(side='bottom', ipadx=40, padx=10, pady=15)

tkinter.mainloop()
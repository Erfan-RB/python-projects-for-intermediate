#Digital-Clock
from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Clock')

#Time Function
def time():
    string = strftime('%H:%M:%S %P')
    lbl.config(text=string)
    lbl.after(1000, time)

#Style
lbl = Label(root, font=('calibri', 40, 'bold'),
            background="purple",
            foreground="white")

lbl.pack(anchor='center')
time()          

mainloop()  

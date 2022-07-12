from tkinter import *
import webbrowser
import tkinter.font as font
from tkinter.ttk import *

root = Tk()
root.geometry('370x200')

e = Entry(root,width=20,)
e.grid(row=1, column=1)
e.insert(0, 'Enter Your Name:')

new = 1
url = 'https://discord.gg/sw2PnkHP2T'
url2 = 'https://www.roblox.com/' 
f1 = font.Font(size=10)
f2 = font.Font(size=16)
#Welcome Label
LB1 = Label(root, text= 'Welcome to IMine')
LB1.grid(row=0, column=1)
LB1['font'] = f2


def myClick():
     webbrowser.open(url,new=new)
     LB2 = Label(root, text='   Hello: ' + e.get() + ' Welcome to IMine Discord Server')
     LB2.grid(row=2,column=1)
     LB2['font'] = f1


#Style
style = Style()
style.configure('TButton', font =
               ('calibri', 12, 'bold'),
                    borderwidth = '4')

style.map('TButton', foreground = [('active', '!disabled', 'cyan1')],
                     background = [('active', 'black')])

def myClick2():
    webbrowser.open(url2,new=new)
#Discord Button
btn1 = Button(root, text='Discord', command=myClick)
btn1.grid(row=2,column=0)

#Roblox Button 
btn2 = Button(root, text='Roblox',command=myClick2)
btn2.grid(row=3,column=0)

root.mainloop()

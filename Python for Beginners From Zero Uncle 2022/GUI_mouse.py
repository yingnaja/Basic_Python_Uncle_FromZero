from cgitb import text
from tkinter import *
from tkinter import ttk
import pyautogui as pg
import webbrowser

GUI = Tk()
GUI.title('Program Calender')
GUI.geometry('500x300')

def Calender1():
    pg.click(1885, 1051)

def Calender2():
    pg.click(439, 1045)

def Google():
    webbrowser.open('https://www.google.com')

B1 = Button(GUI, text='Calender1', command=Calender1)
B1.pack(ipadx=20, ipady=10, pady=20)

B2 = ttk.Button(GUI, text='Calender2', command=Calender2)
B2.pack(ipadx=20, ipady=10, pady=20)

B3 = ttk.Button(GUI, text='Calender3', command=Google)
B3.pack(ipadx=20, ipady=10)

GUI.mainloop()


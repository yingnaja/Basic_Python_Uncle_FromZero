from cgitb import text
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox

GUI = Tk()
GUI.title('Program Calculater') ### ชื่อโปรแกรม

GUI.geometry('500x700')         ### ขนาดหน้าจอโปรแกรม

 ### iconarchive  การใส่รูปภาพ
bg = PhotoImage(file='images/Cars.png')   ### เก็บปภาพ
BG = Label(GUI, image=bg)  
BG.pack()              ### แสดงรูปภาพ

L = Label(GUI, text="กรุณากรอกจำนวนปลา(กิโลกรัม)", font=(None, 20))
L.pack()  ## ป้ายแสดงชื่อ


v_quantity = StringVar()  ## สร้างตัวแปรเป็นตัวหนังสือ
E1 = ttk.Entry(GUI, textvariable=v_quantity, font=(None, 20)) ### ช่องกรอกข้อมูล
E1.pack()

#### function
def Cal():
    try:
        quan = float(v_quantity.get())
        price = 30
        calc = quan * price
        messagebox.showinfo('รวมราคาทั้งหมด', f'ราคาปลาทั้งหมด {calc:.2f} บาท')
        v_quantity.set('')
    except:
        messagebox.showwarning('กรอกจำนวนผิด','กรุณากรอกเฉพาะตัวเลขเท่านั้น')
        v_quantity.set('')

B1 = ttk.Button(GUI, text="Calculate", command=Cal)
B1.pack(ipadx=20, ipady=20)  ### ipadx , ipady ขยายความกว้างภายในปุ่ม


GUI.mainloop()   ## เพื่อให้โปรแกรมทำงานตอลดเวลา
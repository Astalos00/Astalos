from tkinter import *
from bazooka import *
from roquette import *

def create_roquette():
    can.delete(r1)
    r1 = Roquette(can,b1.x2,b1.y2, 'red')

def delete_roquette():
    can.delete(r1)

# Code pour tester sommairement la classe Bazouka :
f = Tk()
can = Canvas(f,width =500, height =250, bg ='ivory')
can.pack(padx =10, pady =10)
b1 = Bazooka(can, 50, 200)
 
s1 =Scale(f, label='hausse', from_=90, to=0, command=b1.orienter)
s1.pack(side=LEFT, pady =5, padx =20)
s1.set(25)                          # angle de tir initial

#button tir
buttir=Button(f, text='feu',command=create_roquette)
buttir.pack(side=LEFT, pady=20, padx=20)

#button delete roquette
butdelete=Button(f, text='delete',command=delete_roquette)
butdelete.pack(side=RIGHT, pady=20, padx=20)

f.mainloop()

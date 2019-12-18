from tkinter import *
from math import pi, sin, cos

class Roquette(object):
    def __init__(self, parent, Xroquette, Yroquette, coul):
        self.parent = parent
        self.Xroquette=Xroquette
        self.Yroquette=Yroquette
        self.r=self.parent.create_oval(self.Xroquette-5, self.Yroquette-5, self.Xroquette+5, self.Yroquette+5, fill=coul)

    def destroy(self):
        self.parent.delete(self.r)

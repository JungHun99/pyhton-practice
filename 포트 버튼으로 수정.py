import tkinter as tk
import tkinter.font as font

class App:
    def _init_(self):
        root=tk.Tk()

        self.customFont=font.Fount(family="Helvetica",size=12)

        label=tk.Label(root,text="Hello Word",font=self.customFont)
        label.pack()
        buttonframe=tk.Frame()
        buttonframe.pack()

        bigger=tk.Button(buttonframe,text="폰트를 크게",command=self.BigFont)
        smaller=tk.Button(buttonframe,text="폰트를 작게",command=self.SmallFont)
        bigger.pack()
        smaller.pack()

    def BigFont():
        size=self.customFont['size']
        self.customFont.configure(size=size+2)

    def SmalFont():
        size=self.customFont['size']
        self.customFont.configure(size=size-2)



app=App()

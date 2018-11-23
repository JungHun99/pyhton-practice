from tkinter import*

def main():
    global var
    window=Tk()
    var=StringVar()
    hi()

def hi():
    root=Tk()
    global var
    lbl1=Label(root,textvariable=var)
    lbl1.pack()
    var.set("hello")
main()

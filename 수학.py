from tkinter import*
from math import*

root=Tk()

def calculate(event):
    lbl2.configure(text="결과:"+str(eval(ent.get())))

lbl1=Label(root,text="파이썬 수식 입력")
lbl1.pack()

ent=Entry(root)
ent.bind("<Return>",calculate)
ent.pack()

lbl2=Label(root,text="결과")
lbl2.pack()

root.mainloop()
    

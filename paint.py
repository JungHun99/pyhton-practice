from tkinter import*
from tkinter.colorchooser import*

window=Tk()
col=[0,"black"]
wd=2

can=Canvas(window,width=300,height=300)

def color():
    global col
    col=askcolor()

def wid():
    global wd
    wd=en.get()

def mousedraw(event):
    global x1,y1,col,wd
    
    can.create_line(x1,y1,event.x,event.y,width=wd,fill=col[1])
    x1,y1=event.x,event.y

def mousedown(event):
    global x1,y1
    x1,y1=event.x,event.y

def mouseup(event):
    global x1,y1,col,wd
    if((x1,y1)==(event.x,event.y)):
        can.create_line(x1,y1,x1+1,y1+1,width=wd,fill=col[1])

can.bind("<B1-Motion>",mousedraw)
can.bind("<Button-1>",mousedown)
can.bind("<ButtonRelease-1>",mouseup)

fp=Frame(window)
but=Button(fp,text="색변경",command=color)
but.grid()
en=Entry(fp)
en.grid(row=0,column=1)
bu=Button(fp,text="굵기 변경",command=wid)
bu.grid(row=0,column=2)

can.pack()
fp.pack()

window.mainloop()
    

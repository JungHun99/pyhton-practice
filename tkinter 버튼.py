from tkinter import*

window=Tk()
frame=Frame(window)
frame.pack()
var=StringVar()
add=["첫번째 버튼","두번째 버튼"]
    
x=0
times=0

def time():
    global x
    x+=1
    print()
    var.set(str(x)+"번 클릭 하였습니다")

def color_change():
    change=color

def change():
    global times
    times+=1
    
    if(times%2==0):
        b1["text"]=add[0]
        b2["text"]=add[1]
        
    else:
        b1["text"]="two"
        b2["text"]="two"

def down():
    exit()

b1=Button(frame,text="첫번째 버튼",command=time)
b1.pack(side=LEFT)

b2=Button(frame,text="두번째 버튼",command=color_change)
b2.pack(side=LEFT)

b3=Button(window,text="click",command=change)
b3.pack()

lbl=Label(window,textvariable=var)
lbl.pack()

b4=Button(window,text="quit",command=down)
b4.pack()

var.set(str(x)+"번 클릭 하였습니다")

window.mainloop()

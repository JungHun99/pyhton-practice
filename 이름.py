from tkinter import*


parent=Tk()

def show():
    print("이름: %s\n 나이: %s"%(e1.get(),e2.get()))

Label=(parent,text = "이름").grid(row=0)
Label=(parent,text = "나이").grid(row=1)

e1=Entry(parent)
e2=Entry(parent)

e1.grid(row=0,column=1)
e1.grid(row=1,column=1)

Button(parent,text="보이기",commend=show).grid(row=2,column=1)sticky=W,pady=4)
Button(parent,text="종료",commend=parent.quit).grid(row=2,column=1)sticky=W,pady=4)

parent.mainloop()

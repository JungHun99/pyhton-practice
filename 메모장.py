from tkinter import*
from tkinter import filedialog
from tkinter import messagebox

window=Tk()
text=Text(window,height=100,width=80)
text.pack()

def open():
    file=filedialog.askopenfile(parent=window,mode='r')
    if(file!=None):
        lines=file.read()
        text.insert('1.0',lines)

def save():
    file = filedialog.asksaveasfile(parent=window,mode='w')
    if(file!=None):
        lines=text.get(1.0,END+'-1c')
        file.write(lines)
        file.close()
        text.delete(0.0,END)

def exit():
    if messagebox.askokcancel("QUIT","종료하시겠습니까?"):
        window.destory()

def about():
    label=massagebox.showinfo("About","메모장 프로그램")

menu=Menu(window)
window.config(menu=menu)

filemenu=Menu(menu)
menu.add_cascade(label="파일",menu=filemenu)
filemenu.add_command(label="열기",command=open)
filemenu.add_command(label="저장",command=save)
filemenu.add_command(label="종료",command=exit)


sub=Menu(filemenu)
window.config(menu=menu)

subc=Menu(sub)
sub.add_cascade(label="부제",menu=subc)
subc.add_command(label="부제1")
subc.add_command(label="부제2")







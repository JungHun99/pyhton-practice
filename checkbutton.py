from tkinter import*

window=Tk()

name=[('C',1),('Python',2),('JAVA',3)]
invar=[]

def printChoies():
    a=0
    for i in range(len(name)):
        if(invar[i].get()==1):
            print(name[i][0]+" 입니다")
            a+=1
    if(a==0):
        print("체크된 박스가 없습니다")

for dem,var in name:
    invar.append(IntVar())
    check=Checkbutton(window,text=dem,variable=invar[var-1])
    check.grid(row=var,column=0)
    

but=Button(window,text="확인",command=printChoies)
but.grid(row=var+1,column=0)

window.mainloop()

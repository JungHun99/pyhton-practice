#이름:정훈
#학번 201811485
#학생관리 프로그램
from tkinter import*

root=Tk()

select = IntVar()
select.set(1)

list={("남자",1),("여자",2)}
langList = ["Python", "C", "Java", "C++"]
pt=["이름 : ","나이 : ","성별 : ","사용언어 : ","메모 : ","주소 : ","특기 : ","취미 : "]
valueList=[]
value_List=[]
infor=[]
lb_list=[]

def load():
    f=open("manger.txt",'a')
    f.close()
    a=0
    f=open("manager.txt","r")
    infor.append([])
    while(True):
        line=f.readline()
        
        if not line:
            del infor[a]
            break
        
        if(line=="\n"):
            infor.append([])
            a+=1
        else:
            infor[a].append(line)
            
    f.close()

def save():
    gender=["남자","여자"]
    result = ''
    for i in range(len(valueList)) :
        if valueList[i].get() == 1 :
            result += langList[i] + ', '
    
    infor.append([name2.get(),number2.get(), gender[select.get()-1] ,result,memo2.get(1.0,END),addr2.get(1.0,END),bro2.get(),hob2.get()])
    inputs()
    lb.insert(END,infor[len(infor)-1][0].replace("\n",""))
    lb_list.append(lb)
    name2.delete(0,END)
    number2.delete(0,END)
    memo2.delete(0.0,END)
    addr2.delete(0.0,END)
    bro2.delete(0,END)
    hob2.delete(0,END)

def inputs():
    f=open("manager.txt",'w')
    for i in range(len(infor)):
        for j in range(len(infor[i])):
            if(infor[i][j].find("\n") != -1):
                f.write(infor[i][j])
            else:
                f.write(infor[i][j]+"\n")
        f.write("\n")
    f.close()

def delet():
    items=lb.curselection()
    for i in items:
        del infor[i]
        lb_list[i].delete(0,END)
        del lb_list[i]
        inputs()
    for i in range(len(infor)):
        lb.insert(END,infor[i][0].replace("\n",""))
        lb_list.append(lb)

def printf():
    call=Tk()
    a=0
    items=lb.curselection()
    for i in items:
        f1=Frame(call)
        f1.pack()
        for j in range(8):
            na=Label(f1,text=pt[j])
            na.grid(row=j,column=0)
            if(len(infor[i])==9):
                if(j==4):
                    f2=Frame(f1)
                    f2.grid(row=j,column=1)
                    na2=Label(f2,text=infor[i][j])
                    na2.pack()
                    na3=Label(f2,text=infor[i][j+1])
                    na3.pack()
                    a+=1
                else:
                    na2=Label(f1,text=infor[i][j+a])
                    na2.grid(row=j,column=1)
            elif(len(infor[i])==10):
                if(j==4):
                    f2=Frame(f1)
                    f2.grid(row=j,column=1)
                    na2=Label(f2,text=infor[i][j])
                    na2.pack()
                    na3=Label(f2,text=infor[i][j+1])
                    na3.pack()
                    na4=Label(f2,text=infor[i][j+2])
                    a+=2
                else:
                    na2=Label(f1,text=infor[i][j+a])
                    na2.grid(row=j,column=1)
            else:
                na2=Label(f1,text=infor[i][j+a])
                na2.grid(row=j,column=1)

def modify():
    lang_List = ["Python", "C", "Java", "C++"]
    a=0
    warning=Tk()
    items=lb.curselection()

    select_m = IntVar()
    select_m.set(1)
    
    def modif(x):
        gender=["남자","여자"]
        reserve=infor[x][3]
        infor[x]=[name4.get(),number4.get(), gender[select_m.get()-1] ,reserve,memo4.get(1.0,END),addr4.get(1.0,END),bro4.get(),hob4.get()]
        inputs()
        lb_list[0].delete(0,END)
        for i in range(len(infor)):
            lb.insert(END,infor[i][0].replace("\n",""))
            lb_list.append(lb)
        warning.destroy()
    
    if(len(items)!=1):
        lbl=Label(warning,text="리스트박스에서 한가지만 선택하여 주세요")
        lbl.pack()
        return 0
    
    else:
        for k in items:
            f1=Frame(warning)
            f1.pack()
            for j in range(8):
                na = Label(f1,text=pt[j])
                na.grid(row=j,column=0)
                if(len(infor[k])==9):
                    if(j==4):
                        f2=Frame(f1)
                        f2.grid(row=j,column=1)
                        na2=Label(f2,text=infor[k][j])
                        na2.pack()
                        na3=Label(f2,text=infor[k][j+1])
                        na3.pack()
                        a+=1
                    else:
                        na2=Label(f1,text=infor[k][j+a])
                        na2.grid(row=j,column=1)
                        
                elif(len(infor[k])==10):
                    if(j==4):
                        f2=Frame(f1)
                        f2.grid(row=j,column=1)
                        na2=Label(f2,text=infor[k][j])
                        na2.pack()
                        na3=Label(f2,text=infor[k][j+1])
                        na3.pack()
                        na4=Label(f2,text=infor[k][j+2])
                        a+=2
                    else:
                        na2=Label(f1,text=infor[k][j+a])
                        na2.grid(row=j,column=1)
                else:
                    na2=Label(f1,text=infor[k][j])
                    na2.grid(row=j,column=1)
                
    f3=Frame(warning)
    f3.pack()
    F1=Frame(f3,padx=10)
    F1.grid(row=0,column=0)
    name3=Label(F1,text="이름",width=5)
    name3.grid(row=0,column=0)
    name4=Entry(F1)
    name4.grid(row=0,column=1)

    F2=Frame(f3,padx=10)
    F2.grid(row=0,column=1)
    number3=Label(F2,text="전화번호",width=7)
    number3.grid(row=0,column=0)
    number4=Entry(F2)
    number4.grid(row=0,column=1)

    F3=Frame(f3,padx=10)
    F3.grid(row=1,column=0)
    for txt, val in list:
        Radiobutton(F3, text=txt,padx = 20,variable = select_m,value=val).grid(row=1,column=val-1)
            
    
    F4=Frame(f3,padx=10)
    F4.grid(row=2,column=0)
    memo3=Label(F4,text="메모",font=("",15,))
    memo3.grid(row=0,column=0)
    memo4=Text(F4,height=3)
    memo4.grid(row=1,column=0)

    F5=Frame(f3,padx=10)
    F5.grid(row=3,column=0)
    addr3=Label(F5,text="주소",font=("",15,))
    addr3.grid(row=0,column=0)
    addr4=Text(F5,height=1)
    addr4.grid(row=1,column=0)

    F6=Frame(f3,padx=10)
    F6.grid(row=2,column=1)
    bro3=Label(F6,text="특기")
    bro3.grid(row=0,column=0)
    bro4=Entry(F6)
    bro4.grid(row=1,column=0)

    F7=Frame(f3,padx=10)
    F7.grid(row=3,column=1)
    hob3=Label(F7,text="취미")
    hob3.grid(row=0,column=0)
    hob4=Entry(F7)
    hob4.grid(row=1,column=0)

    but=Button(f3,text="저장",command=lambda x=k : modif(k),width=10,pady=15)
    but.grid(row=4,column=1)
    warning.mainloop()
        

def end():
    exit()

load()

F1=Frame(root,padx=10)
F1.grid(row=0,column=0)
name=Label(F1,text="이름",width=5)
name.grid(row=0,column=0)
name2=Entry(F1)
name2.grid(row=0,column=1)

F2=Frame(root,padx=10)
F2.grid(row=0,column=1)
number=Label(F2,text="전화번호",width=7)
number.grid(row=0,column=0)
number2=Entry(F2)
number2.grid(row=0,column=1)

F3=Frame(root,padx=10)
F3.grid(row=1,column=0)
for txt, val in list:
    Radiobutton(F3, text=txt,padx = 20,variable=select,value=val).grid(row=1,column=val-1)
    
F3=Frame(root,padx=10)
F3.grid(row=1,column=1)
for i in range(len(langList)) :
    valueList.insert(i, IntVar())
    Checkbutton(F3, text=langList[i], variable=valueList[i]).grid(row=i+1, sticky=W)
    
F4=Frame(root,padx=10)
F4.grid(row=2,column=0)
memo=Label(F4,text="메모",font=("",15,))
memo.grid(row=0,column=0)
memo2=Text(F4,height=3)
memo2.grid(row=1,column=0)

F5=Frame(root,padx=10)
F5.grid(row=3,column=0)
addr=Label(F5,text="주소",font=("",15,))
addr.grid(row=0,column=0)
addr2=Text(F5,height=1)
addr2.grid(row=1,column=0)

F6=Frame(root,padx=10)
F6.grid(row=2,column=1)
bro=Label(F6,text="특기")
bro.grid(row=0,column=0)
bro2=Entry(F6)
bro2.grid(row=1,column=0)

F7=Frame(root,padx=10)
F7.grid(row=3,column=1)
hob=Label(F7,text="취미")
hob.grid(row=0,column=0)
hob2=Entry(F7)
hob2.grid(row=1,column=0)

but=Button(root,text="저장",command=save,width=10,pady=15)
but.grid(row=4,column=1)

F8=Frame(root,padx=10)
F8.grid(row=4,column=0)
saving=Label(F8,text="저장 목록")
saving.pack()
sb = Scrollbar(F8, orient=VERTICAL)
sb.pack(side=RIGHT, fill=Y)

lb = Listbox(F8, height=5, selectmode=MULTIPLE)
lb.pack()

for i in range(len(infor)):
    lb.insert(END,infor[i][0].replace("\n",""))
    lb_list.append(lb)
sb.configure(command=lb.yview)
lb.configure(yscrollcommand=sb.set)

F8=Frame(root,padx=10)
F8.grid(row=5, column=0)
modi=Button(F8,text="수정",command=modify,width=10)
modi.pack(side=LEFT)
remo=Button(F8,text="삭제",command=delet,width=10)
remo.pack(side=LEFT)
pri=Button(F8,text="출력",command=printf,width=10)
pri.pack()

button=Button(root,text="종료",command=end)
button.grid(row=5,column=1)

mainloop()

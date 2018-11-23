from tkinter import*

def modify():
    lang_List = ["Python", "C", "Java", "C++"]
    a=0
    warning=Tk()

    select_m = IntVar()
    select_m.set(1)
    
    def modif(x):
        gender=["남자","여자"]
        mo = ''
        for i in range(len(value_List)):
            print(value_List[i].get())
            if (value_List[i].get() == 1):
                mo += lang_List[i] + ', '
        infor[x]=[name4.get(),number4.get(), gender[select_m.get()-1] ,mo,memo4.get(1.0,END),addr4.get(1.0,END),bro4.get(),hob4.get()]
        print(infor[x])
        inputs()
        
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
            
        F10=Frame(f3,padx=10)
        F10.grid(row=1,column=1)
        for i in range(len(langList)) :
            value_List.insert(i,IntVar())
            Checkbutton(F10, text=langList[i], variable = value_List[i]).grid(row=i+1, sticky=W)
    
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

coon=Tk()
modi=Button(coon,text="수정",command=modify,width=10)
modi.pack(side=LEFT)

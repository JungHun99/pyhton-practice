from tkinter import*

menu=Tk()
menu.geometry("320x320")
menu.title("tkinter diction")


dic=[]
count=0

f=open("diction.txt",'a')
f.close()

def save_sub():
    global count
    eng=eng2.get()
    kor=kor2.get()
    f=open("diction.txt",'a')
    dic.append([eng,kor])
    f.write(eng)
    f.write("\n")
    f.write(kor)
    f.write("\n")
    f.close()
    eng2.delete(0,END)
    kor2.delete(0,END)
    save.quit()
    save.destroy()
    count+=1
    
def save():
    global save
    save=Tk()
    eng1=Label(save,text="단어")
    eng1.grid(row=0,column=0)
    global eng2
    eng2=Entry(save)
    eng2.grid(row=0,column=1)
    kor1=Label(save,text="뜻")
    kor1.grid(row=1,column=0)
    global kor2
    kor2=Entry(save)
    kor2.grid(row=1,column=1)
    check=Button(save,text="확인",command=save_sub)
    check.grid(row=2,column=1)

def load():
    global count
    f=open("diction.txt",'r')
    while (True):
        for i in range(2):
            line=f.readline()
            if(i==0):
                name=line
                name=name.replace("\n","")
            elif(i==1):
                code=line
                code=code.replace("\n","")
        if not line:
            break
        count+=1
        dic.append([name,code])
    f.close()

def search_sub():
    global sear
    global search_e
    a=0
    eng=search_e.get()
    sear.quit()
    sear.destroy()
    see=Tk()
    for i in range(count):
        if(dic[i][0]==eng):
            lbl=Label(see,text="단어 :"+dic[i][0]+" 뜻: "+dic[i][1])
            lbl.pack()
            but=Button(see,text="확인",command=see.destroy)
            but.pack()
            a+=1
    if(a==0):
        lbl=Label(see,text="사전에 없는 단어입니다.")
        lbl.pack()
        but=Button(see,text="확인",command=see.destroy)
        but.pack()
    see.quit()
    

def search():
    global sear
    sear=Tk()
    global search_e
    search_e=Entry(sear)
    search_e.pack()
    word=Button(sear,text="단어검색",command=search_sub)
    word.pack()

def delet_sub():
    global count
    global dele
    global dele_e
    a=0
    eng=dele_e.get()
    dele.quit()
    dele.destroy()
    delete=Tk()
    for i in range(count):
        y=dic[i][0]
        if(y==eng):
            del (dic[i])
            a+=1
            count-=1
            f=open("diction.txt","w")
            f.write("")
            f.close()
            f=open("diction.txt","a")
            for i in range(count):
                f.write(dic[i][0]+"\n")
                f.write(dic[i][1]+"\n")
            f.close()
            lbl=Label(delete,text="단어 삭제 완료")
            lbl.pack()
            btn=Button(delete,text="확인",command=delete.destroy)
            btn.pack()
            break
    if(a==0):
        lbl=Label(delete,text="사전에 없는 단어 입니다.")
        lbl.pack()
        btn=Button(delete,text="확인",command=delete.destroy)
        btn.pack()
    delete.quit()
    

def delet():
    global dele
    dele=Tk()
    global dele_e
    dele_e=Entry(dele)
    dele_e.pack()
    word=Button(dele,text="단어삭제",command=delet_sub)
    word.pack()

def fine1():
    global eng
    global word
    global t
    eng=ent.get()
    dic[t][0]=eng
    f=open("diction.txt","w")
    f.write("")
    f.close()
    f=open("diction.txt","a")
    for i in range(count):
        f.write(dic[i][0]+"\n")
        f.write(dic[i][1]+"\n")
    f.close()
    word.quit()
    word.destroy()

def fine2():
    global kot
    global word
    global t
    kor = kot.get()
    dic[t][1]=kor
    f=open("diction.txt","w")
    f.write("")
    f.close()
    f=open("diction.txt","a")
    for a in range(count):
        f.write(dic[a][0]+"\n")
        f.write(dic[a][1]+"\n")
    f.close()
    word.quit()
    word.destroy()

def mean():
    global word
    global kot
    global modi
    modi.quit()
    modi.destroy()
    word=Tk()
    lbl1=Label(word,text=dic[t][0]+" : "+dic[t][1])
    lbl1.pack()
    lbl=Label(word,text="뜻 입력")
    lbl.pack()
    kot=Entry(word)
    kot.pack()
    but=Button(word,text="확인",command=fine2)
    but.pack()

def word():
    global modi
    global word
    global ent
    modi.quit()
    modi.destroy()
    word=Tk()
    lbl1=Label(word,text=dic[t][0]+" : "+dic[t][1])
    lbl1.pack()
    lbl=Label(word,text="단어 입력")
    lbl.pack()
    ent=Entry(word)
    ent.pack()
    but=Button(word,text="확인",command=fine1)
    but.pack()


def sub_modify():
    global modif
    global modi
    global t
    eng=engm.get()
    modif.quit()
    modif.destroy()
    modi=Tk()
    a=0
    for t in range(count):
        if(dic[t][0]==eng):
            a+=1
            break
    if(a==1):
        lbl1=Label(modi,text=dic[t][0]+" : "+dic[t][1])
        lbl1.pack()
        lbl=Label(modi,text="어떤 것을 수정하시겠습니까?")
        lbl.pack()
        frame=Frame(modi)
        frame.pack()
        b2=Button(modi,text="뜻",command=mean,width=10)
        b2.pack(side=LEFT)
        b1=Button(modi,text="단어",command=word,width=10)
        b1.pack(side=LEFT)
        modi.mainloop()
            
    elif(a==0):
        lbl=Label(modi,text="사전에 없는 단어 입니다.")
        lbl.pack()
        b1=Button(modi,text="확인",command=modi.destroy)
        b1.pack()
    
def modify():
    global modif
    modif=Tk()
    global engm
    engm=Entry(modif)
    engm.pack()
    word=Button(modif,text="단어검색",command=sub_modify)
    word.pack()
    
    
def printf():
    global count
    printf=Tk()
    frame1=Frame(printf)
    frame1.pack()
    save=Label(frame1,text="단어",relief="solid",bd=1,width=15,padx=5)
    save.pack(side=LEFT)
    save1=Label(frame1,text="뜻",relief="solid",bd=1,width=15,padx=5)
    save1.pack(side=LEFT)
    for i in range(count):
        frame=Frame(printf)
        frame.pack()
        save=Label(frame,text=dic[i][0],relief="solid",bd=1,width=15,padx=5)
        save.pack(side=LEFT)
        save1=Label(frame,text=dic[i][1],relief="solid",bd=1,width=15,padx=5)
        save1.pack(side=LEFT)
        
def end():
    exit()
    
load()

b1=Button(menu,text="저장",command=save,width=10)
b1.place(x=0,y=0)
b2=Button(menu,text="검색",command=search,width=10)
b2.place(x=0,y=50)
b3=Button(menu,text="삭제",command=delet,width=10)
b3.place(x=0,y=100)
b4=Button(menu,text="사전 출력",command=printf,width=10)
b4.place(x=0,y=150)
b5=Button(menu,text="사전 수정",command=modify,width=10)
b5.place(x=0,y=200)
b6=Button(menu,text="종료",command=end,width=10)
b6.place(x=0,y=250)
menu.mainloop()

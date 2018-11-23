from tkinter import*
import random
import time

main=Tk()

#단어 리스트
word=[]

check=0

#단어를 text파일에서 불러와서 리스트에 저장
fp=open("words.txt",'r')
while(True):
    line=fp.readline()
    line=line.strip()
    if not line:
        break
    word.append([])
    for i in range(len(line)):
        word[check].append(line[i:i+1])
    check+=1
    print(str(check)+" / 658")
print("단어 로딩 완료")
fp.close() 

use=[]
answer=[]

count=0

#랜덤 초이스
ch=random.randint(0,check)

for i in range(len(word[ch])):
    answer.append("_ ")

#심판대 초기
def mim():
    global ch
    can.create_line(40,350,80,350,tags="line")
    can.create_line(60,350,60,100,tags="line")
    can.create_line(60,100,150,100,tags="line")
    can.create_line(60,130,100,100,tags="line")
    can.create_text(250,200,text="정답 : "+"_ "*len(word[ch]),tags="word")
    can.create_text(250,250,text="사용한 단어 : ",tags="use")
    
#사람그리기
def man():
    global count
    if(count==0):
        can.create_line(150,100,150,150,tags="line1")
    elif(count==1):
        can.create_oval(135,150,165,180,tags="oval")
    elif(count==2):
        can.create_line(150,180,150,250,tags="line2")
    elif(count==3):
        can.create_line(150,210,120,170,tags="line3")
    elif(count==4):
        can.create_line(150,210,180,170,tags="line4")
    elif(count==5):
        can.create_line(150,250,120,280,tags="line5")
    elif(count==6):
        can.create_line(150,250,180,280,tags="line6")
    elif(count==7):
        can.create_line(120,130,180,110,fill="red",tags="die")
        die()
    count+=1

#사람이 죽을때    
def die():
    w=""
    global ch
    can.delete("line1","oval","line2","line3","line4","line5","line6",)
    time.sleep(2)
    can.create_oval(155,170,185,200,tags="oval")
    can.create_line(170,200,170,270,tags="line2")
    can.create_line(170,230,140,190,tags="line3")
    can.create_line(170,230,200,190,tags="line4")
    can.create_line(170,270,140,300,tags="line5")
    can.create_line(170,270,200,300,tags="line6")
    for i in range(len(word[ch])):
        w+=word[ch][i]
    can.delete("word")
    can.create_text(300,200,text=w+" 이(가) 정답이었습니다..",tags="finish")

#단어읽고 검색    
def wo():
    global ch
    a=[]
    mid=En.get()
    En.delete(0,END)
    get=mid[0:1]
    if(get==""):
        return 6
    for i in range(len(word[ch])):
        if(get==word[ch][i]):
            a.append(i)
    if(len(a)==0):
        man()
        cre(get)
    else:
        br=clo(a,get)
        if(br==0):
            return 0
        cre(get)

#사용한 단어 보여주기 이미 있다면 되돌리기
def cre(get):
    for i in range(len(use)):
        if(use[i]==get):
            return 0
    use.append(get)
    a=""
    for i in range(len(use)):
        a+=" "+use[i]
    can.delete("use")
    can.create_text(250,250,text="사용한 단어 : "+a,tags="use")
    return 1

#글자를 맞추었을때
def clo(a,get):
    global ch
    k=0
    a.append("")
    can.delete("word")
    w=""
    for i in range(len(word[ch])):
        if(answer[i]=="_ "):
            if(i==a[k]):
                answer[i]=get
                k+=1
    for i in range(len(word[ch])):
        w+=answer[i]
    can.create_text(250,200,text="정답 : "+ w,tags="word")

    if(answer==word[ch]):
        end(w)

#정답을 다 맞추었을때
def end(w):
    can.delete("word")
    can.create_text(250,200,text=w+" 정답을 맞추셨습니다.",tags="finish")
    
#화면 초기 설정
can=Canvas(main,width=400,height=400,bg="white")
can.grid()
f1=Frame(main)
f1.grid(row=1,column=0)
En=Entry(f1)
En.grid()
bt=Button(f1,text="확인",command=wo)
bt.grid(row=0,column=1)

mim()

mainloop()

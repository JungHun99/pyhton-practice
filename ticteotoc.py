from tkinter import*
import os

main=Tk()

control=0

but=[[],[],[]]
tic=[[0,0,0],[0,0,0],[0,0,0]]

color_count=0

#플레이어가 있겼을 때 윈도우로 라벨을 통해 이긴거 표시 
def player_win():
    global control
    global sc
    b=0
    for i in range(3):
        b=tic[i][0]+tic[i][1]+tic[i][2]
        if(b==3):
            if(control==0):
                if(b==3):
                    f=open("score.txt",'w')
                    f.write(str(1+int(sc)))
                    f.close()
                control+=1
                main.quit()
                main.destroy()
                sub=Tk()
                lbl=Label(sub,text="플레이어가 이겼습니다")
                lbl.pack()

    b=0
    for i in range(3):
        b=tic[0][i]+tic[1][i]+tic[2][i]
        if(b==3):
            if(control==0):
                if(b==3):
                        f=open("score.txt",'w')
                        f.write(str(1+int(sc)))
                        f.close()
                control+=1
                main.quit()
                main.destroy()
                sub=Tk()
                lbl=Label(sub,text="플레이어가 이겼습니다")
                lbl.pack()

    b=0
    b=tic[0][0]+tic[1][1]+tic[2][2]
    if(b==3):
        if(control==0):
            if(b==3):
                f=open("score.txt",'w')
                f.write(str(1+int(sc)))
                f.close()
            control+=1
            main.quit()
            main.destroy()
            sub=Tk()
            lbl=Label(sub,text="플레이어가 이겼습니다.")
            lbl.pack()
        
    b=0
    b=tic[0][2]+tic[1][1]+tic[2][0]
    if(b==3):
        if(control==0):
            if(b==3):
                f=open("score.txt",'w')
                f.write(str(1+int(sc)))
                f.close()
            control+=1
            main.quit()
            main.destroy()
            sub=Tk()
            lbl=Label(sub,text="플레이어가 이겼습니다.")
            lbl.pack()
    b=0

#컴퓨터가 이겼을때 플레이어와 똑같은 방법으로 표시 
def computer_win():
    global control
    global c
    
    c=0
    for i in range(3):
        c=tic[i][0]+tic[i][1]+tic[i][2]
        if(c==0.30000000000000004):
            if(control==0):
                control+=1
                main.quit()
                main.destroy()
                sub=Tk()
                lbl=Label(sub,text="컴퓨터가 이겼습니다")
                lbl.pack()

    c=0
    for i in range(3):
        c=tic[0][i]+tic[1][i]+tic[2][i]
        if(c==0.30000000000000004):
            if(control==0):
                control+=1
                main.quit()
                main.destroy()
                sub=Tk()
                lbl=Label(sub,text="컴퓨터가 이겼습니다")
                lbl.pack()

    c=0
    c=tic[0][0]+tic[1][1]+tic[2][2]
    if(c==0.30000000000000004):
        if(control==0):
            control+=1
            main.quit()
            main.destroy()
            sub=Tk()
            lbl=Label(sub,text="컴퓨터가 이겼습니다.")
            lbl.pack()
    
    c=0
    c=tic[0][2]+tic[1][1]+tic[2][0]
    if(c==0.30000000000000004):
        if(control==0):
            control+=1
            main.quit()
            main.destroy()
            sub=Tk()
            lbl=Label(sub,text="컴퓨터가 이겼습니다.")
            lbl.pack()
    c=0

#무승부가 났을 때 표시
def search():
    global control
    global k
    k=0
    a=0
    for i in range(9):
        if(tic[a][i%3]!=0):
            k+=1
        if(i%3==2):
            a+=1
    if(k==9):
        if(control==0):
            sub=Tk()
            lbl=Label(sub,text="무승부 입니다.")
            lbl.pack()

#버튼을 생성
def load():
    a=0
    f=Frame(main)
    f.grid()
    for i in range(9):
        bu=Button(f,text="click",bg="white",command=lambda x=a,y=i%3:color(x,y),width=10,height=5)
        bu.grid(row=a,column=i%3)
        but[a].append(bu)
        if(i%3==2):
            a+=1

#컴퓨터가 검색해야할 항목들
def computer():
    global done
    done=0
    computer_attack()
    computer_defence()
    computer_first()
    computer_sec()

#플레이어가 버튼을 눌렀을 때 하는 기능 집합 
def color(x,y):
    search()
    computer_win()
    global color_count
    if(tic[x][y]==0):
        but[x][y]['bg']="red"
        but[x][y]['text']="X"
        tic[x][y]+=1
        color_count+=1
        computer()
    player_win()
    computer_win()
    search()

def pass_p():
    search()
    computer_win()
    computer()
    player_win()
    computer_win()
    search()

#컴퓨터 인공지능 1
def computer_attack():
    global done
    a=0
    if(done==1):
        return 0
    
    for i in range(3):
        a=tic[i][0]+tic[i][1]+tic[i][2]
        if(a==0.2):
            for x in range(3):
                find(i,x)
                if(done==1):
                    return 0
        a=0
        
    if(done==1):
        return 0
    
    for i in range(3):
        a=tic[0][i]+tic[1][i]+tic[2][i]
        if(a==0.2):
            for x in range(3):
                find(x,i)
                if(done==1):
                    return 0
        a=0
        
    if(done==1):
        return 0
    
    a=tic[0][0]+tic[1][1]+tic[2][2]
    if(a==0.2):
        for x in range(3):
            find(x,x)
            if(done==1):
                return 0
    a=0

    if(done==1):
        return 0
    
    a=tic[0][2]+tic[1][1]+tic[2][0]
    if(a==0.2):
        for x in range(3):
            find(x,2-x)
            if(done==1):
                return 0
    a=0

#컴퓨터 인공지능 2
def computer_defence():
    global done
    a=0
    if(done==1):
        return 0
    
    for i in range(3):
        a=tic[i][0]+tic[i][1]+tic[i][2]
        if(a==2):
            for x in range(3):
                find(i,x)
                if(done==1):
                    return 0
        a=0
        
    if(done==1):
        return 0
    
    for i in range(3):
        a=tic[0][i]+tic[1][i]+tic[2][i]
        if(a==2):
            for x in range(3):
                find(x,i)
                if(done==1):
                    return 0
        a=0
        
    if(done==1):
        return 0
    
    a=tic[0][0]+tic[1][1]+tic[2][2]
    if(a==2):
        for x in range(3):
            find(x,x)
            if(done==1):
                return 0
    a=0

    if(done==1):
        return 0
    
    a=tic[0][2]+tic[1][1]+tic[2][0]
    if(a==2):
        for x in range(3):
            find(x,2-x)
            if(done==1):
                return 0
    a=0

#컴퓨터 인공지능 3
def computer_first():
    global done
    
    if(done==1):
        return 0
    
    a=0
    if(tic[1][1]==0):
        find(1,1)

    if(done==1):
        return 0
        
    a=0
    for i in range(3):
        a=tic[i][0]+tic[i][1]+tic[i][2]
        if(a==0):
            for x in range(3):
                find(i,x)
                if(done==1):
                    return 0
        a=0
        
    if(done==1):
        return 0

    for i in range(3):
        a=tic[0][i]+tic[1][i]+tic[2][i]
        if(a==0):
            for x in range(3):
                find(x,i)
                if(done==1):
                    return 0
        a=0

    if(done==1):
        return 0
        
    a=tic[0][0]+tic[1][1]+tic[2][2]
    if(a==0):
        for x in range(3):
            find(x,x)
            if(done==1):
                return 0
    a=0

    if(done==1):
        return 0

    a=tic[0][2]+tic[1][1]+tic[2][0]
    if(a==0):
        for x in range(3):
            find(x,2-x)
            if(done==1):
                return 0
    a=0

#컴퓨터 인공지능 4
def computer_sec():
    global done

    if(done==1):
        return 0
    
    a=0
    for i in range(3):
        a=tic[i][0]+tic[i][1]+tic[i][2]
        if(a==0.1):
            for x in range(3):
                find(i,x)
                if(done==1):
                    return 0
        a=0

    if(done==1):
        return 0

    for i in range(3):
        a=tic[0][i]+tic[1][i]+tic[2][i]
        if(a==0.1):
            for x in range(3):
                find(x,i)
                if(done==1):
                    return 0
        a=0

    if(done==1):
        return 0
        
    a=tic[0][0]+tic[1][1]+tic[2][2]
    if(a==0.1):
        for x in range(3):
            find(x,x)
            if(done==1):
                return 0
    a=0

    if(done==1):
        return 0

    a=tic[0][2]+tic[1][1]+tic[2][0]
    if(a==0.1):
        for x in range(3):
            find(x,2-x)
            if(done==1):
                return 0
    a=0

#인공지능이 보낸 함수 표시
def find(x,y):
    global done
    global color_count
    if(tic[x][y]==0):
        but[x][y]['bg']="yellow"
        but[x][y]['text']="X"
        tic[x][y]+=0.1
        color_count+=0.1
        done+=1
        return 0

def score():
    global sc
    if(os.path.exists("score.txt")==0):
        f=open("score.txt",'w')
        f.write("0")
        f.close()
    f2=Frame(main)
    f2.grid(row=0,column=1)
    lbl=Label(f2,width=10,height=5)
    lbl.pack()
    f=open("score.txt",'r')
    sc=f.read()
    lbl["text"]=sc+"승"
    pass_v=Button(f2,text="한수 쉼",command=pass_p)
    pass_v.pack()
    
    
    
#윈도우창 로딩
load()
score()

#윈도우 메인루프
main.mainloop()

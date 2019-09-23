dic={}

def append(name,number,habit,no,adrress):
    global dic
    a=0
    for i in dic:
        if(-1 != i.find(name)):
            a+=1
    if(a==0):
        dic[name]=[number,habit,no,address]
    else:
        dic[name+" "+str(a)]=[number,habit,no,address]

def search():
    global dic
    print("어떤 것을 검색 하시겠습니까?")
    n= int(input("1.이름 2.번호 3.취미 4.학번 5.주소"))
    if(n==1):
        name=input("이름을 입력해주세요")
        for i in dic:
            if(-1 != i.find(name)):
                print("이름:",i," 번호:",dic[i][0]," 취미:",dic[i][1],"학번: ",dic[i][2]," 주소: ",dic[i][3])
    if(n==2):
        name=input("번호를 입력해주세요")
        for i in dic:
            if(name == dic[i][0]):
                print("이름:",i," 번호:",dic[i][0]," 취미:",dic[i][1],"학번: ",dic[i][2]," 주소: ",dic[i][3])
    if(n==3):
        name=input("취미를 입력해주세요")
        for i in dic:
            if(name == dic[i][1]):
                print("이름:",i," 번호:",dic[i][0]," 취미:",dic[i][1],"학번: ",dic[i][2]," 주소: ",dic[i][3])
    if(n==4):
        name=input("학번을 입력해주세요")
        for i in dic:
            if(name == dic[i][2]):
                print("이름:",i," 번호:",dic[i][0]," 취미:",dic[i][1],"학번: ",dic[i][2]," 주소: ",dic[i][3])
    if(n==5):
        name=input("주소를 입력해주세요")
        for i in dic:
            if(name == dic[i][3]):
                print("이름:",i," 번호:",dic[i][0]," 취미:",dic[i][1],"학번: ",dic[i][2]," 주소: ",dic[i][3])


def delete(key):
    global dic
    del dic[key]

def modify(key):
    global dic
    if key in dic:
        print("1.이름")
        print("2.번호")
        print("3.취미")
        print("4.학번")
        print("5.주소")
        n=int(input("어떤것을 수정할지 선택해주세요"))
        if(n==1):
            name=input("이름을 입력해주세요")
            app=dic.pop(key)
            append(name,app[0],app[1],app[2],app[3])
        if(n==2):
            number=input("번호를 입력해주세요")
            dic[name][0]=number
        if(n==3):
            habit=input("취미를 입력해주세요")
            dic[name][1]=habit
        if(n==4):
            no=input("학번을 입력해주세요")
            dic[name][2]=no
        if(n==5):
            address=inpuzxzt("주소를 입력해주세요")
            dic[name][3]=address

while(1):
    print("1.추가")
    print("2.검색")
    print("3.삭제")
    print("4.수정")
    print("5.전체 출력")
    print("6.종료")
    n=int(input("어떤것을 누를지 선택해주세요"))
    if(n==1):
        name=input("이름을 입력해주세요")
        number=input("번호를 입력해주세요")
        habit=input("취미를 입력해주세요")
        no=input("학번을 입력해주세요")
        address=input("주소를 입력해주세요")
        append(name,number,habit,no,address)
    if(n==2):
        search()
    if(n==3):
        name=input("이름을 입력해주세요")
        delete(name)
    if(n==4):
        name=input("이름을 입력해주세요")
        modify(name)
    if(n==5):
        for i in dic:
            print(i)
    if(n==6):
        break

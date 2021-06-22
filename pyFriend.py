from tkinter import * #tkinter import
import pyrebase #pyrebase import
Config = {
    "apiKey": "AIzaSyBZ4VeDX4HPCC_UYGwA0dbHKG4MPr4VmoI",
    "authDomain": "addressbook-9fde2.firebaseapp.com",
    "databaseURL": "https://addressbook-9fde2-default-rtdb.firebaseio.com",
    "projectId": "addressbook-9fde2",
    "storageBucket": "addressbook-9fde2.appspot.com",
    "messagingSenderId": "84179225280",
    "appId": "1:84179225280:web:75912dddd6d8b7556abb25",
    "measurementId": "G-M6B313D69T"
  };

firebase = pyrebase.initialize_app(Config)
db = firebase.database()

def start(): #프로그램 실행 시 처음 호출되는 메서드
    all_user = db.child("Addressbook").get(); #Addressbook의 값들을 all_user에 가져옴
    if all_user.each() is None: #all_user에 아무 정보가 없다면
        txt1.insert(END, f'등록된 정보가 없습니다') #해당 메시지를 리스트박스에 출력
        e1.focus_set() #이름 엔트리에 포커싱
    else: #all_user에 정보가 있다면
        txt1.insert(END, f'현재 등록 되어 있는 유저')
        e1.focus_set()
        for user in all_user.each(): #DB전체값 검색
            print(user.key())
            print(user.val())
            txt1.insert(END, f'{user.key()} : {user.val()}') #f-string을 사용하여 key : value형태로 표시

def search() : #검색 메서드
    e1.focus_set() #이름 엔트리에 포커싱
    all_users = db.child("Addressbook").get() #Addressbook의 값들을 all_user에 가져옴
    print("검색")
    name = e1.get() #Entry의 입력된 값을 name변수에 가져옴
    if name=='': #가져온 값이 공백이면
        txt1.insert(END, f'정보가 입력되지 않았습니다\n') #메시지 출력
    else: #가져온 값이 공백이 아니면
        if name not in all_users.val(): #name값이 DB에 존재하는 값이 아니면
            txt1.insert(END, f'등록된 정보가 없습니다') #메시지 출력
            e1.delete(0, END) #해당 엔트리에 있는 텍스트 지움
            e2.delete(0, END) #해당 엔트리에 있는 텍스트 지움
            e3.delete(0, END) #해당 엔트리에 있는 텍스트 지움
            e4.delete(0, END) #해당 엔트리에 있는 텍스트 지움
            e1.focus_set() #이름 엔트리에 포커싱
        else: #name값이 DB에 존재하는 값이면
            for user in all_users.each(): #DB전체 값 검색
                if name==user.key(): #name값에 해당하는 DB의 key값 검색
                    txt1.insert(END, f'{user.key()}의 정보 : {user.val()}') #해당 key값과 value값 출력
                    e1.delete(0, END) #해당 엔트리에 있는 텍스트 지움
                    e2.delete(0, END) #해당 엔트리에 있는 텍스트 지움
                    e3.delete(0, END) #해당 엔트리에 있는 텍스트 지움
                    e4.delete(0, END) #해당 엔트리에 있는 텍스트 지움
                    e1.focus_set() #이름 엔트리에 포커싱

def add() : #추가 메서드
    e1.focus_set() #이름 엔트리에 포커싱
    name = e1.get() #Entry의 입력된 값을 name변수에 가져옴
    phone = e2.get() #Entry의 입력된 값을 phone변수에 가져옴
    address = e3.get() #Entry의 입력된 값을 address변수에 가져옴
    email = e4.get()  # Entry의 입력된 값을 email변수에 가져옴
    if name=='' or phone=='' or address=='' or email=='': #가져온 값중 하나라도 공백이있다면
        txt1.insert(END, f'입력 정보가 비어있습니다\n') #해당 메시지 출력
    else: #하나라도 공백이 없으면
        print("추가")
        db.child("Addressbook").child(name).set({"이메일":email, "주소":address, "휴대전화":phone}) #DB에 name값을 key로 하는 value값 삽입
        txt1.insert(END, f'{e1.get()}의 정보를 목록에 추가 했습니다\n') #리스트 박스에 name 값을 추가 했다는 메시지 출력
        e1.delete(0, END) #해당 엔트리에 있는 텍스트 지움
        e2.delete(0, END) #해당 엔트리에 있는 텍스트 지움
        e3.delete(0, END) #해당 엔트리에 있는 텍스트 지움
        e4.delete(0, END) #해당 엔트리에 있는 텍스트 지움
        e1.focus_set() #이름 엔트리에 포커싱

def delete() : #삭제 메서드
    e1.focus_set() #이름 엔트리에 포커싱
    name = e1.get() #Entry의 입력된 값을 name변수에 가져옴
    if name=='': #name값이 공백이라면
        txt1.insert(END, f'입력 정보가 비어있습니다\n') #해당 메시지 출력
    else: #공백이 아니면
        print("삭제")
        db.child("Addressbook").child(name).remove() #DB에서 name값에 해당하는 key를 삭제
        txt1.insert(END, f'{e1.get()}의 정보를 목록에서 삭제 했습니다\n') #name값을 삭제했음을 알리는 메시지 출력
        e1.delete(0, END) #해당 엔트리에 있는 텍스트 지움
        e1.focus_set() #이름 엔트리에 포커싱

def output() : #출력 메서드
    e1.focus_set() #이름 엔트리에 포커싱
    print("출력")
    all_user = db.child("Addressbook").get() #Addressbook의 값들을 all_user에 가져옴
    if all_user.each() is None: #가져온 값이 아예 없다면
        txt1.insert(END, f'등록된 정보가 없습니다\n') #해당 메시지 출력
    else: #가져온 값이 있다면
        for user in all_user.each(): #DB전체 값 검색
            print(user.key())
            print(user.val())
            txt1.insert(END, f'{user.key()} : {user.val()}') #f-string으로 key : value형식으로 출력
    e1.delete(0, END)

def update(): #수정 메서드
    e1.focus_set() #이름 엔트리에 포커싱
    all_users = db.child("Addressbook").get() #Addressbook의 값들을 all_user에 가져옴
    name = e1.get()  # Entry의 입력된 값을 가져옴
    phone = e2.get()  # Entry의 입력된 값을 가져옴
    address = e3.get()  # Entry의 입력된 값을 가져옴
    email = e4.get()  # Entry의 입력된 값을 가져옴
    if name=='' or phone=='' or address=='' or email=='': #가져온 값중 하나라도 비어있다면
        txt1.insert(END, f'입력 정보가 비어있습니다\n') #해당 메시지 출력
    elif name not in all_users.val(): #name값에 해당하는 값이 DB에 없으면
        txt1.insert(END, f'등록된 정보가 없습니다\n')  # 해당 메시지 출력
    else: #name값에 해당하는 값이 DB에 있으면
        print("수정")
        db.child("Addressbook").child(name).update({"휴대전화": phone})  # name값에 해당하는 키의 value값을 변경
        db.child("Addressbook").child(name).update({"주소": address})  # name값에 해당하는 키의 value값을 변경
        db.child("Addressbook").child(name).update({"이메일": email})  # name값에 해당하는 키의 value값을 변경
        txt1.insert(END, f'해당 유저의 정보가 수정되었습니다\n')
        e1.delete(0, END)  # 해당 엔트리에 있는 텍스트 지움
        e2.delete(0, END)  # 해당 엔트리에 있는 텍스트 지움
        e3.delete(0, END)  # 해당 엔트리에 있는 텍스트 지움
        e4.delete(0, END)  # 해당 엔트리에 있는 텍스트 지움
        e1.focus_set()  # 해당 엔트리에 포커싱


def Empty(): #리스트 박스를 전부 지우느 메서드(리스트 박스가 지저분해질것을 염려)
    print("박스초기화")
    txt1.delete(0,END)

def saveExit() : #프로그램 종료 메서드
    print("종료")
    txt1.insert(END, "저장 & 종료\n")
    exit()


window = Tk() #tkinter 객체를 window변수에 가져옴
f = Frame(window, bg="yellow") #frame f선언

l1 = Label(window, text="이름") #이름 라벨
l1.grid(row=0,column=0, pady=10) #(0,0)위치에 삽입
l2 = Label(window, text="전화번호") #전화번호 라벨
l2.grid(row=1,column=0, pady=10) #(1,0)위치에 삽입
l3 = Label(window, text="주소") #주소 라벨
l3.grid(row=2,column=0, pady=10) #(2,0)위치에 삽입
l4 = Label(window, text="이메일") #이메일 라벨
l4.grid(row=3,column=0, pady=10) #(3,0)위치에 삽입
e1 = Entry(window)
e1.grid(row=0,column=1) #이름 엔트리(0,1)에 삽입
e2 = Entry(window)
e2.grid(row=1,column=1) #전화번호 엔트리(0,1)에 삽입
e3 = Entry(window)
e3.grid(row=2,column=1) #주소 엔트리(0,1)에 삽입
e4 = Entry(window)
e4.grid(row=3,column=1) #이메일 엔트리(0,1)에 삽입

f.grid(row=4,column=0, columnspan=2) #frame f를 (4,0)위치에 삽입(라벨과 엔트리 밑) columnspan=2로 병합

b1 = Button(f, text="검색", command=search, width=10, padx=10)
b1.grid(row=0,column=0) #b1을 frame의 (0,0)에 삽입
b2 = Button(f, text="추가", command=add, width=10, padx=10)
b2.grid(row=0,column=1) #b2을 frame의 (0,1)에 삽입
b3 = Button(f, text="삭제", command=delete, width=10, padx=10)
b3.grid(row=0,column=2) #b3을 frame의 (0,2)에 삽입
b4 = Button(f, text="수정", command=update, width=10, padx=10)
b4.grid(row=0,column=3) #b4을 frame의 (0,3)에 삽입
b5 = Button(f, text="출력", command=output, width=10, padx=10)
b5.grid(row=0,column=4) #b5을 frame의 (0,4)에 삽입
b6 = Button(f, text="리스트박스초기화", command=Empty, width=10, padx=10)
b6.grid(row=0,column=5) #b6을 frame의 (0,5)에 삽입
b7 = Button(f, text="종료", command=saveExit, width=10, padx=10)
b7.grid(row=0,column=6) #b7 frame의 (0,6)에 삽입

txt1 = Listbox(window,width=80,height=10, bg="orange") #리스트 박스객체를 txt1에 가져옴
txt1.grid(row=5,column=0,columnspan=2, pady=10) #txt1을 (5,0)에 삽입 (frame 밑)

scrollbar = Scrollbar(window, orient='vertical') # 방향이 세로인 Scroolbar객체를 scrollbar에 가져옴
scrollbar.grid(row=5, column=2, sticky=N+S) #(4,2)에 삽입

txt1.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=txt1.yview)

start() #프로그램 실행
window.mainloop()

import random
from tkinter import *
import pygame

## 기본 설정
w = Tk()
w.geometry("640x480+700+150")
w.resizable(False, False)
w.title("인물퀴즈(알고리즘8팀)")

## 변수
num = 0
score = 0
r_num = 0
nickname = 0

num_onemore = 0
nickname_onemore = 0
r_num_onemore = 0
score_onemore = 0

pygame.init()

## 오프닝 화면
opening = Canvas(w, width=640, height=480, bg="black")
opening.pack()
img_op=[PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_screen/game_opening.png"),
     PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_screen/game_gide1.png"),
     PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_screen/game_gide2.png"),
     PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_screen/game_gide3.png")]
opening.create_image(320, 240, image=img_op[0])

## 게임 진행 화면
gamescrean = Canvas(w, width=640, height=480, bg="white")
img_bg=[PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_screen/game_bg.png")]
gamescrean.create_image(320,240, image=img_bg)
gamescrean.pack()
## 게임 실패 화면
xxx = Canvas(w, width=640, height=480, bg="black")
img_ddang=[PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_screen/ddang.png")]
xxx.create_image(320,240, image=img_ddang)
## 게임 성공 화면
ooo = Canvas(w, width=640, height=480, bg="black")
img_ooo=[PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_screen/ooo.png")]
ooo.create_image(320,240, image=img_ooo)

## 효과음
s_opening = pygame.mixer.Sound("C:/Users/MASTER/Desktop/hi/soundeffect/에어호른.wav")
s_next = pygame.mixer.Sound("C:/Users/MASTER/Desktop/hi/soundeffect/타닥.wav")
s_roundstart = pygame.mixer.Sound("C:/Users/MASTER/Desktop/hi/soundeffect/라운드시작.wav")
s_game = pygame.mixer.Sound("C:/Users/MASTER/Desktop/hi/soundeffect/게임진행.wav")
s_correctanswer = pygame.mixer.Sound("C:/Users/MASTER/Desktop/hi/soundeffect/정답.mp3")
s_xxx = pygame.mixer.Sound("C:/Users/MASTER/Desktop/hi/soundeffect/땡.wav")
s_ooo = pygame.mixer.Sound("C:/Users/MASTER/Desktop/hi/soundeffect/성공.wav")
s_opening.set_volume(0.2)
s_opening.play()
s_next.set_volume(0.6)
s_roundstart.set_volume(0.2)
s_game.set_volume(0.4)
s_correctanswer.set_volume(0.4)
s_xxx.set_volume(0.6)
s_ooo.set_volume(0.4)

# next 버튼 / enter 버튼 / start 버튼 / one more 버튼 / finish 버튼
next_button=Button(w, text="next", font=("둥근모꼴", 10), fg="black", command=lambda:[next_image()])    #화면 넘기기
next_button.place(x=295, y=390)
enter_button=Button(w, text="enter", font=("둥근모꼴",10), fg="black", command=lambda:[get_nickname()]) #닉네임 저장, start 버튼 활성화
start_button=Button(w, text="start", font=("둥근모꼴",15), fg="red", command=lambda:[start_game()])     #게임 진행 시작
replay = Button(w, text="one more", font=("둥근모꼴", 13), fg="red", command=lambda:[restart()])        #다시 시작
finish = Button(w, text="finish", font=("둥근모꼴", 13), fg="red", command=lambda:[exit()])             #게임 종료

# 닉네임 입력받는 엔트리
nick_ent=Entry(w)
nick_ent.insert(0, "ex. 이수근")
def clear(event):
    if nick_ent.get() == "ex. 이수근":
        nick_ent.delete(0, len(nick_ent.get()))
nick_ent.bind("<Button-1>", clear)

## next버튼 클릭: 화면 넘기기
def next_image():
    s_next.play()
    global num
    num = num+1
    opening.create_image(320,240, image=img_op[num])
    if num == 3:                        
        return game_nickname()

## 오프닝 마지막 페이지(닉네임 입력 화면), next버튼 삭제, nick_ent 생성, enter버튼 생성
def game_nickname():
    next_button.destroy()
    nick_ent.place(x=225, y=305)
    enter_button.place(x=375, y=305)

## 닉네임을 입력받고 출력한 후, start 버튼 생성
def get_nickname():        
    global nickname
    nickname = nick_ent.get()
    print(nickname)
    start_button.place(x=290, y=370)

## start 버튼 클릭: 메인 게임 시작
def start_game():
    opening.destroy()
    enter_button.destroy()
    start_button.destroy()
    nick_ent.destroy()
    s_roundstart.play()
    s_game.play(-1)
    main_game()

## 메인 게임 화면에서 문제 랜덤 출제, game_input 생성
def main_game():
    global r_num
    r_num = set()
    r_num = random.randrange(0,30)
    gamescrean.create_image(190, 240, image=list[r_num][1])
    game_input.place(x=330, y=340)

##문제 리스트
list=[["김희철",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy0.png")],
           ["루피",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy1.png")],
           ["미키마우스",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy2.png")],
           ["올라프",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy3.png")],
           ["유재석",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy4.png")],
           ["이영자",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy5.png")],
           ["제니",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy6.png")],
           ["지코",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy7.png")],
           ["하하",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy8.png")],
           ["홍진경",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy9.png")],
           ["설현",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy10.png")],
           ["이제훈",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy11.png")],
           ["엠마 왓슨",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy12.png")],
           ["한지민",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy13.png")],
           ["황정민",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy14.png")],
           ["김구라",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy15.png")],
           ["자두",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy16.png")],
           ["아따맘마",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy17.png")],
           ["샘 해밍턴",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy18.png")],
           ["김영철",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy19.png")],
           ["아리아나 그란데",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy20.png")],
           ["공명",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy21.png")],
           ["선미",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy22.png")],
           ["칼 라거펠트",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy23.png")],
           ["뚝딱이",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy24.png")],
           ["유희열",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy25.png")],
           ["쿵푸팬더",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy26.png")],
           ["로꼬",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy27.png")],
           ["조정석",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy28.png")],
           ["도라에몽",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy29.png")]]

## game_input 엔터: 정답 받아서 게임 진행(성공, 실패)
def answer(n):
    global score
    if score >= 9:                                         ## 10개를 맞히면 성공 화면
        gamescrean.destroy()
        game_input.destroy()
        s_ooo.play()
        s_game.stop()
        ooo.pack()
        replay.place(x=230, y=350)
        finish.place(x=350, y=350)
    else:
        if game_input.get() == list[r_num][0]:             ## 정답과 입력값이 같다면
            game_input.delete(0, len(game_input.get()))
            score = score + 1                              # 스코어 + 1
            s_correctanswer.play()
            main_game()                                    # 문제 다시 출제
        else:
            game_input.delete(0, len(game_input.get()))    ## 정답과 입력값이 다르다면
            gamescrean.destroy()
            game_input.destroy()
            xxx.pack()                                     ## 게임 실패 화면(땡!)
            s_game.stop()
            s_roundstart.stop()
            s_xxx.play()
            replay.place(x=230, y=350)                     # 한 번 더 버튼
            finish.place(x=350, y=350)                     # 끝내기 버튼
                     
## 답 입력받는 엔트리, 엔터 시 answer 함수 시작
game_input=Entry(w)
game_input.bind("<Return>", answer)

## 다시 시작하는 함수
def restart():
    global w
    global opening
    global img_op
    global next_button
    global nick_ent
    global enter_button
    global start_button
    global num_onemore
    global nickname_onemore
    global r_num_onemore
    global gamescrean
    global img_bg
    global list
    global game_input
    global xxx
    global ooo
    global replay
    global finish
    global img_ooo
    global img_ddang
    global score_onemore
    global s_opening
    global s_next
    global s_roundstart
    global s_game
    global s_correctanswer
    global s_xxx
    global s_ooo

    try:
        if('normal' == w.state()):
            w.destroy()
    finally:
        w = Tk()
        w.geometry("640x480+700+150")
        w.resizable(False, False)
        w.title("인물퀴즈(알고리즘8팀)")
        w.wm_attributes("-topmost", 1)
        
        pygame.init()

        opening = Canvas(w, width=640, height=480, bg="black")
        img_op=[PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_screen/game_opening.png"),
                PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_screen/game_gide1.png"),
                PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_screen/game_gide2.png"),
                PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_screen/game_gide3.png")]
        opening.create_image(320, 240, image=img_op[0])
        opening.pack()
        
        gamescrean = Canvas(w, width=640, height=480, bg="white")  #화면
        img_bg=[PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_screen/game_bg.png")]
        gamescrean.create_image(320,240, image=img_bg)
        gamescrean.pack()

        xxx = Canvas(w, width=640, height=480, bg="black")
        img_ddang=[PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_screen/ddang.png")]
        xxx.create_image(320,240, image=img_ddang)

        ooo = Canvas(w, width=640, height=480, bg="black")
        img_ooo=[PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_screen/ooo.png")]
        ooo.create_image(320,240, image=img_ooo)

        next_button=Button(w, text="next", font=("둥근모꼴", 10), fg="black", command=lambda:[next_image()])
        next_button.place(x=295, y=390)
        start_button=Button(w, text="start", font=("둥근모꼴",15), fg="red", command=lambda:[start_game()])
        enter_button=Button(w, text="enter", font=("둥근모꼴",10), fg="black", command=lambda:[get_nickname()])
        finish = Button(w, text="finish", font=("둥근모꼴", 13), fg="red", command=lambda:[exit()])

        s_opening = pygame.mixer.Sound("C:/Users/MASTER/Desktop/hi/soundeffect/에어호른.wav")
        s_next = pygame.mixer.Sound("C:/Users/MASTER/Desktop/hi/soundeffect/타닥.wav")
        s_roundstart = pygame.mixer.Sound("C:/Users/MASTER/Desktop/hi/soundeffect/라운드시작.wav")
        s_game = pygame.mixer.Sound("C:/Users/MASTER/Desktop/hi/soundeffect/게임진행.wav")
        s_correctanswer = pygame.mixer.Sound("C:/Users/MASTER/Desktop/hi/soundeffect/정답.mp3")
        s_xxx = pygame.mixer.Sound("C:/Users/MASTER/Desktop/hi/soundeffect/땡.wav")
        s_ooo = pygame.mixer.Sound("C:/Users/MASTER/Desktop/hi/soundeffect/성공.wav")
        s_opening.set_volume(0.2)
        s_next.set_volume(0.6)
        s_roundstart.set_volume(0.3)
        s_game.set_volume(0.3)
        s_correctanswer.set_volume(0.4)
        s_xxx.set_volume(0.6)
        s_ooo.set_volume(0.4)

        s_opening.play()

        def next_image():
            s_next.play()
            global num_onemore
            num_onemore = num_onemore +1
            opening.create_image(320,240, image=img_op[num_onemore])
            if num_onemore == 3:                        
                return game_nickname()         

        nick_ent=Entry(w)
        nick_ent.insert(0, "ex. 이수근")
        def clear(event):
            if nick_ent.get() == "ex. 이수근":
                nick_ent.delete(0, len(nick_ent.get()))
        nick_ent.bind("<Button-1>", clear)

        def game_nickname():
            next_button.destroy()
            nick_ent.place(x=225, y=305)
            enter_button.place(x=375, y=305)

        def get_nickname():        
            global nickname_onemore
            nickname_onemore = nick_ent.get()
            print(nickname_onemore)
            start_button.place(x=290, y=370)
        
        def start_game():
            opening.destroy()
            enter_button.destroy()
            start_button.destroy()
            nick_ent.destroy()
            s_roundstart.play()
            s_game.play(-1)
            main_game()
            
        def main_game():
            global r_num_onemore
            r_num_onemore = set()
            r_num_onemore = random.randrange(0,30)
            gamescrean.create_image(200, 240, image=list[r_num_onemore][1])
            game_input.place(x=350, y=340)
                 
        list=[["김희철",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy0.png")],
               ["루피",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy1.png")],
               ["미키마우스",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy2.png")],
               ["올라프",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy3.png")],
               ["유재석",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy4.png")],
               ["이영자",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy5.png")],
               ["제니",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy6.png")],
               ["지코",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy7.png")],
                ["하하",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy8.png")],
                ["홍진경",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy9.png")],
                ["설현",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy10.png")],
                ["이제훈",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy11.png")],
                ["엠마 왓슨",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy12.png")],
                ["한지민",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy13.png")],
                ["황정민",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy14.png")],
                ["김구라",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy15.png")],
                ["자두",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy16.png")],
                ["아따맘마",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy17.png")],
                ["샘 해밍턴",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy18.png")],
                ["김영철",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy19.png")],
                ["아리아나 그란데",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy20.png")],
                ["공명",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy21.png")],
                ["선미",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy22.png")],
                ["칼 라거펠트",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy23.png")],
                ["뚝딱이",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy24.png")],
                ["유희열",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy25.png")],
                ["쿵푸팬더",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy26.png")],
                ["로꼬",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy27.png")],
                ["조정석",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy28.png")],
                ["도라에몽",PhotoImage(file="C:/Users/MASTER/Desktop/hi/game_img/easy29.png")]]

        def answer(n):
            global score_onemore
            if score_onemore >= 9:
                gamescrean.destroy()
                game_input.destroy()
                s_ooo.play()
                s_game.stop()
                ooo.pack()
                finish.place(x=290, y=350)
            else:
                if game_input.get() == list[r_num_onemore][0]:
                    game_input.delete(0, len(game_input.get()))
                    score_onemore = score_onemore + 1
                    s_correctanswer.play()                          
                    main_game()
                else:
                    game_input.delete(0, len(game_input.get())) 
                    gamescrean.destroy()
                    game_input.destroy()
                    xxx.pack()
                    s_game.stop()
                    s_roundstart.stop()
                    s_xxx.play()
                    finish.place(x=290, y=350)
        
        game_input=Entry(w)
        game_input.bind("<Return>", answer)

        w.mainloop()

w.mainloop()

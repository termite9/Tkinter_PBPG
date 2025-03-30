#터틀을 이용하여 레이스 게임 만들기.
import turtle as t
import winsound
import time
import random   

#기본설정
t.bgcolor("lavender")
t.up()  #붓을 종이에서 떼었다고 생각하면 된다. 그림이 그리지 않는다.
t.speed(0) #1~10까지 속도조절가능하며  '0'은 최고속도
t.goto(0,220)
t.write("터틀 레이스",False,align="center", font=("Arial", 20, "bold"))

#레이스 경기장 그리기,
t.goto(-400,170)
t.down()
t.color('lightPink')
t.begin_fill()
for i in range(2):
    t.forward(800)
    t.right(90)
    t.forward(400)
    t.right(90)
t.end_fill()

#결승선그리기
t.color('black')
t.up()
t.goto(300,200)
t.down()
t.goto(300,-250)

#출발선그리기
t.color('black')
t.up()
t.goto(-320,180)
t.down()
t.pensize(5)
t.goto(-320,-240)

start_ycor=[150,90,30,-30,-90,-150,-210] #각레인의 y좌표값(시작위치)

#레이스라인생성
for i in range(6):
    t.up()
    t.goto(-400,start_ycor[i]-30)
    t.color('white')
    t.down()
    t.pensize(5)
    t.goto(400,start_ycor[i]-30)

color_list=["red",'green','blue','yellow','purple','orange','white']
turtles=[]

#터들선수생성
for i in range(7):
    new_turtle=t.Turtle()
    new_turtle.up()
    new_turtle.shape("turtle")
    new_turtle.color(color_list[i])
    new_turtle.goto(-370,start_ycor[i]) #출발선에 배팅할수있도록 번호를 찍어준다.
    new_turtle.write(f"{i+1}번",False,align="center", font=("Arial", 8, "bold"))
    new_turtle.goto(-350,start_ycor[i]) #출발선
    turtles.append(new_turtle)


#배팅하기
user_choice=int(t.textinput("터틀레이스", "어떤거북이에게 배팅하시겠습니까?(1~7)"))
t.up()
t.goto(0,-290)
t.color('black')
t.write(f"당신의 배팅번호는 {user_choice}번 입니다.",False,align="center", font=("Arial", 20, "bold"))
t.ht()  #거북이를 숨긴다  ht()는 hide turtle/ st()는 show turtle

#경기시작알림
winsound.Beep(523,300)
time.sleep(0.3)

#경기시작  #xcor()는 x좌표값을 반환해주는 내장함수이다.
game_over=False
while not game_over:
    for i in turtles:
        rand_speed=random.randint(1,10)
        i.forward(rand_speed)
        if i.xcor() > 330:
            winsound.Beep(800,880)
            game_over=True #게임종료되었지만 이후 터들도 랜덤으로 이동하게되어 1등을 별도로 찾아야한다.
            
#1등 찾기
max_xcor=0
winner=0
for i in range(len(turtles)):
    if turtles[i].xcor() > max_xcor:
        max_xcor=turtles[i].xcor()
        winner=i+1

#결과출력
t.goto(0,0)
if user_choice==winner:
    t.write(f"축하합니다. {winner}번 거북이가 1등입니다.",False,align="center", font=("Arial", 20, "bold"))
else:
    t.write(f"아쉽습니다. {winner}번 거북이가 1등입니다.",False,align="center", font=("Arial", 20, "bold"))
t.done()  # Close the turtle graphics window
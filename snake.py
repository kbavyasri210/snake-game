from turtle import Screen,Turtle
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("snake")
screen.tracer(0)
starting_position=[( 0,0),(-20,0),(-40,0)]
segment=[]
for position in starting_position:
    segment_1=Turtle("square")
    segment_1.color("white")
    segment_1.penup()
    segment_1.goto(position)
    segment.append(segment_1)

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(2,0,-1):
       new_x=segment[seg_num-1].xcor()
       new_y=segment[seg_num-1].ycor()
       segment[seg_num].goto(new_x,new_y)

    
    segment[0].forward(20)












screen.exitonclick()
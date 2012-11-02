# The third mini project for the stop watch game
# Besides providing you with a stop watch 
# This game is designed to test your reflexes
# It displays the number of successful stops/total stops
# A succesfull stop is one where you stop the watch at a whole number

# import 

import simplegui
import random
import math

# globals

interval=100
A=B=C=D=0
successful_stops=total_stops=0
timer_val=0

# function to format the value of timer into a displayable value
# for stopwatch in the format string A:BC.D

def format(t):
    global A,B,C,D
    D=t%10
    C=(int(t/10)%10)
    B=(int(t/100)%6)
    A=int(t/600)
    return

# Handle for the timer called repeatedly

def timer_handle():
    global timer_val
    timer_val+=1
    format(timer_val)

# create the timer

timer=simplegui.create_timer(interval, timer_handle)


# event handlers for start,stop and reset functions of timer

def start():
    timer.start()

def stop():
    global successful_stops,total_stops
    if timer_val!=0:
        total_stops+=1
    if timer_val%10==0 and timer_val!=0:
        successful_stops+=1
    timer.stop()

def reset():
    global A,B,C,D,timer_val,total_stops,successful_stops
    A=B=C=D=timer_val=successful_stops=total_stops=0
    stop()
    
# draw handler for the frame

def draw(canvas):
    canvas.draw_text(str(A)+":"+str(B)+str(C)+"."+str(D),[100,100],30,"White")
    canvas.draw_text(str(successful_stops)+"/"+str(total_stops),[240,30],20,"Green")
# create the frame

frame=simplegui.create_frame("Stopwatch",300,200)

# add the buttons

frame.add_button("Start",start,200)
frame.add_button("Stop",stop,200)
frame.add_button("Reset",reset,200)

# register the draw handler

frame.set_draw_handler(draw)

# start the frame and watch the magic unfold

frame.start()


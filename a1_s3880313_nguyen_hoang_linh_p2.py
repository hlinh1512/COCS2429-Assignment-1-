# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2020C
# Assignment: 1
# Author: Nguyen Hoang Linh(s3880313)
# Created date: 12/08/2020
# Last modified date: dd/mm/yyyy

#Problem 2 Assignment 1: Clock drawing and New Year count down

import turtle, datetime, time


def draw_circle():
    t = turtle.Turtle()


def draw_clock():
    t = turtle.Turtle()
    t.speed(100)
    t.pensize(10)


#DRAW THE MAIN CIRCLE
    t.penup()
    t.goto(0, -150) #starting point
    t.pendown()
    t.circle(250) #draw circle radius = 250px
    t.penup()
    t.goto(0,100) #turtle go to center of the circle
    t.pendown()

#DRAW GRADUATIONS ON THE CLOCK
    t.pensize(4)
    t.left(90)
    for i in range (0,12):
        t.shape("circle")
        t.penup()
        t.forward(230)
        t.stamp()
        t.backward(230)
        for k in range (0,4):
            t.right(360/60)
            t.forward(230)
            t.shape("classic")
            t.stamp()
            t.backward(230)
        t.right(360/60)

    t.pendown()



#DRAW 12 NUMBERS ON THE CLOCK
    #I do it a little bit complicated because I want the position of numbers to be fit to the scale of the clock
    t.left(90 - 180/6)
    t.penup()


        # draw 10 and 11 of clock
    #draw 10
    t.left(9) #adjust turtle
    t.forward(165)
    t.write("10", font=("Verdana", 40, "bold"), align= 'center')
    t.backward(165)
    t.right(9)
    #draw 11
    t.right(180 / 6)
    t.left(6)
    t.forward(158)
    t.write("11", font=("Verdana", 40, "bold"), align='center')
    t.backward(158)
    t.right(6)
    t.right(180/6)

        #draw 12 on the clock
    t.forward(160)
    t.write("12", font=("Verdana", 40, "bold"), align='center')
    t.backward(160)
    t.right(180/6)

        # draw 1 and 2 of clock
    sq_clock = [1,2]
    t.right(7)  # adjust the turtle
    for i in range (0,2):
        t.forward(170)
        t.write(sq_clock[i], font=("Verdana", 40, "bold"), align='center')
        t.backward(170)
        t.right(180 / 6)

    t.left(7)


        # draw 3 and 9 of clock
    #draw 3
    t.right(9) #adjust turtle
    t.forward(190)
    t.write("3", font=("Verdana", 40, "bold"), align='center')
    t.backward(190)
    t.left(9)
    #draw 9
    t.right(180)
    t.left(11)
    t.forward(190)
    t.write("9", font=("Verdana", 40, "bold"), align='center')
    t.backward(190)
    t.right(11)
    t.left(180)


        #draw 4 and 5 of clock
    #draw 4
    t.right(7)
    t.right(180/6)
    t.forward(205)
    t.write("4", font=("Verdana", 40, "bold"), align='center')
    t.backward(205)
    #draw 5
    t.right(180/6)
    t.left(3)
    t.forward(207)
    t.write("5", font=("Verdana", 40, "bold"), align='center')
    t.backward(207)
    t.right(3)
    t.left(7)

        #draw 6 of clock
    t.right(180/6)
    t.forward(220)
    t.write("6", font=("Verdana", 40, "bold"), align='center')
    t.backward(220)


        #draw 7 and 8 of clock
    #draw 7
    t.right(180/6)
    t.forward(207)
    t.write("7", font=("Verdana", 40, "bold"), align='center')
    t.backward(207)
    #draw 8
    t.right(180 / 6)
    t.left(7)
    t.forward(207)
    t.write("8", font=("Verdana", 40, "bold"), align='center')
    t.backward(207)
    t.right(7)
    t.setheading(0) #set angle back to west direction for next step.



#DRAW 3 HANDS OF THE CLOCK


    # #hour hand
    # t.pensize(10)
    # t.setheading(90)
    # t.pendown()
    # t.backward(20)
    # t.forward(130)
    # t.shape("arrow")
    # t.stamp()
    # t.penup()
    # t.goto(0,100) #back to center position

    # #minute hand
    # t.setheading(0)
    # t.pendown()
    # t.backward(20)
    # t.forward(225)
    # t.stamp()
    # t.penup()
    # t.goto(0,100) #back to center position
    # t.pendown()

    # (0,0) stamp a red circle center of the clock\
    t.setheading(90)
    t.penup()
    t.backward(3)  # backward the turtle
    t.pendown()
    t.setheading(0)
    t.pensize(4)
    t.color("red")
    t.fillcolor("red")
    t.pendown()
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.penup()
    t.setheading(90)
    t.forward(3)
    t.setheading(0)
    t.color("black")
    t.pendown()

    t.hideturtle()

    # #second hand
    # t.pensize(3)
    # t.color("red")
    # t.left(45)
    # t.forward(210)
    # t.stamp()


#get current time
    curr_time = time.localtime()
    curr_hour = curr_time.tm_hour
    curr_min = curr_time.tm_min
    curr_sec = curr_time.tm_sec

    #turtle to draw the second hand
    t_sec = turtle.Turtle() #create another turtle to draw second-hand.
    t_sec.penup()
    t_sec.goto(0,100) #set t1 to the center of the circle
    t_sec.setheading(90) #set the second-hand to 0 second
    t_sec.right(curr_sec * (360/60)) #set the second-hand direction to the current time second direction on the clock
    t_sec.pendown()



    #turtle to draw the minute hand
    t_min = turtle.Turtle()
    t_min.penup()
    t_min.goto(0,100)
    t_min.setheading(90)
    t_min.right(curr_min * (360/60))
    t_min.pendown()


    while True:
        for k in range (0,60):
            t_min.right(360/60)
            t_min.pensize(8)
            t_min.forward(205)
            t_min.stamp()
            t_min.penup()
            t_min.backward(205)
            t_min.pendown()
            for j in range (0,60):
               t_sec.right(360/60)
               t_sec.pensize(3)
               t_sec.color("red")
               t_sec.forward(210)
               t_sec.stamp()
               t_sec.penup()
               t_sec.backward(210)
               t_sec.pendown()
               t_sec.clear()
               time.sleep(1) #delay the time to make it moves 1 second in real time
               if (curr_sec == 0):
                   break #dang het 1 vong ma no moi' cap nhat

            t_min.clear()








#main function
if __name__ == "__main__":
    scr = turtle.Screen()
    scr.setup(800,800)


    draw_clock()

    scr.exitonclick()


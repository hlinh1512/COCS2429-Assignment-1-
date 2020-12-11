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
    # (0,0) stamp a red circle center of the clock

    t.shape("circle")
    t.color("red")
    t.stamp()
    t.color("black")
    t.setheading(90)
    t.pensize(8)

    #hour hand
    t.pendown()
    t.backward(20)
    t.forward(130)
    t.shape("arrow")
    t.stamp()
    t.penup()
    t.goto(0,100) #back to center position

    #minute hand
    t.setheading(0)
    t.pendown()
    t.backward(20)
    t.forward(225)
    t.stamp()
    t.penup()
    t.goto(0,100) #back to center position

    #second hand
    t.left(45)
    t.shape("circle")
    t.stamp()
    t.pensize(2)
    t.backward(5)
    t.left(45+90+30)
    t.forward(2)







if __name__ == "__main__":
    scr = turtle.Screen()
    scr.setup(800,800)


    draw_clock()

    scr.exitonclick()


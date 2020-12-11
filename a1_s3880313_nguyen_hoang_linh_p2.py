# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2020C
# Assignment: 1
# Author: Nguyen Hoang Linh(s3880313)
# Created date: 12/08/2020
# Last modified date: dd/mm/yyyy

#Problem 2 Assignment 1: Clock drawing and New Year count down

import turtle, datetime, time, math



def draw_clock():
    t = turtle.Turtle()
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
            t.pensize(3)
            t.pendown()
            t.backward(10)
            t.forward(10)
            t.penup()
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

    t.hideturtle()


#DRAW 3 HANDS OF THE CLOCK
#GET CURRENT TIME
    curr_time = time.localtime()
    curr_hour = curr_time.tm_hour
    curr_min = curr_time.tm_min
    curr_sec = curr_time.tm_sec

    #turtle to draw the second-hand
    t_sec = turtle.Turtle() #create another turtle to draw second-hand.
    t_sec.color("red")
    t_sec.pensize(5)
    t_sec.hideturtle()
    tsec_length = 205
    tsec_angle = curr_sec * 6 + 6 #angle of current second. plus 6 because use time sleep so plus 6 to equal current second

    # turtle to draw the min-hand
    t_min = turtle.Turtle()  # create turtle for min-hand
    t_min.color("black")
    t_min.pensize(8)
    t_min.hideturtle()
    tmin_length = 205
    # tmin_angle = curr_min * (360 / 60)
    tmin_angle = curr_min * (360/60) + curr_sec * (360/60/60) #angle of current minute. I plus the angle of current sec into cur min angle


    #turtle to draw the hour-hand
    t_hour = turtle.Turtle()
    t_hour.color("black")
    t_hour.pensize(8)
    t_hour.hideturtle()
    thour_length = 150
    # thour_angle = curr_hour * (360 / 12)
    thour_angle = curr_hour * (360/12) + curr_min * (360/60/12) + curr_sec * (360/60/60/12) #angle of current hour


    while True:
        #while loop to draw hour-hand
        t_hour.clear()
        t_hour.up()
        t_hour.goto(0,100)
        t_hour.down()
        thour_x = math.sin(math.radians(thour_angle)) * thour_length
        thour_y = math.cos(math.radians(thour_angle)) * thour_length + 100
        t_hour.goto(thour_x, thour_y)
        thour_angle += (360/60/60/12) #current hour it moves per second




        # while loop to draw minute-hand
        t_min.clear()
        t_min.up()
        t_min.goto(0, 100)
        t_min.down()
        tmin_x = math.sin(math.radians(tmin_angle)) * tmin_length
        tmin_y = (math.cos(math.radians(tmin_angle)) * tmin_length) + 100
        t_min.goto(tmin_x, tmin_y)
        tmin_angle += (360/60/60) #current min it moves per second

        #while loop to draw second-hand
        t_sec.clear()
        t_sec.up()
        t_sec.goto(0, 100)  # set t_sec to the center of the circle
        t_sec.down()
        tsec_x = math.sin(math.radians(tsec_angle)) * tsec_length  # x position after 1 second
        tsec_y = (math.cos(math.radians(tsec_angle)) * tsec_length) + 100 #y position after 1 second. I plus 100 because the starting coordinate is (0,100)
        t_sec.goto(tsec_x, tsec_y)
        tsec_angle += 6


        time.sleep(1)
        scr.update()





def draw_string():
    curr_date = datetime.date.today()
    curr_time = time.localtime()
    curr_hour = int(curr_time.tm_hour)
    curr_min = int(curr_time.tm_min)
    curr_sec = int(curr_time.tm_sec)

    #calculate day, hour, min, sec left to new year
    day_left = str(31 - curr_date.day) + " day, "
    hour_left = str(24 - curr_hour) + " hour, "
    min_left = str(60 - curr_min) + " minute, and "
    sec_left = str(60 - curr_sec) + " second "
    string = "Current time is " + str(curr_date) + ' ' + str(curr_hour) + ":" + str(curr_min) + ":" + str(
        curr_sec) + ", \n there are " + day_left + hour_left + min_left + sec_left + "left to New Year "
    #write the whole string
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(-350,-250)
    t.write(string, font=("Comic Sans MS", 17, "bold")) #draw the string
    t.pendown()



#main function
if __name__ == "__main__":
    scr = turtle.Screen()
    scr.setup(1000, 800)
    scr.tracer(0)
    draw_string()
    draw_clock()


    scr.exitonclick()



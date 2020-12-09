# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2020C
# Assignment: 1
# Author: Nguyen Hoang Linh(s3880313)
# Created date: 12/08/2020
# Last modified date: dd/mm/yyyy

#Problem 1 Assignment 1: Histogram drawing


import random #import random library
import turtle #import turtle library
def draw_mark_histogram(hd, di, cr, pa, nn): #function to draw the histogram
    scr = turtle.Screen() #create a screen
    scr.setup(800,800)
    t = turtle.Turtle()
    t.pensize(3)
    #t.speed(10) #put the speed if you want to speed the drawing up
    t.penup()
    t.goto(-230,-250) #starting point (0,0)
    t.pendown()
#draw x,y coordinates and texts
#Y-COORDINATES
    t.left(90)

    #loop drawing scale y-coordinates
    for i in range(1,11):
        t.forward(50)
        #draw the little horizontal bars
        t.left(90)
        t.forward(10)
        t.backward(20)
        t.penup()
        t.forward(10)
        t.pendown()
        t.right(90)
        #draw numbers on y-coordinates
        t.penup()
        t.left(90)
        t.forward(40)
        t.write(i * 10, font=("Arial", 14, "bold"))
        t.backward(40)
        t.right(90)
        t.pendown()


    #draw the frequencies text
    t.forward(50)
    t.penup()
    t.left(90)
    t.forward(150)
    t.write("Frequencies", font=("Arial", 18, "bold"))
    t.goto(-230,-250)
    t.pendown()


#X-COORDINATES
    #draw x-line
    t.right(180)
    t.forward(550)
    t.penup()
    t.backward(550)


    #draw final grade text
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.write("Final grade", font=("Arial", 18, "bold"))
    t.penup()
    t.goto(-230,-250)
    t.pendown()


    #draw NN,PA,CR,DI,HD texts
    t.penup()
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(110+33/2)
    mark_text = ["NN", "PA", "CR", "DI", "HD"] #list of mark texts
    t.pendown()
    for i in range (0,len(mark_text)):
        t.write(mark_text[i], font=("Arial", 18, "bold"))
        t.penup()
        t.forward(66)
    t.goto(-230,-250)
    t.pendown()



#DRAW MARK CHARTS:

    t.penup()
    t.forward(110)
    t.fillcolor('#00A2E8') #color of charts
    t.pendown()


    #draw charts
    mark_value = [nn, pa, cr, di, hd] #list of number of students with mark respectively
    for i in range (0, len(mark_value)):
        for k in range (0,2):
            t.begin_fill()
            t.forward(66)
            t.left(90)
            t.forward(mark_value[i] * 5)  # Times 5 because the ratio on graph 1 students = 5 pixels
            t.left(90)
            t.end_fill()
        #draw text of numbers on top of the chart.
        t.penup()
        t.left(90)
        t.forward(mark_value[i] * 5 + 20)
        t.right(90)
        t.forward(18)
        t.write(mark_value[i], font=("Arial", 18, "bold"))
        t.backward(33/2)
        t.left(90)
        t.backward(mark_value[i] * 5 +20)
        t.right(90)
        #move to next chart.
        t.penup()
        t.forward(66)
        t.pendown()





    scr.exitonclick()


if __name__ == "__main__":
    mark = []
    for i in range(0, 100):
        mark.append(random.randint(0, 100))
    print(mark)
    # grading marks and counting
    hd = 0  # variables for grading
    di = 0
    cr = 0
    pa = 0
    nn = 0
    for i in range(0, len(mark)): #check grade and count number of student each bucket.
        if mark[i] >= 80:
            hd += 1
        elif mark[i] >= 70:
            di += 1
        elif mark[i] >= 60:
            cr += 1
        elif mark[i] >= 50:
            pa += 1
        else:
            nn += 1
    print('Number of NN students: ' + str(nn))
    print('Number of PA students:  ' + str(pa))
    print('Number of CR students:  ' + str(cr))
    print('Number of DI students:  ' + str(di))
    print('Number of HD students:  ' + str(hd))

    draw_mark_histogram(hd, di, cr, pa, nn)








import turtle

def quadrado(posx,posy,lado,cor):
    turtle.showturtle()
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.pendown()
    turtle.fillcolor(cor)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(lado)
        turtle.left(90)
    turtle.end_fill()
    turtle.hideturtle()


def tabuleiro(posx,posy,lado, n, cor1, cor2):
    turtle.speed(0)
    #posição inicial
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.pendown()
    for i in range(1,n+1):
        #desenha linha i
        if i%2 == 0:
            par = cor2
            impar = cor1
        else:
            par = cor1
            impar = cor2

        for j in range(1,n+1):
            # desenha coluna j da linha i
            if j%2 == 0:
                quadrado(turtle.xcor(), turtle.ycor(), lado, par)
            else:
                quadrado(turtle.xcor(), turtle.ycor(), lado, impar)

            turtle.setx(turtle.xcor() + lado)


        turtle.penup()
        turtle.goto(posx, turtle.ycor() + lado)
        turtle.pendown()

def drawCreditos(string,posx,posy,fontsize):
    turtle.showturtle()
    turtle.penup()
    turtle.pencolor("black")
    turtle.pensize(5)
    turtle.speed(6)
    turtle.goto(posx,posy)
    turtle.write(string,align="left",font=("Arial", fontsize, "normal"))
    #turtle.pendown()
    turtle.hideturtle()
    turtle.pensize(2)

def drawPos(pos,i,j):
    turtle.showturtle()
    turtle.penup()
    turtle.pencolor("black")
    turtle.pensize(5)
    turtle.speed(6)
    turtle.goto((-280 + 70 * i)+70/2,(-280 + 70 * j)+70/2)
    turtle.write(pos,align="center",font=("Arial", 18, "normal"))
    #turtle.pendown()
    turtle.hideturtle()

def drawPath(i,j):
    turtle.showturtle()
    turtle.pencolor("black")
    turtle.pensize(5)
    turtle.speed(1)

    turtle.goto((-280 + 70 * i) + 70 / 2, (-280 + 70 * j) + 70 / 2)
    turtle.pendown()

#https://programacaocompython.blogspot.com/2013/11/olhar-e-ver-iv.html
#https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.write
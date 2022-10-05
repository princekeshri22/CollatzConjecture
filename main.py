#Collatz Conjecture

# The Collatz conjecture is a conjecture in mathematics that concerns sequences defined as follows: start with any positive integer n. Then each term is obtained from the previous term as follows:

# If the previous term is even,the next term is half of the previous term.
# If the previous term is odd,the next term is 3 times the previous term plus 1.
# The conjecture is that no matter what value of n, the sequence will always reach 1.

# if x is odd then next term 3*x + 1
# if x is even then next term x//2

# def even(n):
#     return n%2==0

def nextVal(n):
    if(n%2 == 0):
        return n//2
    else:
        return 3*n+1

num = int(input("Enter start parameter :- "))
i = 0

while(num != 1):
    num = nextVal(num)
    print(num)
    i += 1 
print("\n\n")
print(i)
import turtle

win = turtle.getscreen()
impostor = turtle.Turtle()
win.setup(width=600, height=600)

body_color = 'red'
glass_color = '#9acedc'


# it can move forward backward left right
def body():
    """ draws the body """
    impostor.pensize(20)
    # impostor.speed(15)

    impostor.fillcolor(body_color)
    impostor.begin_fill()

    # right side
    impostor.right(90)
    impostor.forward(50)
    impostor.right(180)
    impostor.circle(40, -180)
    impostor.right(180)
    impostor.forward(200)

    # head curve
    impostor.right(180)
    impostor.circle(100, -180)

    # left side
    impostor.backward(20)
    impostor.left(15)
    impostor.circle(500, -20)
    impostor.backward(20)

    impostor.circle(40, -180)
    impostor.left(7)
    impostor.backward(50)

    # hip
    impostor.up()
    impostor.left(90)
    impostor.forward(10)
    impostor.right(90)
    impostor.down()
    impostor.right(240)
    impostor.circle(50, -70)

    impostor.end_fill()


def glass():
    impostor.up()
    impostor.right(230)
    impostor.forward(100)
    impostor.left(90)
    impostor.forward(20)
    impostor.right(90)

    impostor.down()
    impostor.fillcolor(glass_color)
    impostor.begin_fill()

    impostor.right(150)
    impostor.circle(90, -55)

    impostor.right(180)
    impostor.forward(1)
    impostor.right(180)
    impostor.circle(10, -65)
    impostor.right(180)
    impostor.forward(110)
    impostor.right(180)

    impostor.circle(50, -190)
    impostor.right(170)
    impostor.forward(80)

    impostor.right(180)
    impostor.circle(45, -30)

    impostor.end_fill()


def backpack():
    impostor.up()
    impostor.right(60)
    impostor.forward(100)
    impostor.right(90)
    impostor.forward(75)

    impostor.fillcolor(body_color)
    impostor.begin_fill()

    impostor.down()
    impostor.forward(30)
    impostor.right(255)

    impostor.circle(300, -30)
    impostor.right(260)
    impostor.forward(30)

    impostor.end_fill()


body()
glass()
backpack()

turtle.done()

# ping pong game using oob libraries
import turtle

window = turtle.Screen()
window.title("Ping pong python game")
window.bgcolor("#451261")
window.setup(width=800, height=600)
window.tracer(0) #stops window from repainting. it will speed up game


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of repaining
paddle_a.shape("square") #square cyrcle triangle
paddle_a.color("#c499f3")
paddle_a.penup() #do not drow line while moving
paddle_a.goto(-350, 0)
# default size 20px x 20 px
paddle_a.shapesize(stretch_wid=5, stretch_len=1)



# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of repaining
paddle_b.shape("square") #square cyrcle triangle # Ball
paddle_b.color("#c499f3")
paddle_b.penup() #do not drow line while moving
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1) 

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square") #square cyrcle triangle # Ball
ball.color("#c499f3")
ball.penup() #do not drow line while moving
ball.goto(0, 0)


# Function
def paddle_a_up():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	y -= 20
	paddle_a.sety(y)

def paddle_b_up():
	y = paddle_b.ycor()
	y += 20
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y -= 20
	paddle_b.sety(y)

# Keyboard binding
# tells the program to listen to the keybard input
window.listen()
# bind  key press on "w" key on keyboard to invocation of puddle_a_up() function
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")
# Keybard bindings


# Main game loop
while True:
    window.update()



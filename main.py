from turtle import  Turtle, Screen

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
screen = Screen()
screen.setup(width=500, height=400)
import random
for n in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[n])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=(-60+n*30))
    turtles.append(new_turtle)

#tim = Turtle(shape="turtle")

#def move_forwards():
#    tim.forward(10)

#screen.listen()
#screen.onkey(fun=move_forwards, key="space")




user_bet = screen.textinput(title="Make your bet", prompt="Wich turtle will win the race? Enter a color: ")

if user_bet:
    is_race_on = True

while is_race_on:
    for next_turtle in turtles:
        rand_distance = random.randint(0, 10)
        next_turtle.forward(rand_distance)
        if next_turtle.xcor() > 210:
            is_race_on = False
            winning_color = next_turtle.pencolor()
            if winning_color == user_bet:
                print("You won!")
            else:
                print(f"You lost. The winner is the {winning_color}")

#tim.penup()
#tim.goto(x=-230, y=-50)


screen.exitonclick()

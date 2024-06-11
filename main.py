import turtle
import pandas as pd

states = pd.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def mouse_click(x, y):
#     print(x,y)
#
#
# turtle.onscreenclick(mouse_click)
# turtle.mainloop()

# 1 convert guess to title case
# 2 check if guess is among 50 states
# 3 Write correct guesses onto map
# 4 use a loop to allow guessing
# 5 record the correct guesses in a list
# 6 keep track of the score

# creating a list to store the states
state_list = states.state.to_list()
correct_guess = []

game_over = False
while not game_over:

    if len(correct_guess) == 0:
        answer = screen.textinput(title="Guess a state", prompt="Name a state?")

    elif len(correct_guess) != 0:
        answer = screen.textinput(title=f"{len(correct_guess)}/50", prompt="Name a state")

    # confirm that their answer is correctohioo

    if answer in state_list:
        # name of the state should go to the state coord
        correct_guess.append(answer)
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        answer_state = states[answer == states.state]
        state_name.goto(int(answer_state.x), int(answer_state.y))
        state_name.pendown()
        state_name.write(arg=answer, font=('Arial', 8, 'normal'))

        if len(correct_guess) == 50:
            game_over = True
            screen.textinput(prompt="Congrats you got them all")

screen.exitonclick()

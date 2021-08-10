import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
found = 0

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

# To get the coordinates of states from the map image:
#
# def get_mouse_click_coor(x, y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

while found < 50:
    guess = screen.textinput(title=f"{found}/50 States Correct", prompt="Guess a state's name.").title()

    if guess in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        guess_data = data[data.state == guess]
        t.goto(int(guess_data.x), int(guess_data.y))
        t.write(guess)
        found += 1
        all_states.remove(guess)
    if guess == "Exit":
        break


new_data = pandas.DataFrame(all_states)
new_data.to_csv("states_to_learn.csv")

import turtle
import pandas as pd
from writer import Writer

data = pd.read_csv('50_states.csv')
all_states = data['state'].unique()
states_list = data['state'].to_list()
print(states_list)



def check_state(user_input):
    return user_input in all_states


writer_turtle = Writer()

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)  # list out new gif image as one of the shapes that our screen can have

turtle.shape(image)

states_guessed = 0
total_states = 50

answer_state = screen.textinput(title=f'Guess as many states!', prompt="What is another state's name?").title()
answers = []

while len(answers) < 50:
    if answer_state == 'Exit':
        break
    if check_state(answer_state) and not (answer_state in answers):
        answers.append(answer_state)
        states_guessed += 1
        x_cor = data[data['state'] == answer_state].x
        y_cor = data[data['state'] == answer_state].y
        print(int(x_cor), int(y_cor))
        writer_turtle.go_write(answer_state, int(x_cor), int(y_cor))
    answer_state = screen.textinput(title=f'Guessed states {states_guessed} / {total_states}',
                                    prompt="What is another state's name?").title()

# print(data)
#screen.exitonclick()
states_to_learn = []
for state in states_list:
    if state not in answers:
        states_to_learn.append(state)

states_to_learn_dict = {'states to learn': states_to_learn}
states_to_learn_data = pd.DataFrame(states_to_learn_dict)
states_to_learn_data.to_csv('states_to_learn.csv')
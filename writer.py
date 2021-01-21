from turtle import Turtle


class Writer(Turtle):
    def __int__(self):
        super.__init__()
        self.hideturtle()
        self.penup()


    def go_write(self, state_name, x, y):
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(arg=state_name, font=('Courier', 12, 'normal'))

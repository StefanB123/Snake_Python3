from tkinter import *
from random import randrange
# from tkinter import messagebox


class MainWindow(Tk):

    def __init__(self):
        super().__init__()

        # create the game frame
        self.frame_game = Frame(self, width=500, height=500, bg='#484848', relief='ridge')

        # bind the movements to it and focus it
        self.frame_game.bind('<w>', self.change_direction)
        self.frame_game.bind('<a>', self.change_direction)
        self.frame_game.bind('<s>', self.change_direction)
        self.frame_game.bind('<d>', self.change_direction)
        self.frame_game.focus()

        # creates a fruit and defines its position
        self.frame_fruit = Frame(self.frame_game, width=10, height=10)
        self.fruit = Label(self.frame_fruit, bg='#0f0')
        self.fruit_x = randrange(0, 500, 10)
        self.fruit_y = randrange(0, 500, 10)

        # create a snake
        self.frame_snake = Frame(self.frame_game, width=10, height=10)
        self.snake = Label(self.frame_snake, bg='#f00')

        # pack the frames and labels
        self.frame_game.pack_propagate(0)
        self.frame_snake.pack_propagate(0)
        self.frame_fruit.pack_propagate(0)
        self.frame_game.pack()
        self.frame_snake.place(x=0, y=0)
        self.frame_fruit.place(x=self.fruit_x, y=self.fruit_y)
        self.snake.pack(fill=BOTH, expand=1)
        self.fruit.pack(fill=BOTH, expand=1)
        self.after_id = None

        # define an starting direction
        self.pressed = None

        # define an score
        self.score = 0
        self.label_score = Label(self, text=('Your score is: ' + str(self.score)))
        self.label_score.pack()

    def move_snake(self):
        self.after_id = self.after(500, self.move_snake)

        pos_x = self.frame_snake.winfo_x()
        pos_y = self.frame_snake.winfo_y()

        print(str(pos_x) + 'x')
        print(str(pos_y) + 'y')

        if self.pressed == 'w':
            if pos_y > 0:
                pos_y -= 10

        elif self.pressed == 's':
            if pos_y < 490:
                pos_y += 10

        elif self.pressed == 'a':
            if pos_x > 0:
                pos_x -= 10

        else:
            if pos_x < 490:
                pos_x += 10

        self.frame_snake.place(x=pos_x, y=pos_y)
        self.check_fruit(snake_pos_x=pos_x, snake_pos_y=pos_y)

    def change_direction(self, event):
        self.pressed = event.keysym

        if self.after_id is not None:
            self.after_cancel(self.after_id)

        self.move_snake()

    def check_fruit(self, snake_pos_x, snake_pos_y):
        check = False

        while (snake_pos_x == self.fruit_x) & (snake_pos_y == self.fruit_y):
            if not check:
                check = True
                self.score += 1
                self.label_score = Label(self, text='Your score is: ' + str(self.score))
                self.label_score.update()

            self.fruit_x = randrange(0, 500, 10)
            self.fruit_y = randrange(0, 500, 10)

        self.frame_fruit.place(x=self.fruit_x, y=self.fruit_y)







MainWindow().mainloop()

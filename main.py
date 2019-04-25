from tkinter import *
from random import randrange


class MainWindow(Tk):

    def __init__(self):
        super().__init__()

        # set fixed game values (height, width etc.)
        self.height = 500
        self.width = 500
        self.snake_h = 50
        self.snake_w = 50
        self.refresh_time = 500

        # create the game frame
        self.frame_game = Frame(self, width=self.width, height=self.height, bg='#484848', relief='ridge')

        # bind the movements to it and focus it
        self.frame_game.bind('<w>', self.change_direction)
        self.frame_game.bind('<a>', self.change_direction)
        self.frame_game.bind('<s>', self.change_direction)
        self.frame_game.bind('<d>', self.change_direction)
        self.frame_game.focus()

        # creates a fruit and defines its position
        self.frame_fruit = Frame(self.frame_game, width=self.snake_w, height=self.snake_h)
        self.fruit = Label(self.frame_fruit, bg='#0f0')
        self.fruit_x = randrange(0, self.width, self.snake_w)
        self.fruit_y = randrange(0, self.height, self.snake_h)

        # create a snake
        self.frame_snake = Frame(self.frame_game, width=self.snake_w, height=self.snake_h)
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
        # save the id of the self.after so i can stop it
        self.after_id = self.after(self.refresh_time, self.move_snake)

        # get the positions of the snake
        pos_x = self.frame_snake.winfo_x()
        pos_y = self.frame_snake.winfo_y()

        # some printing statements. will get deleted later
        print(str(pos_x) + 'x')
        print(str(pos_y) + 'y')

        # edit the position according to the input
        if self.pressed == 'w':
            if pos_y > 0:
                pos_y -= self.snake_h

        elif self.pressed == 's':
            if pos_y < (self.height - self.snake_h):
                pos_y += self.snake_h

        elif self.pressed == 'a':
            if pos_x > 0:
                pos_x -= self.snake_w

        else:
            if pos_x < (self.width - self.snake_w):
                pos_x += self.snake_w

        # change the position of the snake and check if the snake eats the fruit
        self.frame_snake.place(x=pos_x, y=pos_y)
        self.check_fruit(snake_pos_x=pos_x, snake_pos_y=pos_y)

    def change_direction(self, event):
        # define the key
        self.pressed = event.keysym

        # cancel the timer if it exists
        if self.after_id is not None:
            self.after_cancel(self.after_id)

        # call the method to move the snake
        self.move_snake()

    def check_fruit(self, snake_pos_x, snake_pos_y):
        check = False

        # generates a new fruit position; also increases the score
        while (snake_pos_x == self.fruit_x) & (snake_pos_y == self.fruit_y):
            # score gets only increased once
            if not check:
                check = True
                self.score += 1
                self.label_score = Label(self, text='Your score is: ' + str(self.score))
                self.label_score.update()

            # generate the position randomly
            self.fruit_x = randrange(0, self.width, self.snake_w)
            self.fruit_y = randrange(0, self.height, self.snake_h)

        # place the fruit with the position
        self.frame_fruit.place(x=self.fruit_x, y=self.fruit_y)







MainWindow().mainloop()

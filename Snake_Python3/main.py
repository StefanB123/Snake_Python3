from tkinter import *               # what?? that should normally work
from tkinter import messagebox


class MainWindow(Tk):

    def __init__(self):
        super().__init__()

        self.snake = PhotoImage(file='snake.png')
        self.frame_game = Frame(self, width=500, height=500, bg='#484848', borderwidth=2, relief='ridge')
        self.frame_game.pack_propagate(0)

        self.label_snake = Label(self.frame_game, image=self.snake)
        self.label_snake.pack()



        # self.frame_game.pack()









MainWindow().mainloop()

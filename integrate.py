from __future__ import division
from Tkinter import *
from math import *


class Input:
    def __init__(self, frame, *args, **kwargs):
        self.label = Label(frame, text=kwargs['label_text'])
        self.label.grid(row=kwargs['row'], column=kwargs['column'])
        self.entry = Entry(frame)
        self.entry.grid(row=kwargs['row'], column=kwargs['column'] + 1)
        

class App:
    def __init__(self, master):
        # create a frame
        frame = Frame(master)
        frame.pack()

        # create a input for function
        self.func = Input(frame, label_text='Function', row=0, column=0)

        # create a input for lower limit
        self.lower = Input(frame, label_text='Lower Limit', row=1, column=0)

        # create a input for upper limit
        self.upper = Input(frame, label_text='Upper Limit', row=2, column=0)

        # create a input for steps
        self.steps = Input(frame, label_text='Steps (1-10000)', row=3, column=0)

        # create a output for result
        self.result = Input(frame, label_text='Result', row=4, column=0)
        
        # create a reset button
        self.cal_button = Button(frame, text="Reset", fg="black", command=self.reset)
        self.cal_button.grid(row=5, column=0)

        # create a calculate button
        self.cal_button = Button(frame, text="Calculate", fg="black", command=self.calculate)
        self.cal_button.grid(row=5, column=1)

    def calculate(self):
        # get inputs
        fun = self.func.entry.get()
        lower = float(self.lower.entry.get())
        upper = float(self.upper.entry.get())
        steps = int(self.steps.entry.get())

        # calculate delta x
        del_x = (upper - lower) * 1.0 / steps

        # calculate result using trapezoidal rule
        x = lower
        ans = 0
        ans = ans + eval(fun)
        for i in range(1, steps - 1):
            x = x + del_x
            ans = ans + 2 * eval(fun)
        x = x + eval(fun)
        ans = ans + eval(fun)
        ans = ans * del_x / 2

        # write the result to output
        self.result.entry.delete(0, END)
        self.result.entry.insert(0, round(ans, 8))

    def reset(self):
        self.func.entry.delete(0, END)
        self.lower.entry.delete(0, END)
        self.upper.entry.delete(0, END)
        self.steps.entry.delete(0, END)
        self.result.entry.delete(0, END)


root = Tk()

app = App(root)

root.mainloop()

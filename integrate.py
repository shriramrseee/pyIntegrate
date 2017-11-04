from __future__ import division
from Tkinter import *
from math import *


class App:

    def __init__(self, master):

        # create a frame
        frame = Frame(master)
        frame.pack()

        # create a input for function
        self.func_label = Label(frame, text='Function')
        self.func_label.grid(row=0, column=0)
        self.func_input = Entry(frame)
        self.func_input.grid(row=0, column=1)

        # create a input for lower limit
        self.lower_label = Label(frame, text='Lower Limit')
        self.lower_label.grid(row=1, column=0)
        self.lower_input = Entry(frame)
        self.lower_input.grid(row=1, column=1)

        # create a input for upper limit
        self.upper_label = Label(frame, text='Upper Limit')
        self.upper_label.grid(row=2, column=0)
        self.upper_input = Entry(frame)
        self.upper_input.grid(row=2, column=1)

        # create a input for step size
        self.step_label = Label(frame, text='Steps')
        self.step_label.grid(row=3, column=0)
        self.step_input = Entry(frame)
        self.step_input.grid(row=3, column=1)

        # create a output for result
        self.result_label = Label(frame, text='Result')
        self.result_label.grid(row=4, column=0)
        self.result_input = Entry(frame)
        self.result_input.grid(row=4, column=1)

        # create a reset button
        self.cal_button = Button(frame, text="Reset", fg="black", command=self.reset)
        self.cal_button.grid(row=5, column=0)

        # create a calculate button
        self.cal_button = Button(frame, text="Calculate", fg="black", command=self.calculate)
        self.cal_button.grid(row=5, column=1)

    def calculate(self):
        # get inputs
        fun = self.func_input.get()
        lower = float(self.lower_input.get())
        upper = float(self.upper_input.get())
        steps = int(self.step_input.get())

        # calculate delta x
        del_x = (upper - lower)*1.0/steps

        # calculate result using trapezoidal rule
        x = lower
        ans = 0
        ans = ans + eval(fun)
        for i in range(1, steps-1):
            x = x + del_x
            ans = ans + 2*eval(fun)
        x = x + eval(fun)
        ans = ans + eval(fun)
        ans = ans * del_x / 2

        # write the result to output
        self.result_input.delete(0, END)
        self.result_input.insert(0, round(ans, 8))

    def reset(self):
        self.func_input.delete(0, END)
        self.lower_input.delete(0, END)
        self.upper_input.delete(0, END)
        self.step_input.delete(0, END)
        self.result_input.delete(0, END)



root = Tk()

app = App(root)

root.mainloop()


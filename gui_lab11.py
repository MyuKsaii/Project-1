from tkinter import *

from geo_functions import *

class GUI:
    def __init__(self, window):
        """
        Function for creating window during the initialization of program
        """

        self.window = window
        self.frame_shape = Frame(self.window)
        self.radio_shape = IntVar()
        self.radio_shape.set(0)
        self.radio_circle = Radiobutton(self.frame_shape, text='Circle', variable=self.radio_shape, value=1, command= self.repack)
        self.radio_rectangle = Radiobutton(self.frame_shape, text='Rectangle', variable=self.radio_shape, value=2, command= self.repack)
        self.radio_square = Radiobutton(self.frame_shape, text='Square', variable= self.radio_shape, value=3, command= self.repack)
        self.radio_triangle = Radiobutton(self.frame_shape, text='Triangle', variable=self.radio_shape, value=4, command= self.repack)
        self.radio_circle.pack(side='left')
        self.radio_rectangle.pack(side='left')
        self.radio_square.pack(side='left')
        self.radio_triangle.pack(side='left')
        self.frame_shape.pack(pady=15)

        self.frame_parameters = Frame(self.window)
        self.parameters = StringVar()
        self.parameters.set('Dimensions')
        self.label_parameters = Label(self.frame_parameters, textvariable= self.parameters)
        self.entry_parameter1 = Entry(self.frame_parameters)
        self.entry_parameter2 = Entry(self.frame_parameters)
        self.label_parameters.pack(padx= 5, side= 'left', anchor='n', pady= 5)
        self.entry_parameter1.pack(pady= 10)
        self.frame_parameters.pack(pady= 10)

        self.frame_enter = Frame(self.window)
        self.button_enter = Button(self.frame_enter, text='Calculate', command=self.calc)
        self.button_enter.pack(pady=10)
        self.frame_enter.pack(pady= 10)

        self.frame_answer = Frame(self.window)
        self.answer = StringVar()
        self.message_answer = Message(self.frame_answer, textvariable= self.answer)
        self.frame_answer.pack()

    def repack(self):
        """Function for unpacking widgets from the entry widgets in the parameter frame and packing
        a different number of entry widget back into the frame"""

        self.entry_parameter2.pack_forget()
        self.answer.set('')

        if self.radio_shape.get() == 1:
            self.parameters.set('Radius')

        if self.radio_shape.get() == 2:
            self.entry_parameter2.pack(pady=10)
            self.parameters.set('Side Lengths')

        if self.radio_shape.get() == 3:
            self.parameters.set('Side Length')

        if self.radio_shape.get() ==4:
            self.entry_parameter2.pack(pady=10)
            self.oarameters.set('Base and Height')


    def calc(self):
        """Function for inputting the entry parameters into the functions for area
        and setting the answer variable to what is returned"""
        try:
            if self.radio_shape.get() == 1:
                self.answer.set('Area:\n' + str(format(crc(float(self.entry_parameter1.get())), '.2f')))
                self.message_answer.pack()

            if self.radio_shape.get() == 2:
                self.answer.set('Area:\n' + str(format(rct(float(self.entry_parameter1.get()),
                                               float(self.entry_parameter2.get())), '.2f')))
                self.message_answer.pack()

            if self.radio_shape.get() == 3:
                self.answer.set('Area:\n' + str(format(sqr(float(self.entry_parameter1.get())), '.2f')))
                self.message_answer.pack()

            if self.radio_shape.get() == 4:
                self.answer.set('Area:\n' + str(format(trg(float(self.entry_parameter1.get()),
                                               float(self.entry_parameter2.get())), '.2f')))
                self.message_answer.pack()

        except ValueError:
            self.answer.set('Invalid Number Input')
            self.message_answer.pack()

        except TypeError:
            self.answer.set('Please enter a number')
            self.message_answer.pack()
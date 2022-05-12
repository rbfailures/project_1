from tkinter import *
from tkinter import messagebox

import main


class GUI:
    """
    Object for widgets in a window
    """
    def __init__(self, window) -> None:
        """
        Creates widgets for a window object
        :param window:
        """
        self.window = window

        self.frame_entry1 = Frame(self.window)
        self.frame_entry2 = Frame(self.window)
        self.frame_entry3 = Frame(self.window)
        self.frame_entry4 = Frame(self.window)
        self.frame_submit = Frame(self.window)
        self.frame_error = Frame(self.window)

        self.label_grade1 = Label(self.frame_entry1, text='Class 1')
        self.label_grade2 = Label(self.frame_entry2, text='Class 2')
        self.label_grade3 = Label(self.frame_entry3, text='Class 3')
        self.label_grade4 = Label(self.frame_entry4, text='Class 4')
        self.text_error = StringVar()
        self.text_error.set('')
        self.label_error = Label(self.frame_error, textvariable=self.text_error)

        self.text_entry1 = Entry(self.frame_entry1)
        self.text_entry2 = Entry(self.frame_entry2)
        self.text_entry3 = Entry(self.frame_entry3)
        self.text_entry4 = Entry(self.frame_entry4)

        self.button_submit = Button(self.frame_submit, text='SUBMIT', command=self.clicked)

        self.frame_entry1.pack(anchor='w', pady=10)
        self.frame_entry2.pack(anchor='w', pady=10)
        self.frame_entry3.pack(anchor='w', pady=10)
        self.frame_entry4.pack(anchor='w', pady=10)
        self.frame_submit.pack()
        self.label_grade1.pack(side='left')
        self.label_grade2.pack(side='left')
        self.label_grade3.pack(side='left')
        self.label_grade4.pack(side='left')
        self.text_entry1.pack()
        self.text_entry2.pack()
        self.text_entry3.pack()
        self.text_entry4.pack()
        self.button_submit.pack()
        self.frame_error.pack(anchor='w', pady=10)
        self.label_error.pack()

    def clicked(self):
        """
        Method to validate input, put that input into a list, and plug that list into a GPA Calculator function
        :return:
        """
        grades = []
        grade1 = self.text_entry1.get()
        grade2 = self.text_entry2.get()
        grade3 = self.text_entry3.get()
        grade4 = self.text_entry4.get()
        try:
            grade1 = int(grade1)
            if grade1 < 0 or grade1 > 100:
                messagebox.showerror('Invalid input', 'Error: Please enter an integer between 0-100')
                raise Exception('Input should be between 0 and 100')
            try:
                grade2 = int(grade2)
                if grade2 < 0 or grade2 > 100:
                    messagebox.showerror('Invalid input', 'Error: Please enter an integer between 0-100')
                    raise Exception('Input should be between 0 and 100')
                try:
                    grade3 = int(grade3)
                    if grade3 < 0 or grade3 > 100:
                        messagebox.showerror('Invalid input', 'Error: Please enter an integer between 0-100')
                        raise Exception('Input should be between 0 and 100')
                    try:
                        grade4 = int(grade4)
                        if grade4 < 0 or grade4 > 100:
                            messagebox.showerror('Invalid input', 'Error: Please enter an integer between 0-100')
                            raise Exception('Input should be between 0 and 100')
                    except ValueError:
                        messagebox.showerror('Invalid input', 'Error: Please enter an integer between 0-100')
                except ValueError:
                    messagebox.showerror('Invalid input', 'Error: Please enter an integer between 0-100')
            except ValueError:
                messagebox.showerror('Invalid input', 'Error: Please enter an integer between 0-100')

        except ValueError:
            messagebox.showerror('Invalid input', 'Error: Please enter an integer between 0-100')
        grades = [grade1, grade2, grade3, grade4]
        self.text_error.set(f"Your GPA is {main.GPA(grades)}")

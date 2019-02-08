from tkinter import *


class CrossInterface(Frame):
    # Initialize with root
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # auto-run create_widgets()
        self.create_widgets()

    def create_widgets(self):
        # Headline Label
        Label(self.master, text="VECTOR CALCULATOR\n", fg="red").grid(row=0, column=2)
        # Vector A label
        Label(self.master, text="Vector A").grid(row=3)
        # Vector B Label
        Label(self.master, text="Vector B").grid(row=7)
        # Answer Label
        Label(self.master, text="Answer:").grid(row=4, column=3)
        # XYZ Labels for both Vectors
        Label(self.master, text="X                                      ").grid(row=2, column=2)
        Label(self.master, text="Y                                      ").grid(row=3, column=2)
        Label(self.master, text="Z                                      ").grid(row=4, column=2)
        Label(self.master, text="X                                      ").grid(row=6, column=2)
        Label(self.master, text="Y                                      ").grid(row=7, column=2)
        Label(self.master, text="Z                                      ").grid(row=8, column=2)
        # Initialize interface input variables as strings
        # Different from self.a1, self.a2, ... etc.
        a1 = StringVar()
        a2 = StringVar()
        a3 = StringVar()
        b1 = StringVar()
        b2 = StringVar()
        b3 = StringVar()
        # Creating input boxes on interface as Vector Label & Vector Magnitude
        self.a1 = Entry(self.master, textvariable=a1)
        self.a2 = Entry(self.master, textvariable=a2)
        self.a3 = Entry(self.master, textvariable=a3)
        self.a1.grid(row=2, column=1)
        self.a2.grid(row=3, column=1)
        self.a3.grid(row=4, column=1)
        self.b1 = Entry(self.master, textvariable=b1)
        self.b2 = Entry(self.master, textvariable=b2)
        self.b3 = Entry(self.master, textvariable=b3)
        self.b1.grid(row=6, column=1)
        self.b2.grid(row=7, column=1)
        self.b3.grid(row=8, column=1)
        # Creating the Run Button. Runs show_answer() when pressed
        self.run = Button(text="      RUN      ", fg="blue", command=self.show_answer)
        self.run.grid(row=9, column=1)
        # Creating the Quit Button. Closes application window and ends all processes when pressed
        self.quit = Button(text="QUIT", fg="red", command=self.master.destroy)
        self.quit.grid(row=9, column=5)
        # Initializing the boolean of the Dot Product Checkbox.
        self.on_off = IntVar()
        # Creating checkbox. Checkbox for either cross prodcut or dot product.
        # Cross Product by default, when bool on_off == 0
        self.c = Checkbutton(self.master, text="Dot", variable=self.on_off)
        self.c.grid(row=9, column=0)
        # Creating the outbox bot for the final answer.
        self.answer = Text(self.master, width=20, height=3)
        self.answer.grid(row=5, column=3)
        # Creating the Clear All button. Deletes all characters in all entry boxes
        self.clear_all = Button(text="Clear All", command=self.clearer)
        self.clear_all.grid(row=9, column=2)
        # Creating the clear button for the answer box. Clears all chars in the answer entry box
        self.clear_answer = Button(text="Clear", command=self.clear_ans)
        self.clear_answer.grid(row=6, column=3)

    def clear_ans(self):
        # Clears the chars in the answer box
        self.answer.delete(1.0, END)

    def clearer(self):
        # Clears the chars in all the entry boxes
        self.answer.delete(1.0, END)
        self.a1.delete(0, END)
        self.a2.delete(0, END)
        self.a3.delete(0, END)
        self.b1.delete(0, END)
        self.b2.delete(0, END)
        self.b3.delete(0, END)

    # Calculator for Cross Product
    def cross_calculate(self):
        # Creating array based on cross product algorithm
        # [(a2 * b3) - (a3 * b2)]
        # [(a3 * b1) - (a1 * b3)]
        # [(a1 * b2) - (a2 * b1)]
        array = [[(self.a2.get(), self.b3.get()), (self.a3.get(), self.b2.get())],
                 [(self.a3.get(), self.b1.get()), (self.a1.get(), self.b3.get())],
                 [(self.a1.get(), self.b2.get()), (self.a2.get(), self.b1.get())]]
        # bool state decide whether to multi set or subtract list
        state = 0
        # to run once for state = 0 and one for state = 1
        for rounds in range(2):
            # for each line
            for line in range(3):
                # state == 0 runs set multiplication
                if state == 0:
                    # for the two set in each line
                    for set_index in range(2):
                        if line == 2 and set_index == 1:
                            state = 1
                            # set state boolean to 1 at the last iteration of set multiplication
                        try:
                            # if both of the variable are numbers, multiply them
                            n1 = float(array[line][set_index][0])
                            n2 = float(array[line][set_index][1])
                            # replace the set with one string
                            array[line][set_index] = (str(n1 * n2))
                        except ValueError:
                            # if one of the variables is a non-number
                            # replace the set with one string
                            array[line][set_index] = str(array[line][set_index][0]) + str(array[line][set_index][1])
                else:
                    # List Subtraction
                    try:
                        x1 = float(array[line][0])
                        x2 = float(array[line][1])
                        array[line] = str(round((x1 - x2), 5))
                    except Exception:
                        array[line] = str(array[line][0]) + " - " + str(array[line][1])
        # end of process, return the replaced array
        return array

    # Dot Product Calculator
    def dot_calculate(self):
        num_list = []
        # making a list of all magnitudes of each vector. From order of XYZ
        a = [self.a1.get(), self.a2.get(), self.a3.get()]
        b = [self.b1.get(), self.b2.get(), self.b3.get()]
        # Runs for each line
        for num in range(3):
            try:
                # adds the two numbers if both are numbers. Then adds number into num_list
                num_list.append(str(round(eval("{a} * {b}".format(a=a[num], b=b[num])), 5)))
            except Exception:
                num_list.append(str(a[num]) + str(b[num]))
        num_string = "{} + {} + {}".format(num_list[0], num_list[1], num_list[2])
        # Adds all the numbers together if they are all numbers.
        # otherwise, return a
        try:
            num_string = round(eval(num_string), 5)
            return round(num_string, 5)
        except Exception:
            return num_string

    def show_answer(self):
        # bool 0 for cross product. bool 1 for dot product
        if self.on_off.get() == 0:
            # Creates matrix and inserts answer values
            array = self.cross_calculate()
            self.answer.insert(INSERT, "i[" + array[0] + "]\n")
            self.answer.insert(INSERT, "j[" + array[1] + "]\n")
            self.answer.insert(INSERT, "k[" + array[2] + "]")

        else:
            # dot product answer insert
            self.answer.insert(INSERT, self.dot_calculate())


main_app = CrossInterface(master=Tk())
main_app.master.title(" Vector Cross & Dot Product")
main_app.mainloop()


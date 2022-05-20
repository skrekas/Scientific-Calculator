import math
import tkinter as tk
from tkinter import font
from build_menu import *


# Constants
font_family = "Sans Serif"
BACKGROUND_COLOR = "#dbdbdb"
SCREEN_DIGIT_COLOR = "#335de8"
SMALL_FONT = (font_family, 16)
LARGE_FONT = (font_family, 20, "bold")
WHITE = "#FFFFFF"
DIGITS_FONT = (font_family, 18, "bold")
DIGITS_COLOR = "#383838"
OPERATIONS_FONT = (font_family, 30)
OPERATION_COLOR = "#4f2121"


class Calculator:

    # Μέθοδος αρχικοποίησης των αντικειμένων της κλάσης τύπου Calculator
    def __init__(self):
        # Αρχικοποίηση του παραθύρου της εφαρμογής
        self.window = tk.Tk()
        # Ορισμός της γεωμετρίας - διαστάσεων του παραθύρου της εφαρμογής
        self.window.geometry("500x600")
        # Ορισμός εαν το παράθυρο της εφαρμογής έχει μεταβαλλόμενες διαστάσεις κατά x και y
        self.window.resizable(False, False)
        # Τίτλος του παραθύρου της εφαρμογής
        self.window.title("Calculator (Standard Mode)")
        # Ορισμός του εικονιδίου της εφαρμογής
        # self.window.iconbitmap("./assets/icon.ico")
        # Ορισμός των ελαχίστων διαστάσεων της εφαρμογής
        self.window.minsize(500, 600)
        # Μεταβλητή που αποθηκεύσει την λειτουργία του calculator (standard, scientific κτλ.)
        self.mode = "standard"

        # Προσθήκη του menu της εφαρμογής που επιτρέπει την εναλλαγή
        # ανάμεσα σε διάφορες καταστάσεις λειτουργίας του calculator
        # π.χ. standard, scientific, etc.
        menu = CalculatorMenu(self.window)

        # Dictionary για την αποθήκευση των ψηφίων του calculator
        # Η χρήση dictionary βοηθά στον ορισμό των ψηφίων του calculator
        # μέσω μιας δομής επανάληψης for για την αποφυγή επανάληψης κώδικα.
        # Τα δεδομένα του Dictionary αποθηκεύουν τα ψηφία στη μορφή:
        # ψηφίο: (αριθμός γραμμής, αριθμός στήλης)
        # όπου αριθμός γραμμής και στήλης είναι η γραμμή και η στήλη του δικτύου (grid)
        # το οποίο χρησιμοποιείται παρακάτω για την τοποθέτηση των ψηφίων στο παράθυρο της
        # εφαρμογής
        self.digits = {
            7: (2, 1), 8: (2, 2), 9: (2, 3),
            4: (3, 1), 5: (3, 2), 6: (3, 3),
            3: (4, 1), 2: (4, 2), 1: (4, 3),
            0: (5, 2), '.': (5, 3)
        }

        self.operations = {
            "/": "\u00F7",
            "x": "\u00D7",
            "-": "-",
            "+": "+"
        }

        self.second_row = {
            "x\u00B2": "x^2",
            "1/x": "1/x",
            "|x|": "|x|",
            "exp": "exp",
            "mod": "mod"
        }

        self.total_value = ""
        self.current_value = "0"

        self.screen_frame = self.create_screen_frame()

        self.total_value_lbl, self.current_value_lbl = self.create_display_readings()

        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1, pad=1)
            self.buttons_frame.columnconfigure(x, weight=1, pad=1)

        # Καλώ τις συναρτήσεις για την δημιουργία των κουμπιών στο GUI
        self.create_digit_buttons()
        self.create_operations_buttons()
        self.create_clear_button()
        self.create_equals_button()
        self.create_plus_minus_button()
        self.create_buttons_2nd_row()

    # Συνάρτηση που δημιουργεί τα κείμενα (labels) τα οποία σχηματίζουν τους
    # αριθμούς και τις πράξεις. Η συνάρτηση επιστρέφει τα κείμενα
    def create_display_readings(self):
        # Κείμενο (label) που αντιπροσωπεύει το σύνολο - (πάνω  label)
        total_value_lbl = tk.Label(self.screen_frame, text=self.total_value,
                                   anchor=tk.E, bg=BACKGROUND_COLOR, fg=SCREEN_DIGIT_COLOR, padx=20, font=SMALL_FONT)
        total_value_lbl.pack(expand=True, fill="both")
        # Κείμενο (label) που αντιπροσωπεύει τον αριθμό που πληκτρολογείται
        current_value_lbl = tk.Label(self.screen_frame, text=self.current_value,
                                   anchor=tk.E, bg=BACKGROUND_COLOR, fg=SCREEN_DIGIT_COLOR, padx=20, font=LARGE_FONT)
        current_value_lbl.pack(expand=True, fill="both")
        # Η συνάρτηση
        return total_value_lbl, current_value_lbl

    def add_to_value(self, value):
        if self.current_value == "0":
            self.current_value = ""
        self.current_value += str(value)

        # TODO - FIX THE SCIENTIFIC FORMAT
        if len(self.current_value) > 20:
            scientific_format_value = '%.2E' % float(self.current_value)
            self.update_current_value()
        self.update_current_value()


    def create_digit_buttons(self):
        for digit, grid_loc in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE,
                               fg=DIGITS_COLOR, font=DIGITS_FONT, borderwidth=0,
                               command=lambda x=digit: self.add_to_value(x))
            button.grid(row=grid_loc[0], column=grid_loc[1], sticky=tk.NSEW)

    def create_buttons_2nd_row(self):
        i = 0
        for item in self.second_row:
            i = i + 1
            if (i < 5):
                button = tk.Button(self.buttons_frame, text=item, bg=WHITE,
                                   fg=DIGITS_COLOR, font=DIGITS_FONT, borderwidth=0,
                                   command=lambda x=item: self.commands2row(x))
                button.grid(row=1, column=i, sticky=tk.NSEW)
        item = self.second_row.get('mod')
        button = tk.Button(self.buttons_frame, text=item, bg=WHITE,
                           fg=DIGITS_COLOR, font=DIGITS_FONT, borderwidth=0,
                           command=lambda x=item: self.append_operator(x))
        button.grid(row=1, column=5, sticky=tk.NSEW)

    def commands2row(self, button):
        if (button=='x\u00B2'):
            curr = eval(self.current_value)
            self.current_value = str(curr * curr)
            self.update_total_value()
            self.update_current_value()
        if (button=='1/x'):
            curr = eval(self.current_value)
            self.current_value = str(1 / curr)
            self.update_total_value()
            self.update_current_value()
        if (button=='|x|'):
            curr = eval(self.current_value)
            self.current_value = str(abs(curr))
            self.update_total_value()
            self.update_current_value()
        if (button=='exp'):
            curr = eval(self.current_value)
            self.current_value = str(math.exp(curr))
            self.update_total_value()
            self.update_current_value()
        return

    def append_operator(self, operator):
        print(operator)
        self.current_value += " " + operator + " "
        self.total_value += self.current_value
        # καθάρισε για την επόμενη είσοδο αριθμού
        self.current_value = ""
        self.update_total_value()
        self.update_current_value()

    def create_operations_buttons(self):
        i = 2
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol,
                               bg=WHITE, fg=OPERATION_COLOR,
                               font=OPERATIONS_FONT, borderwidth=0,
                               command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear(self):
        print(font.families())
        self.current_value = "0"
        self.total_value = ""
        self.update_current_value()
        self.update_total_value()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=WHITE,
                           fg=DIGITS_COLOR, font=DIGITS_FONT, borderwidth=0, command=lambda: self.clear())
        button.grid(row=0, column=1, columnspan=3, sticky=tk.NSEW)

    def evaluate(self):
        self.total_value += self.current_value + ' ='
        self.update_total_value()
        components = self.total_value.split(" ")
        if components[1] == "x":
            self.current_value = str(eval(components[0] + "*" + components[2]))
        elif components[1] == "/":
            self.current_value = str(eval(components[0] + "/" + components[2]))
        elif components[1] == "+":
            self.current_value = str(eval(components[0] + "+" + components[2]))
        elif components[1] == "-":
            self.current_value = str(eval(components[0] + "-" + components[2]))
        elif components[1] == "mod":
            self.current_value = str(eval(components[0] + "%" + components[2]))
        self.total_value = ""
        self.update_current_value()

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg="#4abbf7",
                           fg=DIGITS_COLOR, font=DIGITS_FONT, borderwidth=0, command=self.evaluate)
        button.grid(row=5, column=5, sticky=tk.NSEW)

    # Συνάρτηση για την αλλαγή προσήμου του αριθμού
    def apply_sign(self):
        if self.current_value[0] == "-":
            self.current_value = self.current_value[1:]
        elif self.current_value[0] == "0":
            pass
        else:
            self.current_value = "-" + self.current_value
        self.update_current_value()

    def create_plus_minus_button(self):
        button = tk.Button(self.buttons_frame, text="+/-", bg=WHITE,
                           fg=DIGITS_COLOR, font=DIGITS_FONT, borderwidth=0, command=self.apply_sign)
        button.grid(row=5, column=1, sticky=tk.NSEW)

    def create_screen_frame(self):
        frame = tk.Frame(self.window, height=200, bg=BACKGROUND_COLOR)
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window, height=400)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_value(self):
        self.total_value_lbl.config(text=self.total_value)

    def update_current_value(self):
        self.current_value_lbl.config(text=self.current_value)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
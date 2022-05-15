import tkinter as tk
from tkinter import font
from build_menu import *

# KYRIAKH 15-5-2022
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
        self.window.iconbitmap("./assets/icon.ico")
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
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            3: (3, 1), 2: (3, 2), 1: (3, 3),
            0: (4, 2), '.': (4, 3)
        }

        self.operations = {
            "/": "\u00F7",
            "x": "\u00D7",
            "-": "-",
            "+": "+"
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

        self.create_digit_buttons()
        self.create_operations_buttons()
        self.create_clear_button()
        self.create_equals_button()
        self.create_plus_minus_button()

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

    def append_operator(self, operator):
        print(operator)
        self.current_value += " " + operator + " "
        self.total_value += self.current_value
        # καθάρισε για την επόμενη είσοδο αριθμού
        self.current_value = ""
        self.update_total_value()
        self.update_current_value()

    def create_operations_buttons(self):
        i = 0
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
        self.total_value = ""
        self.update_current_value()

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg="#4abbf7",
                           fg=DIGITS_COLOR, font=DIGITS_FONT, borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=4, sticky=tk.NSEW)

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
        button.grid(row=4, column=1, sticky=tk.NSEW)

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
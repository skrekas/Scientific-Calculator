# ------------------------------------------
# ---        PROJECT: CALCULATOR         ---
# ------------------------------------------
# Περιγραφή
# ------------------------------------------
# Δημιουργία calculator στα πλαίσια την
# εργασίας της ενότητας ΠΛΗΠΡΟ του ΕΑΠ.
# ------------------------------------------
# Δημιουργήθηκε στις: 4/2022
# Τελευταία ενημέρωση: 12/6/2022
# ------------------------------------------
# Authors:
# ΣΚΡΕΚΑΣ ΠΑΣΧΑΛΗΣ
# ΒΕΡΓΟΥ ΝΙΚΙ
# ΚΑΤΕΡΙΝΑ ΚΑΚΙΩΡΗ
# ΑΓΡΙΓΙΑΝΝΗΣ ΚΩΝΣΤΑΝΤΙΝΟΣ
# ------------------------------------------


# ------------------------------------------
# ---       ΕΙΣΑΓΩΓΗ ΒΙΒΛΙΟΘΗΚΩΝ         ---
# ------------------------------------------
import tkinter as tk
from tkinter import font
import numpy as np


# ------------------------------------------
# ---        CONSTANT VARIABLES          ---
# ------------------------------------------
# Σταθερές μεταβλητές σχετικά με την εμφάνιση του GUI

# Το font-family του calculator
font_family = "Calibri"
# Το χρώμα του background του calculator
BACKGROUND_COLOR = "#dbdbdb"
# Το χρώμα των πλήκτρων ψηφίων του calculator
SCREEN_DIGIT_COLOR = "#335de8"


# ------------------------------------------
# ---               FONTS                ---
# ------------------------------------------
# Μικρό font για το label που εκφράζει την πράξη (επάνω label στο frame υπολογισμών)
SMALL_FONT = (font_family, 16)
# Μεγάλο font για το label που ορίζεται από την πληκτρολόγηση ψηφίων (κάτω label στο frame υπολογισμών)
LARGE_FONT = (font_family, 22, "bold")

# Font για το κουμπί x10 (INCREASE ORDER BUTTON)
INCREASE_ORDER_BUTTON_FONT = (font_family, 13)

# Font για τα πλήκτρα ψηφίων του calculator
DIGITS_FONT = (font_family, 16, "normal")

# Font για τα ψηφία (0-9 και '.')
OPERATIONS_FONT = (font_family, 20)

# Font για τα κουμπιά διαφόρων λειτουργιών (π.χ. log, ln , cos κτλ).
FUNCTIONS_FONT = (font_family, 13)


# ------------------------------------------
# ---           COLORS/ΧΡΩΜΑΤΑ           ---
# ------------------------------------------
# Σταθερές που αντιπροσωπεύουν χρώματα
# Άσπρο χρώμα (χρησιμοποιείται στο υπόβαθρο των πλήκτρων ψηφίων)
WHITE = "#FFFFFF"
# Χρώμα που χρησιμοποιείται στο κείμενο/text των πλήκτρων ψηφίων (π.χ. 0, 1)
DIGITS_COLOR = "#595858"
# Χρώμα που χρησιμοποιείται στο κείμενο/text των πλήκτρων functions (π.χ. log, cos, exp κλπ)
OPERATION_COLOR = "#4f2121"

# ------------------------------------------
# ---          ΚΛΑΣΗ CALCULATOR          ---
# ------------------------------------------
class Calculator:

    # Μέθοδος αρχικοποίησης των αντικειμένων της κλάσης τύπου Calculator
    def __init__(self):
        # Αρχικοποίηση του παραθύρου της εφαρμογής
        self.window = tk.Tk()
        # Ορισμός της γεωμετρίας - διαστάσεων του παραθύρου της εφαρμογής
        self.window.geometry("500x700")
        # Ορισμός εαν το παράθυρο της εφαρμογής έχει μεταβαλλόμενες διαστάσεις κατά x και y
        self.window.resizable(False, False)
        # Τίτλος του παραθύρου της εφαρμογής
        self.window.title("Calculator")
        # Ορισμός του εικονιδίου της εφαρμογής
        self.window.iconbitmap("./assets/icon.ico")
        # Ορισμός των ελαχίστων διαστάσεων της εφαρμογής
        self.window.minsize(500, 600)

        # Ορισμός μεταβλητής που ελέγχει αν η προηγούμενη πράξη
        # δεν ήταν εφικτή
        self.error = False

        # Ορισμός μεταβλητής που δηλώνει εάν έχει εισαχθεί το '.' για ορισμό δεκαδικού μέρους.
        # Χρησιμοποιείται για την απαγόρευση διαδοχικών εισόδων του συμβόλου '.' σε έναν αριθμο
        # π.χ. 4.3.5.600.66. Αυτός ο αριθμός δεν είναι έγκυρος.
        self.isDecimal = False

        # Μονάδα μέτρησης γωνίας (degrees, radians)
        self.angle_mode = 'radians'

        # Δημιουργία τοπικών αναφορά των κουμπιών του calculator
        # Χρήσιμες για την ενεργοποίηση/απενεργοποίηση κουμπιών στην περίπτωση σφάλματος υπολογισμού
        self.MC = None
        self.MR = None
        self.M_plus= None
        self.M_minus= None
        self.MS = None
        self.EXP = None
        self.FACTORIAL= None
        self.SIN = None
        self.COS = None
        self.TAN = None
        self.INVERSE = None
        self.SQUARE = None
        self.SQROOT = None
        self.LOG = None
        self.LN = None
        self.DEL = None
        self.AC = None
        self.MULTIPLY = None
        self.DIVIDE = None
        self.PLUS = None
        self.MINUS = None
        self.PLUS_MINUS = None
        self.DOT = None
        self.INCREASE_ORDER = None
        self.EQUAL = None

        self.memory = None

        # Dictionary για την αποθήκευση των ψηφίων του calculator
        # Η χρήση dictionary βοηθά στον ορισμό των ψηφίων του calculator
        # μέσω μιας δομής επανάληψης for για την αποφυγή επανάληψης κώδικα.
        # Τα δεδομένα του Dictionary αποθηκεύουν τα ψηφία στη μορφή:
        # ψηφίο: (αριθμός γραμμής, αριθμός στήλης)
        # όπου αριθμός γραμμής και στήλης είναι η γραμμή και η στήλη του δικτύου (grid)
        # το οποίο χρησιμοποιείται παρακάτω για την τοποθέτηση των ψηφίων στο παράθυρο της
        # εφαρμογής
        self.digits = {
            7: (5, 0), 8: (5, 1), 9: (5, 2),
            4: (6, 0), 5: (6, 1), 6: (6, 2),
            3: (7, 2), 2: (7, 1), 1: (7, 0),
            0: (8, 1)
        }

        # Ορίζoυμε ένα λεξικό με τα σύμβολα για τις βασικές πράξεις για να το χρησιμοποιήσουμε στη συνάρτηση
        # που θα ενεργοποιεί και το πληκτρολόγιο για την εισοδο στοιχείων, 11-6-2022
        self.basic_operators = {"/": "\u00F7", "x": "\u00D7", "-": "-", "+": "+"}

        self.total_value = ""
        self.current_value = "0"
        self.angle_mode = 'radians'

        #
        self.screen_frame = self.create_screen_frame()
        self.total_value_lbl, self.current_value_lbl, self.angle_mode_lbl = self.create_display_readings()

        self.buttons_frame = self.create_buttons_frame()

        # Καθορισμός του βάρους των γραμμών και των στύλων
        # του grid κουμπιών (ισοκατανομή)
        for i in range(9):
            self.buttons_frame.rowconfigure(i, weight=1, pad=0)

        for i in range(5):
            self.buttons_frame.columnconfigure(i, weight=1, pad=0)

        # Καλώ τις συναρτήσεις για την δημιουργία των κουμπιών στο GUI
        self.create_digit_buttons()
        self.create_other_buttons()
        # Καλώ συνάρτηση για χρήση απο πληκτρολόγιο.Για τον πολλαπλασιασμό πρέπει να πατάμε το αγγλικό
        # γράμμα x
        self.keyboard()

    # Συνάρτηση που δημιουργεί τα κείμενα (labels) τα οποία σχηματίζουν τους
    # αριθμούς και τις πράξεις. Η συνάρτηση επιστρέφει τα κείμενα
    def create_display_readings(self):
        # Κείμενο (label) που αντιπροσωπεύει το σύνολο - (πάνω  label)
        total_value_lbl = tk.Label(self.screen_frame, text=self.total_value,
                                   anchor=tk.E, bg=BACKGROUND_COLOR,
                                   fg=SCREEN_DIGIT_COLOR, padx=20, font=SMALL_FONT)
        total_value_lbl.pack(expand=True, fill="both")

        # Κείμενο (label) που αντιπροσωπεύει τον αριθμό που πληκτρολογείται
        current_value_lbl = tk.Label(self.screen_frame, text=self.current_value,
                                   anchor=tk.E, bg=BACKGROUND_COLOR,
                                     fg=SCREEN_DIGIT_COLOR, padx=20, font=LARGE_FONT)
        current_value_lbl.pack(expand=True, fill="both")

        # Κείμενο (label) που αντιπροσωπεύει τη λειτουργία (mode) των γωνιών (degrees, radians)
        # Επηρεάζει τις τριγωνομετρικές συναρτήσεις
        angle_mode_lbl = tk.Label(self.screen_frame, text=self.angle_mode,
                                   anchor=tk.E, bg=BACKGROUND_COLOR,
                                     fg=SCREEN_DIGIT_COLOR, padx=20, font=SMALL_FONT)
        current_value_lbl.pack(expand=True, fill="both")

        return total_value_lbl, current_value_lbl, angle_mode_lbl

    # Συνάρτηση που κατασκευάζει τον αριθμό κατά
    # την πληκτρολόγηση των ψηφίων
    def add_to_value(self, value):

        if self.current_value == "0":
            self.current_value = ""

        if value == '.' and not self.isDecimal:
            self.isDecimal = True
            self.DOT['state'] = 'disabled'
        elif self.isDecimal:
            self.isDecimal = False
            self.DOT['state'] = 'disabled'

        self.current_value += str(value)

        # TODO - FIX THE SCIENTIFIC FORMAT
        if len(self.current_value) > 20:
            scientific_format_value = '%.2E' % float(self.current_value)
            self.update_current_value()
        self.update_current_value()

    # Συνάρτηση που δημιουργεί τα ψηφία 0-9 και τα
    # τοποθετεί στη σωστή θέση
    def create_digit_buttons(self):
        for digit, grid_loc in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE,
                               fg=DIGITS_COLOR, font=DIGITS_FONT, borderwidth=0,
                               command=lambda x=digit: self.add_to_value(x))
            button.grid(row=grid_loc[0], column=grid_loc[1], sticky=tk.NSEW, padx=5, pady=5)

    def append_operator(self, operator):
        # Έλεγχος εαν στην άνω τιμή (label) υπάρχει το σύμβολο
        # '=' από προηγούμενη πράξη. Εαν ναι τότε πρέπει να
        # κρατήσουμε το δεύτερο κομμάτι της συμβολοσειράς (μετά το '=')
        # για την συνέχιση των πράξεων
        if '=' in self.total_value:
            self.total_value = self.total_value.split('=')[1]
        self.current_value += " " + operator + " "
        self.total_value += self.current_value
        # καθάρισε για την επόμενη είσοδο αριθμού
        self.current_value = ""
        self.update_total_value()
        self.update_current_value()
        self.DOT['state'] = 'normal'

        # Συνάρτηση για λειτουργία και απο το πληκτρολόγιο
    def keyboard(self):
        self.window.bind("<Return>", lambda result: self.evaluate())
        for key in self.digits:
                self.window.bind(str(key), lambda result, digit=key: self.add_to_value(digit))
        for key in self.basic_operators:
                self.window.bind(key, lambda result, operator=key: self.append_operator(operator))

    def create_other_buttons(self):
        # 1η γραμμή κουμπιών TO DO
        self.MC = button = tk.Button(self.buttons_frame, text='MC',
                                     bg='#ebdec0', fg=OPERATION_COLOR,
                                     font=FUNCTIONS_FONT, borderwidth=0, command=self.memory_clear)
        self.MC.grid(row=0, column=0, sticky=tk.NSEW, padx=5, pady=5)

        self.MR = button = tk.Button(self.buttons_frame, text='MR',
                                     bg='#ebdec0', fg=OPERATION_COLOR,
                                     font=FUNCTIONS_FONT, borderwidth=0, command=self.memory_recal)
        self.MR.grid(row=0, column=1, sticky=tk.NSEW, padx=5, pady=5)

        self.M_plus = tk.Button(self.buttons_frame, text='M+',
                                bg='#ebdec0', fg=OPERATION_COLOR,
                                font=FUNCTIONS_FONT, borderwidth=0, command=lambda: self.memory_add(self.current_value))
        self.M_plus.grid(row=0, column=2, sticky=tk.NSEW, padx=5, pady=5)

        self.DEG_TO_RAD = tk.Button(self.buttons_frame, text='Deg->Rad',
                                 bg='#c9c5ab', fg=OPERATION_COLOR,
                                 font=FUNCTIONS_FONT, borderwidth=0,command=self.deg_to_rad)
        self.DEG_TO_RAD.grid(row=0, column=3, sticky=tk.NSEW, padx=5, pady=5)

        self.PI = tk.Button(self.buttons_frame, text="π",
                            bg='#c9c5ab', fg=DIGITS_COLOR,
                            font=FUNCTIONS_FONT,
                            borderwidth=0,command=self.pi)
        self.PI.grid(row=0, column=4, sticky=tk.NSEW, padx=5, pady=5)

        # 2η γραμμή κουμπιών
        self.TENPOWER = tk.Button(self.buttons_frame, text='\u0031\u0030\u02E3',
                             bg='#c9c5ab', fg=OPERATION_COLOR,
                             font=FUNCTIONS_FONT, borderwidth=0,
                             command= self.ten_power)
        self.TENPOWER.grid(row=1, column=0, sticky=tk.NSEW, padx=5, pady=5)
        #TO DO
        self.NPOWER = tk.Button(self.buttons_frame, text='x\u02b8',
                                   bg='#c9c5ab', fg=OPERATION_COLOR,
                                   font=FUNCTIONS_FONT, borderwidth=0, command=lambda:self.add_to_value(" ^ "))
        self.NPOWER.grid(row=1, column=1, sticky=tk.NSEW, padx=5, pady=5)
        #TO DO
        self.NthROOT = tk.Button(self.buttons_frame, text="\u02b8\u221Ax",
                                 bg='#c9c5ab', fg=OPERATION_COLOR,
                                 font=FUNCTIONS_FONT, borderwidth=0, command=lambda:self.add_to_value(" R "))
        self.NthROOT.grid(row=1, column=2, sticky=tk.NSEW, padx=5, pady=5)

        self.RAD_TO_DEG = tk.Button(self.buttons_frame, text="Rad->Deg", bg='#c9c5ab',
                             fg=OPERATION_COLOR, font=FUNCTIONS_FONT,
                             borderwidth=0,command=self.rad_to_deg )
        self.RAD_TO_DEG.grid(row=1, column=3, sticky=tk.NSEW, padx=5, pady=5)

        self.PRECENT = tk.Button(self.buttons_frame, text="%", bg='#c9c5ab',
                             fg=OPERATION_COLOR, font=FUNCTIONS_FONT,
                             borderwidth=0, command=self.precent)
        self.PRECENT.grid(row=1, column=4, sticky=tk.NSEW, padx=5, pady=5)

        #3η γραμμή κουμπιών

        self.MOD = tk.Button(self.buttons_frame, text='MOD',
                             bg='#c9c5ab', fg=OPERATION_COLOR,
                             font=FUNCTIONS_FONT, borderwidth=0,
                             command=lambda x=" mod ": self.add_to_value(x))
        self.MOD.grid(row=2, column=0, sticky=tk.NSEW, padx=5, pady=5)

        self.ABSOLUTE = tk.Button(self.buttons_frame, text='|x|',
                                   bg='#c9c5ab', fg=OPERATION_COLOR,
                                   font=FUNCTIONS_FONT, borderwidth=0,
                                   command=self.absolute)
        self.ABSOLUTE.grid(row=2, column=1, sticky=tk.NSEW, padx=5, pady=5)

        self.ARCSIN = tk.Button(self.buttons_frame, text='sin-1',
                             bg='#c9c5ab', fg=OPERATION_COLOR,
                             font=FUNCTIONS_FONT, borderwidth=0,
                             command=self.arcsin)
        self.ARCSIN.grid(row=2, column=2, sticky=tk.NSEW, padx=5, pady=5)

        self.ARCCOS = tk.Button(self.buttons_frame, text="cos-1", bg='#c9c5ab',
                             fg=OPERATION_COLOR, font=FUNCTIONS_FONT,
                             borderwidth=0, command=self.arccos)
        self.ARCCOS.grid(row=2, column=3, sticky=tk.NSEW, padx=5, pady=5)

        self.ARCTAN = tk.Button(self.buttons_frame, text="tan-1", bg='#c9c5ab',
                             fg=OPERATION_COLOR, font=FUNCTIONS_FONT,
                             borderwidth=0, command=self.arctan)
        self.ARCTAN.grid(row=2, column=4, sticky=tk.NSEW, padx=5, pady=5)

        # 4η γραμμή κουμπιών
        self.EXP = tk.Button(self.buttons_frame, text='exp',
                             bg='#c9c5ab', fg=OPERATION_COLOR,
                             font=FUNCTIONS_FONT, borderwidth=0,
                             command=self.exponent)
        self.EXP.grid(row=3, column=0, sticky=tk.NSEW, padx=5, pady=5)

        self.FACTORIAL = tk.Button(self.buttons_frame, text='!x',
                                   bg='#c9c5ab', fg=OPERATION_COLOR,
                                   font=FUNCTIONS_FONT, borderwidth=0,
                                   command=self.factorial)
        self.FACTORIAL.grid(row=3, column=1, sticky=tk.NSEW, padx=5, pady=5)

        self.SIN = tk.Button(self.buttons_frame, text='sin',
                             bg='#c9c5ab', fg=OPERATION_COLOR,
                             font=FUNCTIONS_FONT, borderwidth=0,
                             command=self.sin)
        self.SIN.grid(row=3, column=2, sticky=tk.NSEW, padx=5, pady=5)

        self.COS = tk.Button(self.buttons_frame, text="cos", bg='#c9c5ab',
                             fg=OPERATION_COLOR, font=FUNCTIONS_FONT,
                             borderwidth=0, command=self.cos)
        self.COS.grid(row=3, column=3, sticky=tk.NSEW, padx=5, pady=5)

        self.TAN = tk.Button(self.buttons_frame, text="tan", bg='#c9c5ab',
                             fg=OPERATION_COLOR, font=FUNCTIONS_FONT,
                             borderwidth=0, command=self.tan)
        self.TAN.grid(row=3, column=4, sticky=tk.NSEW, padx=5, pady=5)


        # 5η γραμμή κουμπιών
        self.INVERSE = tk.Button(self.buttons_frame, text='1/x',
                                 bg='#c9c5ab', fg=OPERATION_COLOR,
                                 font=FUNCTIONS_FONT, borderwidth=0,
                                 command=self.inverse_number)
        self.INVERSE.grid(row=4, column=0, sticky=tk.NSEW, padx=5, pady=5)

        self.SQUARE = tk.Button(self.buttons_frame, text='x\u00b2',#11-6-2022
                                bg='#c9c5ab', fg=OPERATION_COLOR,
                                font=FUNCTIONS_FONT, borderwidth=0,
                                command=self.square_number)
        self.SQUARE.grid(row=4, column=1, sticky=tk.NSEW, padx=5, pady=5)

        self.SQROOT = tk.Button(self.buttons_frame, text='√x',
                                bg='#c9c5ab', fg=OPERATION_COLOR,
                                font=FUNCTIONS_FONT, borderwidth=0,
                                command=self.square_root)
        self.SQROOT.grid(row=4, column=2, sticky=tk.NSEW, padx=5, pady=5)

        self.LOG = tk.Button(self.buttons_frame, text='log',
                             bg='#c9c5ab', fg=OPERATION_COLOR,
                             font=FUNCTIONS_FONT, borderwidth=0,
                             command=self.logarithm)
        self.LOG.grid(row=4, column=3, sticky=tk.NSEW, padx=5, pady=5)

        self.LN = tk.Button(self.buttons_frame, text='ln',
                            bg='#c9c5ab', fg=OPERATION_COLOR,
                            font=FUNCTIONS_FONT, borderwidth=0,
                            command=self.natural_log)
        self.LN.grid(row=4, column=4, sticky=tk.NSEW, padx=5, pady=5)

        # 6η γραμμή κουμπιών
        self.DEL = tk.Button(self.buttons_frame, text='DEL',
                             bg='#eda48c', fg=OPERATION_COLOR,
                             font=FUNCTIONS_FONT, borderwidth=0,
                             command=self.delete)
        self.DEL.grid(row=5, column=3, sticky=tk.NSEW, padx=5, pady=5)

        self.AC = tk.Button(self.buttons_frame, text='AC',
                            bg='#eda48c', fg=OPERATION_COLOR,
                            font=FUNCTIONS_FONT, borderwidth=0,
                            command=lambda: self.clear())
        self.AC.grid(row=5, column=4, sticky=tk.NSEW, padx=5, pady=5)

        # 7η γραμμή κουμπιών
        self.MULTIPLY = tk.Button(self.buttons_frame, text='\u00D7',
                                  bg='#4b5e5d', fg=WHITE,
                                  font=DIGITS_FONT, borderwidth=0,
                                  command=lambda x='x': self.append_operator(x))
        self.MULTIPLY.grid(row=6, column=3, sticky=tk.NSEW, padx=5, pady=5)

        self.DIVIDE = tk.Button(self.buttons_frame, text='\u00F7',
                                bg='#4b5e5d', fg=WHITE,
                                font=DIGITS_FONT, borderwidth=0,
                                command=lambda x='/': self.append_operator(x))
        self.DIVIDE.grid(row=6, column=4, columnspan=2, sticky=tk.NSEW, padx=5, pady=5)

        # 8η γραμμή κουμπιών
        self.PLUS = tk.Button(self.buttons_frame, text='+',
                              bg='#4b5e5d', fg=WHITE,
                              font=DIGITS_FONT, borderwidth=0,
                              command=lambda x='+': self.append_operator(x))
        self.PLUS.grid(row=7, column=3, sticky=tk.NSEW, padx=5, pady=5)

        self.MINUS = tk.Button(self.buttons_frame, text='-',
                               bg='#4b5e5d', fg=WHITE,
                               font=DIGITS_FONT, borderwidth=0,
                               command=lambda x='-': self.append_operator(x))
        self.MINUS.grid(row=7, column=4, columnspan=2, sticky=tk.NSEW, padx=5, pady=5)

        # 8η γραμμή κουμπιών
        self.PLUS_MINUS = tk.Button(self.buttons_frame, text="+/-", bg=WHITE, state='disabled',
                                    fg=DIGITS_COLOR, font=DIGITS_FONT, borderwidth=0, command=self.apply_sign)
        self.PLUS_MINUS.grid(row=8, column=0, sticky=tk.NSEW, padx=5, pady=5)

        self.DOT = tk.Button(self.buttons_frame, text=".", bg=WHITE,
                             fg=DIGITS_COLOR, font=DIGITS_FONT, borderwidth=0,
                             command=lambda x='.': self.add_to_value(x))
        self.DOT.grid(row=8, column=2, sticky=tk.NSEW, padx=5, pady=5)

        self.INCREASE_ORDER = tk.Button(self.buttons_frame, text="x10", bg="#4b5e5d",
                                        fg=WHITE, font=INCREASE_ORDER_BUTTON_FONT, borderwidth=0,
                                        command=self.increase_order)
        self.INCREASE_ORDER.grid(row=8, column=3, sticky=tk.NSEW, padx=5, pady=5)

        self.EQUAL = tk.Button(self.buttons_frame, text="=", bg="#0067c0",
                               fg=WHITE, font=DIGITS_FONT, borderwidth=0, command=self.evaluate)
        self.EQUAL.grid(row=8, column=4, sticky=tk.NSEW, padx=5, pady=5)

    def clear(self):
        self.current_value = "0"
        self.total_value = ""
        self.update_current_value()
        self.update_total_value()
        self.isDecimal = False
        self.DOT['state'] = 'normal'


    def evaluate(self):
        self.DOT['state'] = 'normal'
        self.enable_operators()

        self.total_value += self.current_value + ' ='
        self.update_total_value()
        components = self.total_value.split(" ")

        if components[1] == "x":
                    self.current_value = str(eval(components[0] + "*" + components[2]))
        elif components[1] == "/":# 11-6-2022 ελεγχος διαιρεσης με 0
                    if components[2] != "0":
                        self.current_value = str(eval(components[0] + "/" + components[2]))
                    else:
                        self.error = True
                        self.current_value = 'Cannot divide by zero'
                    self.update_current_value()
                    self.total_value = ""
        elif components[1] == "+":
            self.current_value = str(eval(components[0] + "+" + components[2]))
        elif components[1] == "-":
            self.current_value = str(eval(components[0] + "-" + components[2]))
        elif components[1] == "^":
            print("Raising to power")
            self.current_value = str(np.power(eval(components[0]), eval(components[2])))
        elif components[1] == "mod":
            self.current_value = str(eval(components[0] + "%" + components[2]))
        elif components[1] == "R":
            self.current_value = str(np.power(eval(components[0]), 1 / eval(components[2])))

        self.total_value = ""
        self.update_current_value()


    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg="#0067c0",
                           fg=WHITE, font=DIGITS_FONT, borderwidth=0, command=self.evaluate)
        button.grid(row=6, column=3, sticky=tk.NSEW, padx=5, pady=5)

    # Συνάρτηση για την αλλαγή πρόσημου του αριθμού
    def apply_sign(self):
        if self.current_value[0] == "-":
            self.current_value = self.current_value[1:]
        elif self.current_value[0] == "0":
            pass
        else:
            self.current_value = "-" + self.current_value
        self.update_current_value()


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

    def inverse_number(self):# Έλεγχος για διαίρεση με το μηδέν 
        try:
            self.current_value = str(1.0 / float(self.current_value))
        except ZeroDivisionError:
            self.current_value="Cannot divide by zero"
        self.update_current_value()
        self.update_total_value()

    def square_number(self):
        try:
            self.current_value = str(float(self.current_value) ** 2)
            self.update_current_value()
            self.update_total_value()
        except OverflowError:
            self.current_value = 'Infinity'

    def square_root(self):
        self.current_value = str(np.sqrt(float(self.current_value)))
        self.update_current_value()
        self.update_total_value()

    # Συνάρτηση που αφαιρεί ένα ψηφίο από τον αριθμό που πληκτρολογείται.
    # Εκτελείται με το πάτημα του κουμπιού DEL
    def delete(self):
        # Εάν έχει απομείνει μόνο ένα ψηφίο του αριθμού (π.χ. 5)
        # τότε η εκτέλεση της DEL πρέπει να επιστρέψει 0.
        if len(self.current_value) == 1:
            self.current_value = str(0)
        # Εάν έχουν απομείνει δύο ψηφία από τον αριθμό που πληκτρολογείται
        # και ο πρώτο χαρακτήρας είναι το αρνητικό πρόσημο (π.χ. -5)
        # τότε πάλι η εκτέλεση της DEL πρέπει να επιστρέψει 0.
        elif len(self.current_value) == 2 and self.current_value[0] == '-':
            self.current_value = str(0)
        else:
            self.current_value = self.current_value[:-1]
        self.update_current_value()
        self.update_total_value()

    # Συνάρτηση που υπολογίζει τον εκθετικό ενός αριθμού
    # Εκτελείται με το πάτημα του κουμπιού exp
    def increase_order(self):
        if self.current_value == '0':
            self.current_value = str(10 * int(self.current_value))
        else:
            self.current_value = str(10 * float(self.current_value))
        self.update_current_value()
        self.update_total_value()

    def exponent(self):
        try:
            self.current_value = np.exp(float(self.current_value))
            self.update_current_value()
            self.update_total_value()
        except OverflowError:
            self.current_value = 'Infinity'

    def factorial(self):
        try:
            self.current_value = str(np.math.factorial(int(self.current_value)))
        except ValueError:
            self.disable_operators()
            self.error = True
            self.current_value = 'Must be an integer'
        self.update_current_value()
        self.update_total_value()

    def sin(self):
        self.total_value = f"sin({self.current_value}\u00b0) ="
        if (self.current_value == "0" or self.current_value == "180" or self.current_value == "360"):
            self.current_value = 0.0
        else:
            self.current_value = str(np.sin(float(self.current_value) * np.pi / 180))
        self.update_current_value()
        self.update_total_value()

    def cos(self):  # κανω στρογγυλοποιηση ετσι ωστε το cos(60)=0.5  με χρηση της np.round
        self.total_value = f"cos({self.current_value}\u00b0) ="
        if (self.current_value == "90" or self.current_value == "270"):
            self.current_value = 0.0
        else:
            self.current_value = str(np.round((np.cos(float(self.current_value) * np.pi / 180)), 2))
        self.update_current_value()
        self.update_total_value()

    def tan(self):  # Υπολογίζουμε την εφαπτομένη tan προσέχοντας οτι tan(90) και tan(270)δεν ορίζεται και οτι tan(45)=1
        self.total_value = f"tan({self.current_value}\u00b0) ="
        if self.current_value == "90" or self.current_value == "270":
            self.current_value = "Invalid input"
        else:
            self.current_value = str(np.round((np.tan(float(self.current_value) * np.pi / 180)), 2))
        self.update_current_value()
        self.update_total_value()

    def logarithm(self):
        self.total_value = f"log({self.current_value}) ="
        self.current_value = str(np.log(float(self.current_value)))
        self.update_current_value()
        self.update_total_value()

    def natural_log(self):
        self.total_value = f"ln({self.current_value}) ="
        self.current_value = str(np.log(float(self.current_value)))
        self.update_current_value()
        self.update_total_value()

    def pi(self): #11-6-2022
        self.total_value = str(np.pi)
        self.update_current_value()
        self.update_total_value()

    def precent(self): #11-6-22 Υπολογισμός ποσοστού
        self.current_value = str(float(self.current_value)*0.01)
        self.update_current_value()
        self.update_total_value()

    def rad_to_deg(self):  # μετατροπή rad to degrees με χρήση της numpy.rad2deg
        self.current_value = (str(np.rad2deg(float(self.current_value))) + "\u00b0")
        self.update_current_value()
        self.update_total_value()

    def deg_to_rad(self):  # μετατροπή deg to rad με χρήση της numpy.deg2rad
        self.current_value = (str(np.deg2rad(float(self.current_value))) + " (rad)")
        self.update_current_value()
        self.update_total_value()

    def ten_power(self):#αποτελέσματα για δυνάμεις του 10
        self.current_value = str(10 ** (int(self.current_value)))
        self.update_current_value()
        self.update_total_value()

    def arcsin(self):  # Υπολογισμός τοξου sin
        self.total_value = f"sin\u207B\u00B9({self.current_value})rad="
        self.current_value = str(np.arcsin(float(self.current_value)))
        self.update_current_value()
        self.update_total_value()

    def arccos(self):  # Yπολογισμός τόξου cos
        self.total_value = f"cos\u207B\u00B9({self.current_value})rad="
        self.current_value = str(np.arccos(float(self.current_value)))
        self.update_current_value()
        self.update_total_value()

    def arctan(self):  # Υπολογισμός τόξου tan
        self.total_value = f"tan\u207B\u00B9({self.current_value})rad="
        self.current_value = str(np.arctan(float(self.current_value)))
        self.update_current_value()
        self.update_total_value()

    def absolute(self):#Υπολογισμός απόλυτης τιμής
        self.current_value = str(np.abs(float(self.current_value)))
        self.update_current_value()
        self.update_total_value()

    def memory_clear(self):
        self.memory = None

    def memory_add(self, val):
        self.memory = val

    def memory_recal(self):
        if self.memory:
            self.current_value = self.memory
            self.update_current_value()
        else:
            pass



    def disable_operators(self):
        self.PLUS['state'] = 'disabled'
        self.MINUS['state'] = 'disabled'
        self.DIVIDE['state'] = 'disabled'
        self.MULTIPLY['state'] = 'disabled'
        self.DOT['state'] = 'disabled'
        self.DEL['state'] = 'disabled'
        self.INCREASE_ORDER['state'] = 'disabled'
        self.INVERSE['state'] = 'disabled'
        self.LOG['state'] = 'disabled'
        self.LN['state'] = 'disabled'
        self.COS['state'] = 'disabled'
        self.SIN['state'] = 'disabled'
        self.TAN['state'] = 'disabled'
        self.SQROOT['state'] = 'disabled'
        self.SQUARE['state'] = 'disabled'
        self.EXP['state'] = 'disabled'
        self.FACTORIAL['state'] = 'disabled'
        self.PLUS_MINUS['state'] = 'disabled'
        self.MOD['state'] = 'disable'


    def enable_operators(self):
        self.PLUS_MINUS['state'] = 'normal'
        self.DOT['state'] = 'normal'
        self.PLUS['state'] = 'normal'
        self.MINUS['state'] = 'normal'
        self.DIVIDE['state'] = 'normal'
        self.MULTIPLY['state'] = 'normal'
        self.DOT['state'] = 'normal'
        self.DEL['state'] = 'normal'
        self.INCREASE_ORDER['state'] = 'normal'
        self.INVERSE['state'] = 'normal'
        self.LOG['state'] = 'normal'
        self.LN['state'] = 'normal'
        self.COS['state'] = 'normal'
        self.SIN['state'] = 'normal'
        self.TAN['state'] = 'normal'
        self.SQROOT['state'] = 'normal'
        self.SQUARE['state'] = 'normal'
        self.EXP['state'] = 'normal'
        self.MOD['state'] = 'normal'

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()

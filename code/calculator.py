# ------------------------------------------
# ---        PROJECT: CALCULATOR         ---
# ------------------------------------------
# Περιγραφή
# ------------------------------------------
# Δημιουργία calculator στα πλαίσια την
# εργασίας της ενότητας ΠΛΗΠΡΟ του ΕΑΠ.
# ------------------------------------------
# Δημιουργήθηκε στις: 4/2022
# Τελευταία ενημέρωση: 5/6/2022
# ------------------------------------------
# Authors:
# ΣΚΡΕΚΑΣ ΠΑΣΧΑΛΗΣ
# ΒΕΡΓΟΥ ΝΙΚΙ
# ΚΑΤΕΡΙΝΑ
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

        # Dictionary για την αποθήκευση των ψηφίων του calculator
        # Η χρήση dictionary βοηθά στον ορισμό των ψηφίων του calculator
        # μέσω μιας δομής επανάληψης for για την αποφυγή επανάληψης κώδικα.
        # Τα δεδομένα του Dictionary αποθηκεύουν τα ψηφία στη μορφή:
        # ψηφίο: (αριθμός γραμμής, αριθμός στήλης)
        # όπου αριθμός γραμμής και στήλης είναι η γραμμή και η στήλη του δικτύου (grid)
        # το οποίο χρησιμοποιείται παρακάτω για την τοποθέτηση των ψηφίων στο παράθυρο της
        # εφαρμογής
        self.digits = {
            7: (3, 0), 8: (3, 1), 9: (3, 2),
            4: (4, 0), 5: (4, 1), 6: (4, 2),
            3: (5, 2), 2: (5, 1), 1: (5, 0),
            0: (6, 1)
        }

        self.total_value = ""
        self.current_value = "0"
        self.angle_mode = 'radians'

        #
        self.screen_frame = self.create_screen_frame()
        self.total_value_lbl, self.current_value_lbl, self.angle_mode_lbl = self.create_display_readings()

        self.buttons_frame = self.create_buttons_frame()

        # Καθορισμός του βάρους των γραμμών και των στύλων
        # του grid κουμπιών (ισοκατανομή)
        for i in range(7):
            self.buttons_frame.rowconfigure(i, weight=1, pad=0)

        for i in range(5):
            self.buttons_frame.columnconfigure(i, weight=1, pad=0)

        # Καλώ τις συναρτήσεις για την δημιουργία των κουμπιών στο GUI
        self.create_digit_buttons()
        self.create_other_buttons()

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
            print('Setting isDecimal to True')
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

    def create_other_buttons(self):
        # 1η γραμμή κουμπιών
        self.MC = button = tk.Button(self.buttons_frame, text='MC',
                                     bg='#ebdec0', fg=OPERATION_COLOR,
                                     font=FUNCTIONS_FONT, borderwidth=0)
        self.MC.grid(row=0, column=0, sticky=tk.NSEW, padx=5, pady=5)

        self.MR = button = tk.Button(self.buttons_frame, text='MR',
                                     bg='#ebdec0', fg=OPERATION_COLOR,
                                     font=FUNCTIONS_FONT, borderwidth=0)
        self.MR.grid(row=0, column=1, sticky=tk.NSEW, padx=5, pady=5)

        self.M_plus = tk.Button(self.buttons_frame, text='M+',
                                bg='#ebdec0', fg=OPERATION_COLOR,
                                font=FUNCTIONS_FONT, borderwidth=0)
        self.M_plus.grid(row=0, column=2, sticky=tk.NSEW, padx=5, pady=5)

        self.M_minus = tk.Button(self.buttons_frame, text='M-',
                                 bg='#ebdec0', fg=OPERATION_COLOR,
                                 font=FUNCTIONS_FONT, borderwidth=0)
        self.M_minus.grid(row=0, column=3, sticky=tk.NSEW, padx=5, pady=5)

        self.MS = tk.Button(self.buttons_frame, text="MS",
                            bg='#ebdec0', fg=DIGITS_COLOR,
                            font=FUNCTIONS_FONT,
                            borderwidth=0, command=lambda: self.clear())
        self.MS.grid(row=0, column=4, sticky=tk.NSEW, padx=5, pady=5)

        # 2η γραμμή κουμπιών
        self.EXP = tk.Button(self.buttons_frame, text='exp',
                             bg='#c9c5ab', fg=OPERATION_COLOR,
                             font=FUNCTIONS_FONT, borderwidth=0,
                             command=self.exponent)
        self.EXP.grid(row=1, column=0, sticky=tk.NSEW, padx=5, pady=5)

        self.FACTORIAL = tk.Button(self.buttons_frame, text='!x',
                                   bg='#c9c5ab', fg=OPERATION_COLOR,
                                   font=FUNCTIONS_FONT, borderwidth=0,
                                   command=self.factorial)
        self.FACTORIAL.grid(row=1, column=1, sticky=tk.NSEW, padx=5, pady=5)

        self.SIN = tk.Button(self.buttons_frame, text='sin',
                             bg='#c9c5ab', fg=OPERATION_COLOR,
                             font=FUNCTIONS_FONT, borderwidth=0,
                             command=self.sin)
        self.SIN.grid(row=1, column=2, sticky=tk.NSEW, padx=5, pady=5)

        self.COS = tk.Button(self.buttons_frame, text="cos", bg='#c9c5ab',
                             fg=OPERATION_COLOR, font=FUNCTIONS_FONT,
                             borderwidth=0, command=self.cos)
        self.COS.grid(row=1, column=3, sticky=tk.NSEW, padx=5, pady=5)

        self.TAN = tk.Button(self.buttons_frame, text="tan", bg='#c9c5ab',
                             fg=OPERATION_COLOR, font=FUNCTIONS_FONT,
                             borderwidth=0, command=self.tan)
        self.TAN.grid(row=1, column=4, sticky=tk.NSEW, padx=5, pady=5)
        #Προσθήκη δύο προσωρινών κουμπιών
        #Θα αντικατασταθούν με αυτά της Κατερίνας
        #-----------------------------------------------------------------------------
        #Μεγάλη προσοχή θα πρέπει να δοθεί στα commands
        #command=lambda:self.add_to_value(" ^ ")
        #command=lambda:self.add_to_value(" R ")
        #Τόσο η δύναμη όσο και η νιοστή ρίζα είναι ΤΕΛΕΣΤΕΣ
        #Αυτό σημαίνει ότι μπαίνουν ανάμεσα στους αριθμούς
        #Ακριβώς όπως η +, - κλπ
        #Άρα 2 ^ 5 -----> ΔΥΟ ΕΙΣ ΤΗΝ ΠΕΜΠΤΗ
        #27 R 3 Κυβική ρίζα του 27

        self.X_Y = tk.Button(self.buttons_frame, text="x^y", bg='#c9c5ab',
                             fg=OPERATION_COLOR, font=FUNCTIONS_FONT,
                             borderwidth=0, command=lambda:self.add_to_value(" ^ "))
        self.X_Y.grid(row=1, column=5, sticky=tk.NSEW, padx=5, pady=5)

        self.nRX = tk.Button(self.buttons_frame, text="\u207f\u221Ax", bg='#c9c5ab',
                             fg=OPERATION_COLOR, font=FUNCTIONS_FONT,
                             borderwidth=0, command=lambda:self.add_to_value(" R "))
        self.nRX.grid(row=1, column=6, sticky=tk.NSEW, padx=5, pady=5)

        #---------------------------------------------------------------------------
        # 3η γραμμή κουμπιών
        self.INVERSE = tk.Button(self.buttons_frame, text='1/x',
                                 bg='#c9c5ab', fg=OPERATION_COLOR,
                                 font=FUNCTIONS_FONT, borderwidth=0,
                                 command=self.inverse_number)
        self.INVERSE.grid(row=2, column=0, sticky=tk.NSEW, padx=5, pady=5)

        self.SQUARE = tk.Button(self.buttons_frame, text='x^2 ',
                                bg='#c9c5ab', fg=OPERATION_COLOR,
                                font=FUNCTIONS_FONT, borderwidth=0,
                                command=self.square_number)
        self.SQUARE.grid(row=2, column=1, sticky=tk.NSEW, padx=5, pady=5)

        self.SQROOT = tk.Button(self.buttons_frame, text='√x',
                                bg='#c9c5ab', fg=OPERATION_COLOR,
                                font=FUNCTIONS_FONT, borderwidth=0,
                                command=self.square_root)
        self.SQROOT.grid(row=2, column=2, sticky=tk.NSEW, padx=5, pady=5)

        self.LOG = tk.Button(self.buttons_frame, text='log',
                             bg='#c9c5ab', fg=OPERATION_COLOR,
                             font=FUNCTIONS_FONT, borderwidth=0,
                             command=self.logarithm)
        self.LOG.grid(row=2, column=3, sticky=tk.NSEW, padx=5, pady=5)

        self.LN = tk.Button(self.buttons_frame, text='ln',
                            bg='#c9c5ab', fg=OPERATION_COLOR,
                            font=FUNCTIONS_FONT, borderwidth=0,
                            command=self.natural_log)
        self.LN.grid(row=2, column=4, sticky=tk.NSEW, padx=5, pady=5)

        # 4η γραμμή κουμπιών
        self.DEL = tk.Button(self.buttons_frame, text='DEL',
                             bg='#eda48c', fg=OPERATION_COLOR,
                             font=FUNCTIONS_FONT, borderwidth=0,
                             command=self.delete)
        self.DEL.grid(row=3, column=3, sticky=tk.NSEW, padx=5, pady=5)

        self.AC = tk.Button(self.buttons_frame, text='AC',
                            bg='#eda48c', fg=OPERATION_COLOR,
                            font=FUNCTIONS_FONT, borderwidth=0,
                            command=lambda: self.clear())
        self.AC.grid(row=3, column=4, sticky=tk.NSEW, padx=5, pady=5)


        # 5η γραμμή κουμπιών
        self.MULTIPLY = tk.Button(self.buttons_frame, text='\u00D7',
                           bg='#4b5e5d', fg=WHITE,
                           font=DIGITS_FONT, borderwidth=0,
                           command=lambda x='x': self.append_operator(x))
        self.MULTIPLY.grid(row=4, column=3, sticky=tk.NSEW, padx=5, pady=5)

        self.DIVIDE = tk.Button(self.buttons_frame, text='\u00F7',
                           bg='#4b5e5d', fg=WHITE,
                           font=DIGITS_FONT, borderwidth=0,
                           command=lambda x='/': self.append_operator(x))
        self.DIVIDE.grid(row=4, column=4, columnspan=2, sticky=tk.NSEW, padx=5, pady=5)

        # 6η γραμμή κουμπιών
        self.PLUS = tk.Button(self.buttons_frame, text='+',
                           bg='#4b5e5d', fg=WHITE,
                           font=DIGITS_FONT, borderwidth=0,
                           command=lambda x='+': self.append_operator(x))
        self.PLUS.grid(row=5, column=3, sticky=tk.NSEW, padx=5, pady=5)


        self.MINUS = tk.Button(self.buttons_frame, text='-',
                           bg='#4b5e5d', fg=WHITE,
                           font=DIGITS_FONT, borderwidth=0,
                           command=lambda x='-': self.append_operator(x))
        self.MINUS.grid(row=5, column=4, columnspan=2, sticky=tk.NSEW, padx=5, pady=5)

        # 7η γραμμή κουμπιών
        self.PLUS_MINUS = tk.Button(self.buttons_frame, text="+/-", bg=WHITE, state='disabled',
                           fg=DIGITS_COLOR, font=DIGITS_FONT, borderwidth=0, command=self.apply_sign)
        self.PLUS_MINUS.grid(row=6, column=0, sticky=tk.NSEW, padx=5, pady=5)

        self.DOT = tk.Button(self.buttons_frame, text=".", bg=WHITE,
                           fg=DIGITS_COLOR, font=DIGITS_FONT, borderwidth=0,
                           command=lambda x='.': self.add_to_value(x))
        self.DOT.grid(row=6, column=2, sticky=tk.NSEW, padx=5, pady=5)

        self.INCREASE_ORDER = tk.Button(self.buttons_frame, text="x10", bg="#4b5e5d",
                           fg=WHITE, font=INCREASE_ORDER_BUTTON_FONT, borderwidth=0,
                           command=self.increase_order)
        self.INCREASE_ORDER.grid(row=6, column=3, sticky=tk.NSEW, padx=5, pady=5)

        self.EQUAL = tk.Button(self.buttons_frame, text="=", bg="#0067c0",
                           fg=WHITE, font=DIGITS_FONT, borderwidth=0, command=self.evaluate)
        self.EQUAL.grid(row=6, column=4, sticky=tk.NSEW, padx=5, pady=5)


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
        if self.error:
            self.current_value = '0'
            self.update_current_value()
            self.update_total_value()
            self.error = False
        else:
            if self.current_value == '0':
                pass
            else:
                self.total_value += self.current_value + ' ='
                self.update_total_value()
                components = self.total_value.split(" ")
                print(components)
                if components[1] == "x":
                        self.current_value = str(eval(components[0] + "*" + components[2]))
                elif components[1] == "/":
                    if components[2] == '0':
                        self.error = True
                        self.current_value = 'Cannot divide by zero'
                    else:
                        self.current_value = str(eval(components[0] + "/" + components[2]))
                elif components[1] == "+":
                    self.current_value = str(eval(components[0] + "+" + components[2]))
                elif components[1] == "-":
                    self.current_value = str(eval(components[0] + "-" + components[2]))
                # Προσθήκη δύο νέων τελεστών των:
                # ^ Δύναμη
                # R Νιοστή ρίζα
                # Για την δύναμη χρησιμοποιούμε την συνάρτηση power
                # της βιβλιοθήκης numpy
                # Η χρήση της γίνεται ως εξής
                # component[0] Είναι ο πρώτος αριθμός από τον χρήστη (Η ΒΑΣΗ)
                # component[1] Είναι ο τελεστής σύμβολο ^
                # component[2] Είναι ο δεύτερος αριθμός από τον χρήστη (Ο ΕΚΘΕΤΗΣ)

                # Στην νιοστή ρίζα έχουμε παρόμοια προσέγγιση εκμεταλλευόμενοι το γεγονός
                # Ότι η τετραγωνική, κυβική, νιοστή ρίζα είναι ένας αριθμός υψωμένος σε κλασματικό εκθέτη
                # Άρα η τετραγωνική ρίζα του 4 είναι 4 ^ 1/2
                # Η κυβική ρίζα του 27 είναι 27 ^ 1/3
                # κλπ
                # Υπάρχει μια διαφοροποίηση σε σχέση με την δύναμη
                # Ότι δηλ. Ο ΠΡΩΤΟΣ ΑΡΙΘΜΟΣ ΔΗΛΩΝΕΙ ΤΟΝ Ν-ΒΑΘΜΟ της ρίζας
                # Και ο δεύτερος την υπόριζο ποσότητα
                # Άρα για την κυβική ρίζα του 27 γράφουμε
                # 3 R 27

                elif components[1] == "^":
                    self.current_value = str(np.power(eval(components[0]), eval(components[2])))
                elif components[1] == "R":
                    self.current_value = str(np.power(eval(components[2]), 1/eval(components[0])))
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

    def inverse_number(self):
        self.current_value = str(1.0/float(self.current_value))
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
        self.total_value = f"sin({self.current_value}) ="
        self.current_value = str(np.sin(float(self.current_value)))
        self.update_current_value()
        self.update_total_value()

    def cos(self):
        self.total_value = f"cos({self.current_value}) ="
        self.current_value = str(np.cos(float(self.current_value)))
        self.update_current_value()
        self.update_total_value()

    def tan(self):
        self.total_value = f"tan({self.current_value}) ="
        self.current_value = str(np.tan(float(self.current_value)))
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

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()

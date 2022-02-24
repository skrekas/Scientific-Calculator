import tkinter as tk
from calculator import *

class CalculatorMenu(Calculator):

    # Αρχικοποίηση του menu της εφαρμογής calculator
    def __init__(self, window):
        self.window = window

        menu_bar = tk.Menu(self.window)

        mode_menu = tk.Menu(menu_bar, tearoff=0)

        mode_menu.add_command(label="Standard", command=self.change_mode_to_standard)
        mode_menu.add_command(label="Scientific", command=self.change_mode_to_scientific)

        mode_menu.add_separator()

        # Preferences submenu
        preferences_menu = tk.Menu(mode_menu, tearoff=0)
        preferences_menu.add_command(label="Colors")
        preferences_menu.add_command(label="Fonts")
        mode_menu.add_cascade(label="Preferences", menu=preferences_menu)

        mode_menu.add_separator()
        mode_menu.add_command(label="Exit", command=self.window.destroy)

        menu_bar.add_cascade(label="Mode", menu=mode_menu, underline=0)

        self.window.config(menu=menu_bar)


    def change_mode_to_standard(self):
        self.window.geometry("500x600")
        self.window.title("Calculator (Standard Mode)")

    def change_mode_to_scientific(self):
        self.window.geometry("800x1000")
        self.window.title("Calculator (Scientific Mode)")
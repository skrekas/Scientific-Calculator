import tkinter as tk
from tkinter import ttk
import tkinter.font as font

class Calculator(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator")
        self.geometry('400x400+50+50')
        self.resizable(True, True)
        self.config(bg="#757575")
        # Add application icom
        self.iconbitmap("./assets/icon.ico")

        # Set application minimum size (to avoid distortion)
        self.minsize(400, 400)

        self.build_menu()
        self.layout()

    def build_menu(self):
        menubar = tk.Menu(self, tearoff=0)
        self.config(menu=menubar)

        file_menu = tk.Menu(menubar)
        file_menu.add_command(label="Exit", command=self.destroy)

        menubar.add_cascade(label="File", menu=file_menu)

    def layout(self):
        val_pad_x = 1
        val_pad_y = 1

        btn_font = font.Font(family='Helvetica', size=14, weight='normal')
        input_font = font.Font(family='Helvetica', size=20, weight='bold')

        self.columnconfigure(0, pad=3, weight=1)
        self.columnconfigure(1, pad=3, weight=1)
        self.columnconfigure(2, pad=3, weight=1)
        self.columnconfigure(3, pad=3, weight=1)

        self.rowconfigure(0, pad=3, weight=1)
        self.rowconfigure(1, pad=3, weight=1)
        self.rowconfigure(2, pad=3, weight=1)
        self.rowconfigure(3, pad=3, weight=1)
        self.rowconfigure(4, pad=3, weight=1)
        self.rowconfigure(5, pad=3, weight=1)
        self.rowconfigure(6, pad=3, weight=1)

        # --- Input: Row 0 ---
        self.entry = tk.Entry(self, font=input_font, background='#e6e6e6')
        self.entry.grid(row=0, columnspan=4, sticky=tk.NSEW)

        # --- Buttons: Row 1 ---
        perc = tk.Button(self, text="%", background='#3b3b3b', foreground='white', font=btn_font)
        perc.grid(row=1, column=0, sticky=tk.NSEW, padx=val_pad_x, pady=val_pad_y)

        ce = tk.Button(self, text="CE", background='#3b3b3b', foreground='white', font=btn_font)
        ce.grid(row=1, column=1, sticky=tk.NSEW, padx=val_pad_x, pady=val_pad_y)

        c = tk.Button(self, text="C", background='#3b3b3b', foreground='white', font=btn_font)
        c.grid(row=1, column=2, sticky=tk.NSEW, padx=val_pad_x, pady=val_pad_y)

        backspace = tk.Button(self, text="Del", background='#3b3b3b', foreground='white', font=btn_font)
        backspace.grid(row=1, column=3, sticky=tk.NSEW, padx=val_pad_x, pady=val_pad_y)

        # --- Buttons: Row 1 ---
        one_over = tk.Button(self, text="1/x", background='#3b3b3b', foreground='white', font=btn_font)
        one_over.grid(row=2, column=0, sticky=tk.NSEW, padx=val_pad_x, pady=val_pad_y)

        x_square = tk.Button(self, text="x^2", background='#3b3b3b', foreground='white', font=btn_font)
        x_square.grid(row=2, column=1, sticky=tk.NSEW, padx=val_pad_x, pady=val_pad_y)

        sqrt_root = tk.Button(self, text="sqrt", background='#3b3b3b', foreground='white', font=btn_font)
        sqrt_root.grid(row=2, column=2, sticky=tk.NSEW, padx=val_pad_x, pady=val_pad_y)

        div = tk.Button(self, text="/", background='#3b3b3b', foreground='white', font=btn_font)
        div.grid(row=2, column=3, sticky=tk.NSEW, padx=val_pad_x, pady=val_pad_y)

        # --- Buttons: Row 3 ---
        seven = tk.Button(self, text="7", background='#3b3b3b', foreground='white', font=btn_font, command=lambda: self.update_input(7))
        seven.grid(row=3, column=0, sticky=tk.NSEW, padx=val_pad_x, pady=val_pad_y)

        eight = tk.Button(self, text="8", background='#3b3b3b', foreground='white', font=btn_font, command=lambda: self.update_input(8))
        eight.grid(row=3, column=1, sticky=tk.NSEW, padx=val_pad_x, pady=val_pad_y)

        nine = tk.Button(self, text="9", background='#3b3b3b', foreground='white', font=btn_font, command=lambda: self.update_input(9))
        nine.grid(row=3, column=2, sticky=tk.NSEW, padx=val_pad_x, pady=val_pad_y)

        multi = tk.Button(self, text="X", background='#3b3b3b', foreground='white', font=btn_font)
        multi.grid(row=3, column=3, sticky=tk.NSEW, padx=val_pad_x, pady=val_pad_y)

        # --- Buttons: Row 4 ---
        four = tk.Button(self, text="4", background='#3b3b3b', foreground='white', font=btn_font, command=lambda: self.update_input(4))
        four.grid(row=4, column=0, sticky=tk.NSEW, padx=val_pad_x, pady=val_pad_y)

        five = tk.Button(self, text="5", background='#3b3b3b', foreground='white', font=btn_font, command=lambda: self.update_input(5))
        five.grid(row=4, column=1, sticky=tk.NSEW, padx=val_pad_x, pady=val_pad_y)

        six = tk.Button(self, text="6", background='#3b3b3b', foreground='white', font=btn_font, command=lambda: self.update_input(6))
        six.grid(row=4, column=2, sticky=tk.NSEW, padx=val_pad_x, pady=val_pad_y)

        minus = tk.Button(self, text="-", background='#3b3b3b', foreground='white', font=btn_font)
        minus.grid(row=4, column=3, sticky=tk.NSEW, padx=val_pad_x, pady=val_pad_y)

        # --- Buttons: Row 5 ---
        one_btn_icon = tk.PhotoImage(file='./assets/1.png')
        one = tk.Button(self, text=1, background="#3b3b3b", foreground='white', font=btn_font, command=lambda: self.update_input(1))
        one.grid(row=5, column=0, sticky=tk.NSEW, padx=val_pad_x, pady=val_pad_y)

        two = tk.Button(self, text="2", background='#3b3b3b', foreground='white', font=btn_font, command=lambda: self.update_input(2))
        two.grid(row=5, column=1, sticky=tk.NSEW)

        three = tk.Button(self, text="3", background='#3b3b3b', foreground='white', font=btn_font, command=lambda: self.update_input(3))
        three.grid(row=5, column=2, sticky=tk.NSEW, padx=val_pad_x, pady=val_pad_y)

        plus = tk.Button(self, text="+", background='#3b3b3b', foreground='white', font=btn_font)
        plus.grid(row=5, column=3, sticky=tk.NSEW, padx=val_pad_x, pady=val_pad_y)

        # Buttons: Row 6
        plus_minus = tk.Button(self, text="+/-", background='#3b3b3b', foreground='white', font=btn_font)
        plus_minus.grid(row=6, column=0, sticky=tk.NSEW, padx=val_pad_x, pady=val_pad_y)

        zero = tk.Button(self, text="0", background='#3b3b3b', foreground='white', font=btn_font, command=lambda: self.update_input(0))
        zero.grid(row=6, column=1, sticky=tk.NSEW, padx=val_pad_x, pady=val_pad_y)

        comma = tk.Button(self, text=",", background='#3b3b3b', foreground='white', font=btn_font)
        comma.grid(row=6, column=2, sticky=tk.NSEW, padx=val_pad_x, pady=val_pad_y)

        equal = tk.Button(self, text="=", background='#3276c9', foreground='white', font=btn_font)
        equal.grid(row=6, column=3, sticky=tk.NSEW, padx=val_pad_x, pady=val_pad_y)


    def update_input(self, button_id):
        if button_id == 0:
            self.entry.insert(len(self.entry.get()), '0')
        if button_id == 1:
            self.entry.insert(len(self.entry.get()), '1')
        elif button_id == 2:
            self.entry.insert(len(self.entry.get()), '2')
        elif button_id == 3:
            self.entry.insert(len(self.entry.get()), '3')
        elif button_id == 4:
            self.entry.insert(len(self.entry.get()), '4')
        elif button_id == 5:
            self.entry.insert(len(self.entry.get()), '5')
        elif button_id == 6:
            self.entry.insert(len(self.entry.get()), '6')
        elif button_id == 7:
            self.entry.insert(len(self.entry.get()), '7')
        elif button_id == 8:
            self.entry.insert(len(self.entry.get()), '8')
        elif button_id == 9:
            self.entry.insert(len(self.entry.get()), '9')


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()









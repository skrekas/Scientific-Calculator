import tkinter as tk
from tkinter import ttk

def build_layout(root):
    root.columnconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    calculator_input = ttk.Entry(root, font=('Times New Roman', 12, 'normal'))
    calculator_input.grid(column=0, columnspan=3, row=0, sticky=tk.N, padx=1, pady=1)

    one_btn = ttk.Button(text="1")
    one_btn.grid(column=0, row=1, padx=2, pady=2)

    two_btn = ttk.Button(text="2")
    two_btn.grid(column=1, row=1, padx=2, pady=2)

    three_btn = ttk.Button(text="3")
    three_btn.grid(column=2, row=1, padx=2, pady=2)
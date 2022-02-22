import tkinter as tk


def build_menu(root):
    menubar = tk.Menu(root, tearoff=False)
    root.config(menu=menubar)

    file_menu = tk.Menu(menubar, tearoff=1)
    file_menu.add_command(label="Exit", command=root.destroy)

    menubar.add_cascade(label="File", menu=file_menu)


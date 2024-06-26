import tkinter as tk
from tkinter import ttk
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)


class AboutWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.win_width = 360
        self.win_height = 250
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        self.center_x = int(screen_width/2 - self.win_width/2)
        self.center_y = int(screen_height/2 - self.win_height/2)

        self.geometry(f'{self.win_width}x{self.win_height}+{self.center_x}+{self.center_y}')
        self.resizable(0, 0)
        self.title('About the application')

        about_lbl = ttk.Label(self, wraplength=300, justify='left', padding=(5,50, 0, 0), font=("Helvetica Bold", 12),text="This application is developed by Sukhumjeet Singh and Tamanna Dash as a real-time project for 21CSC205P Database Management Systems as part of their 4th Semester of BTech CSE Core at SRMIST KTR . Main functionality of this app involves managing a restaurant system, facilitating the order process between customer an the kitchen chief. Date of development March 2024.")
        about_lbl.pack()

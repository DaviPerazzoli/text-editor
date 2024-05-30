import tkinter as tk
from typing import List
from style_config import *

class Navbar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(row=1, column=1, sticky='ew')

        self.tabs: List[Tab] = []

    def update_navbar(self):
        for tab in self.tabs:
            tab.pack(side=tk.LEFT)
    
    def new_tab(self, file):
        if file == '':
            file = 'New file*'
        self.tabs.append(Tab(self, file))

class Tab (tk.Frame):
    def __init__(self, parent, file):
        self.file = file
        self.file_name = file.split('/')[-1]
        super().__init__(parent, font=CODE_FONT)

        self.file_label = tk.Label(self, text=self.file_name)
        self.file_label.pack(side=tk.LEFT)

        self.close_button = tk.Button(self, text='X')
        self.close_button.pack(side=tk.RIGHT)
        self.pack(side=tk.LEFT, padx=5, pady=5)

        self.main_frame = self.parent.parent.main_frame

        self.bind('<Button-1>', self.handle_click)
    
    def handle_click(self):
        file_content = self.parent.parent.read_file(self.file)
        self.main_frame.textbox.delete('1.0', tk.END)
        self.main_frame.textbox.insert(tk.END, file_content)
        self.main_frame.update_textbox()
    
    def handle_close_btn_click(self):
        



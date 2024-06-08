import tkinter as tk
from typing import List
from style_config import *

class Navbar(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.grid(row=1, column=1, sticky='ew')

        self.app = app
        self.main_frame = app.main_frame

        self.tabs: List[Tab] = []

        self.new_tab('C:/Users/Tufic/Desktop/CURSOS/text-editor/vision/teste.txt')

    def update_navbar(self):
        for tab in self.tabs:
            tab.pack(side=tk.LEFT)
    
    def new_tab(self, file):
        tab = Tab(self, file)
        self.tabs.append(tab)
        self.app.current_file = tab.file

class Tab (tk.Frame):
    def __init__(self, parent, file: str):
        
        self.file = file
        self.text = ''

        try:
            self.file_name = file.split('/')[-1]
        except IndexError:
            self.file_name = 'New file'
        
        super().__init__(parent)

        self.parent = parent

        self.file_label = tk.Label(self, text=self.file_name, font=CODE_FONT, bg='blue')
        self.file_label.pack(side=tk.LEFT)

        self.close_button = tk.Button(self, text='X')
        self.close_button.pack(side=tk.RIGHT)
        self.pack(side=tk.LEFT, padx=5, pady=5)

        self.main_frame = self.parent.main_frame
        
        self.handle_click()

        self.file_label.bind('<Button-1>', self.handle_click)
        self.close_button.bind('<Button-1>', self.close_tab)
    
    def handle_click(self, event = None) -> None:
        self.parent.app.set_current_file(self.file)
        self.uptade_text()
        self.parent.app.set_textbox_text(self.text)
    
    def uptade_text(self):
        self.text: str = self.parent.app.read_file(self.file)

    def close_tab(self, event):
        self.destroy()

import tkinter as tk
from typing import List
from vision.style_config import *

class Navbar(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.grid(row=1, column=1, sticky='ew')

        self.app = app
        self.main_frame = app.main_frame

        self.tabs: List[Tab] = []
        self.active_tab = None

        # self.new_tab('C:/Users/Tufic/Desktop/CURSOS/text-editor/vision/teste.txt')

    def update_navbar(self):
        count=0
        for tab in self.tabs:
            tab.grid(column=count, row=0, sticky='nsw')
            count += 1
    
    def new_tab(self, file):
        tab = Tab(self, file)
        self.tabs.append(tab)
        self.app.set_current_file(tab.file)
    
    def set_all_tab_colors(self, color: str):
        for tab in self.tabs:
            tab.file_label.configure(bg=color)
    
    def set_active_tab(self, tab):
        self.active_tab = tab

class Tab (tk.Frame):
    def __init__(self, parent, file: str):
        
        self.file = file
        self.text = ''

        if self.file == '':
            self.file_name = 'New file'
        else:
            self.file_name = file.split('/')[-1]
        
        
        super().__init__(parent)

        self.parent = parent

        self.file_label = tk.Label(self, text=self.file_name, font=CODE_FONT)
        self.file_label.pack(side=tk.LEFT)

        self.close_button = tk.Button(self, text='X')
        self.close_button.pack(side=tk.RIGHT)
        self.grid(column = len(self.parent.tabs), row=0, sticky='nsw')

        self.main_frame = self.parent.main_frame
        
        self.handle_click()

        self.file_label.bind('<Button-1>', self.handle_click)
        self.close_button.bind('<Button-1>', self.close_tab)
    
    def handle_click(self, event = None) -> None:
        self.parent.app.set_current_file(self.file)
        self.uptade_text()
        self.parent.app.set_textbox_text(self.text)
        self.parent.set_all_tab_colors(TAB_BG_COLOR)
        self.file_label.configure(bg=SELECTED_TAB_BG_COLOR)
        self.configure(bg=SELECTED_TAB_BG_COLOR)
        self.parent.set_active_tab(self)
    
    def uptade_text(self):
        self.text: str = self.parent.app.read_file(self.file)
    
    def update_file(self, file):
        self.file = file
        self.file_name = file.split('/')[-1]
        self.file_label.configure(text=self.file_name)

    def close_tab(self, event):
        self.destroy()
        tab_index = self.parent.tabs.index(self)
        if tab_index > 0:
            self.parent.tabs[tab_index-1].handle_click()
        else:
            self.parent.app.set_textbox_text('')
            self.parent.app.set_current_file('')
        self.parent.tabs.remove(self)
        self.parent.update_navbar()

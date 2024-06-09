import tkinter as tk
from vision.style_config import *

class Main_Frame(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, background=TEXT_BG_COLOR)

        self.parent = parent
        self.grid(row=2,column=1, columnspan=2, sticky='nsew')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_propagate(False)

        self.define_canvas()
    
    def define_canvas(self):
        self.canvas = tk.Canvas(self, background=TEXT_BG_COLOR, highlightthickness=0, borderwidth=0)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.define_vertical_scrollbar()
        self.canvas.config(yscrollcommand = self.vertical_scroll_bar.set)

        self.define_canvas_internal_frame()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        self.define_side_frame()
        self.define_textbox()
    
    def define_vertical_scrollbar(self):
        self.vertical_scroll_bar = tk.Scrollbar(self, orient=tk.VERTICAL, command = self.canvas.yview)
        self.vertical_scroll_bar.grid(row=0, column=1, sticky='ns')
    
    def define_canvas_internal_frame(self):
        self.internal_frame = tk.Frame(self.canvas)
        self.frame_id = self.canvas.create_window((0, 0), window=self.internal_frame, anchor='nw')

        self.canvas.itemconfig(self.frame_id, width = self.canvas.winfo_width())
        self.internal_frame.grid_columnconfigure(1,weight=1)

        self.internal_frame.update_idletasks()
    
    def define_side_frame(self):
        self.side_frame = tk.Frame(self.internal_frame, background=TEXT_BG_COLOR)
        self.side_frame.grid(row=0, column=0, rowspan=2, sticky='ns')
        self.side_frame.grid_columnconfigure(0, weight=1)
        self.side_frame.grid_rowconfigure(0, weight=1)

        self.define_line_count()
    
    def define_line_count(self):
        self.line_count = tk.Label(self.side_frame, anchor='nw', justify=tk.LEFT, width=3, background=TEXT_BG_COLOR, font=CODE_FONT)
        self.line_count.grid(row=0,column=0, sticky='n')
    
    def define_textbox(self):
        self.textbox = tk.Text(self.internal_frame, font=CODE_FONT, wrap='none')
        self.textbox.grid(row=0,column=1, sticky='nsew')
        self.update_textbox_height()

        self.define_textbox_scrollbar()

        self.textbox.config(xscrollcommand = self.horizontal_scrollbar.set)
        self.textbox.update_idletasks()
        self.update_line_count()

        self.textbox.bind('<KeyPress>', self.handle_textbox_keypress)
    
    def define_textbox_scrollbar(self):
        self.horizontal_scrollbar = tk.Scrollbar(self , orient=tk.HORIZONTAL, command = self.textbox.xview)
        self.horizontal_scrollbar.grid(row=2,column=0, columnspan=2, sticky='we')
    
    def get_texbox_lines(self) -> int:
        return self.textbox.count('1.0',tk.END, 'lines')[0]
    
    def update_line_count(self) -> None:
        line_count_text = ''.join((f'{i}\n' for i in range(1, self.get_texbox_lines() + 1)))
        self.line_count.config(text=line_count_text)
    
    def update_textbox_height(self) -> None:
        TEXTBOX_EXTRA_HEIGHT = 10
        self.textbox.configure(height=self.get_texbox_lines() + TEXTBOX_EXTRA_HEIGHT)
    
    def update_textbox(self):
        self.update_line_count()
        self.update_textbox_height()
    
    def handle_textbox_keypress(self, event: tk.Event) -> None:
        # The line count is updated only if ctrl + key (state == 12) or the keys below are pressed
        if event.state == 12 or event.keysym in ('BackSpace', 'Return', 'Delete'):

            # The after_idle method calls the parameter function only after doing everything in the mainloop
            # It is being used to refresh the text widget before updating the line count
            self.textbox.after_idle(self.update_textbox)

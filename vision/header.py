import tkinter as tk
from tkinter import filedialog

class Header_Frame(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.main_frame = app.main_frame
        self.grid(row=0, column=1, columnspan=2, sticky='nw', padx=(25,0))

        self.define_buttons(button_padding=5)

        
    
    def define_buttons(self, button_padding: int) -> None:
        self.new_file_btn = tk.Button(self, text='New File')
        self.open_file_btn = tk.Button(self, text='Open File', command=self.handle_open_file_btn_click)
        self.save_file_btn = tk.Button(self, text='Save', command=self.handle_save_file_btn_click)

        self.new_file_btn.pack(side=tk.LEFT, padx=button_padding, pady=button_padding)
        self.open_file_btn.pack(side=tk.LEFT, padx=button_padding, pady=button_padding)
        self.save_file_btn.pack(side=tk.LEFT, padx=button_padding, pady=button_padding)

    def handle_open_file_btn_click(self, event=None) -> None:
        file_path = filedialog.askopenfilename(
            filetypes=[
                ('All types', '*.*'),
                ('Python', '*.py'),
                ('Text', '*.txt')
                ])
        if file_path:
            file_content = self.parent.read_file(file_path)
            self.main_frame.textbox.delete('1.0', tk.END)
            self.main_frame.textbox.insert(tk.END, file_content)
            self.main_frame.update_textbox()
    
    def handle_save_file_btn_click(self):
        raise NotImplementedError()
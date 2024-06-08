import tkinter as tk
from tkinter import filedialog

class Header_Frame(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
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
            self.app.handle_new_opened_file(file_path)
    
    def handle_save_file_btn_click(self, event=None):
        textbox_content: str = self.main_frame.textbox.get('1.0', tk.END)

        if self.app.current_file == '':
            file = filedialog.asksaveasfile(mode='w')
            file.write(textbox_content)
        else:
            self.app.save_text_to_file(self.app.current_file, textbox_content)

import tkinter as tk

class Header_Frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid(row=0, column=1, columnspan=2, sticky='nw', padx=(25,0))

        self.define_buttons(button_padding=5)
    
    def define_buttons(self, button_padding: int) -> None:
        self.new_file_btn = tk.Button(self, text='New File')
        self.open_file_btn = tk.Button(self, text='Open File')
        self.save_file_btn = tk.Button(self, text='Save File')

        self.new_file_btn.pack(side=tk.LEFT, padx=button_padding, pady=button_padding)
        self.open_file_btn.pack(side=tk.LEFT, padx=button_padding, pady=button_padding)
        self.save_file_btn.pack(side=tk.LEFT, padx=button_padding, pady=button_padding)

    
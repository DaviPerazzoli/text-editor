import tkinter as tk
from tkinter import filedialog

class Header_Frame(tk.Frame):
    def __init__(self, parent, main_frame):
        super().__init__(parent)
        self.main_frame = main_frame
        self.grid(row=0, column=1, columnspan=2, sticky='nw', padx=(25,0))

        self.define_buttons(button_padding=5)
    
    def define_buttons(self, button_padding: int) -> None:
        self.new_file_btn = tk.Button(self, text='New File')
        self.open_file_btn = tk.Button(self, text='Open File', command=self.handle_open_file_click)
        self.save_file_btn = tk.Button(self, text='Save', command=self.save_file)

        self.new_file_btn.pack(side=tk.LEFT, padx=button_padding, pady=button_padding)
        self.open_file_btn.pack(side=tk.LEFT, padx=button_padding, pady=button_padding)
        self.save_file_btn.pack(side=tk.LEFT, padx=button_padding, pady=button_padding)

    def read_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[
                ('All types', '*.*'),
                ('Python', '*.py'),
                ('Text', '*.txt')
                ])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content  = file.read()
                return content
            except FileNotFoundError:
                print('Error: File not found')
            except Exception:
                print(Exception)
        
    #TODO terminar a funcionalidade de salvar o arquivo
    def handle_save_file_click(self):
        file_name = filedialog.asksaveasfilename()
        print(file_name)
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write()
                return content
            except Exception:
                print(Exception)


    def handle_open_file_click(self, event=None):
        file_content = self.read_file()
        self.main_frame.textbox.delete('1.0', tk.END)
        self.main_frame.textbox.insert(tk.END, file_content)
        self.main_frame.update_textbox()
    
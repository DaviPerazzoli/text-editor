from typing import Tuple, Dict, Callable
import tkinter as tk
from vision.header import Header_Frame
from vision.main_frame import Main_Frame
from vision.navbar import Navbar, Tab
from vision.style_config import *

class Text_Editor:
    def __init__(self):
        self.root = tk.Tk()
        self.current_file: str = ''

        self.root.title('Text Editor')

        self.define_geometry()
        
        self.main_frame = Main_Frame(self.root, self)
        self.navbar = Navbar(self.root, self)
        self.header = Header_Frame(self.root, self)

        self.define_menus()

        self.root.update()
        self.handle_resize()
        self.root.bind("<Configure>", self.handle_resize)

        # root grid configuration
        self.root.grid_columnconfigure(0,weight=0) # Explorer
        self.root.grid_columnconfigure(1,weight=1) # Main frame and header

        self.root.grid_rowconfigure(0,weight=0) # Header and explorer
        self.root.grid_rowconfigure(1,weight=0) # Main frame and explorer
        self.root.grid_rowconfigure(2,weight=1) # Main frame and explorer

        self.root.mainloop()
    
    def get_screen_width(self) -> int:
        return self.root.winfo_screenwidth()
    
    def get_screen_height(self) -> int:
        return self.root.winfo_screenheight()

    def define_geometry(self) -> None:
        screen_width = int(self.get_screen_width()*0.8)
        screen_height = int(self.get_screen_height()*0.8)

        self.root.geometry(f'{screen_width}x{screen_height}')
        self.root.state('zoomed')
    
    def define_menus(self) -> None:
        self.menubar = self.new_menu(self.root)

        self.filemenu = self.new_menu(self.menubar, options={
            'New File': self.header.handle_new_file_btn_click,
            'Open file': self.header.handle_open_file_btn_click,
            'Save file': self.header.handle_save_file_btn_click
        })

        self.menubar.add_cascade(menu=self.filemenu, label="File")

        self.root.config(menu=self.menubar)
    
    def new_menu(self, 
            target: tk.Widget,
            separators: Tuple[int] or None = None, 
            options: Dict[str, Callable] or None = None) -> tk.Menu:

        if separators == None:
            separators = ()

        if options == None:
            options = {}
        
        menu = tk.Menu(target, tearoff=0)

        step = 1
        for lab, com in options.items():
            if step in separators:
                menu.add_separator()
            menu.add_command(label=lab, command=com)
            step += 1
        
        return menu
    
    def add_cascades_into(self, 
            target_menu: tk.Menu, 
            cascades: Dict[str, tk.Menu]) -> None:

        for label, menu in cascades.items():
            target_menu.add_cascade(menu, label)
        
    def handle_resize(self, event=None) -> None:
        self.main_frame.config(width=self.get_screen_width(),height=self.get_screen_height())
        self.main_frame.canvas.config(width=self.main_frame.winfo_width())
        self.main_frame.canvas.itemconfig(self.main_frame.frame_id, width = self.get_screen_width())
        self.main_frame.canvas.configure(scrollregion=self.main_frame.canvas.bbox("all"))
    
    def read_file(self, file_path) -> str:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content  = file.read()
            return content
        except FileNotFoundError:
            print('Creating new file...')
            return ''
        except UnicodeDecodeError:
            tk.messagebox.showinfo(title="Decode Error", message='This file uses an unsuported text encoding')
            return ''
        except Exception as e:
            print(e.__class__)
            print(e)
            return ''

    def save_text_to_file(self, file_path: str, content) -> bool:
        try:
            with open(file_path, 'w') as file:
                file.write(content)
            return True
        except Exception as e:
            print(e)
            return False

    def save_file_as(self, file_path: str, content: str) -> bool:
        try:
            with open(file_path, 'x') as file:
                file.write(content)
            return True
        except Exception as e:
            print(e)
            return False
    
    def set_textbox_text(self, text: str):
        self.main_frame.textbox.delete('1.0', tk.END)
        self.main_frame.textbox.insert(tk.END, text)
        self.main_frame.update_textbox()

    def set_current_file(self, file: str):
        self.current_file = file
    
    def handle_new_opened_file(self, file: str):
        self.set_current_file(file)
        tab_is_opened = False
        for tab in self.navbar.tabs:
            if tab.file == file:
                tab.handle_click()
                tab_is_opened = True
        
        if not tab_is_opened:
            self.navbar.new_tab(file)

    def test(self):
        print('test')
    

# def main():
#     text_editor = Text_Editor()

# if __name__ == '__main__':
#     main()
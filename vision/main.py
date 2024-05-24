from typing import Tuple, Dict, Callable
import tkinter as tk

class Text_Editor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Text Editor')

        screen_width = int(self.get_screen_width()*0.8)
        screen_height = int(self.get_screen_height()*0.8)

        self.root.geometry(f'{screen_width}x{screen_height}')
        self.root.state('zoomed')
        
        # Creating the menus
        self.menubar = self.new_menu(self.root)

        self.testmenu = self.new_menu(self.menubar, options={
            'Hello': self.test
        })

        self.menubar.add_cascade(menu=self.testmenu, label="Test")

        self.root.config(menu=self.menubar)

        # Creating a header to put the action buttons
        self.header = tk.Frame(self.root)
        self.header.grid(row=0, column=0, columnspan=2)

        # Creating and placing the buttons
        self.new_file_btn = tk.Button(self.header, text='New File')
        self.open_file_btn = tk.Button(self.header, text='Open File')
        self.save_file_btn = tk.Button(self.header, text='Save File')

        HEADER_BUTTON_PADDING = 5
        self.new_file_btn.pack(side=tk.LEFT, padx=HEADER_BUTTON_PADDING, pady=HEADER_BUTTON_PADDING)
        self.open_file_btn.pack(side=tk.LEFT, padx=HEADER_BUTTON_PADDING, pady=HEADER_BUTTON_PADDING)
        self.save_file_btn.pack(side=tk.LEFT, padx=HEADER_BUTTON_PADDING, pady=HEADER_BUTTON_PADDING)

        #Creating the side frame for the line count
        self.side_frame = tk.Frame(self.root, background='#FFF')
        self.side_frame.grid(row=1, column=0, sticky='ns')
        self.side_frame.columnconfigure(0, weight=1)
        self.side_frame.rowconfigure(0, weight=1)

        CODE_FONT = ('consolas', 11)

        self.line_count = tk.Label(self.side_frame, text='', anchor='nw', justify=tk.LEFT, width=3, background='#FFFFFF', font=CODE_FONT)
        self.line_count.grid(row=0,column=0, sticky='n')

        # Creating the textbox
        
        self.textbox = tk.Text(self.root, font=CODE_FONT)
        self.textbox.grid(row=1,column=1, sticky='nsew')

        self.root.columnconfigure(0,weight=0)
        self.root.columnconfigure(1,weight=1)
        self.root.rowconfigure(1,weight=1)
        
        self.textbox.bind('<KeyRelease>', self.update_line_count)
        self.root.mainloop()
    
    def get_screen_width(self):
        return self.root.winfo_screenwidth()
    
    def get_screen_height(self):
        return self.root.winfo_screenheight()
    
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
        
    def get_texbox_lines(self) -> int:
        return self.textbox.count('1.0',tk.END, 'lines')[0]
    
    def update_line_count(self, event=None) -> None:
        line_count_text = ''.join((f'{i}\n' for i in range(1, self.get_texbox_lines() + 1)))
        self.line_count.config(text=line_count_text)
        # print('key pressed')
        

    def test(self):
        # print('hello world')
        
        print(self.get_texbox_lines())
    

def main():
    text_editor = Text_Editor()

if __name__ == '__main__':
    main()
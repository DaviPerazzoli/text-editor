from typing import Tuple, Dict, Callable
import tkinter as tk
from time import sleep

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
        self.header.grid(row=0, column=1, columnspan=2, sticky='nw', padx=(25,0))

        # Creating and placing the buttons
        self.new_file_btn = tk.Button(self.header, text='New File')
        self.open_file_btn = tk.Button(self.header, text='Open File')
        self.save_file_btn = tk.Button(self.header, text='Save File')

        HEADER_BUTTON_PADDING = 5
        self.new_file_btn.pack(side=tk.LEFT, padx=HEADER_BUTTON_PADDING, pady=HEADER_BUTTON_PADDING)
        self.open_file_btn.pack(side=tk.LEFT, padx=HEADER_BUTTON_PADDING, pady=HEADER_BUTTON_PADDING)
        self.save_file_btn.pack(side=tk.LEFT, padx=HEADER_BUTTON_PADDING, pady=HEADER_BUTTON_PADDING)

        #*_________________________________________________________________________________________________________________________________
    
        #Creating the main frame
        TEXT_BG_COLOR = '#FFF'

        self.main_frame = tk.Frame(self.root, background=TEXT_BG_COLOR)
        self.main_frame.grid(row=1,column=1, columnspan=2, sticky='nsew')
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_propagate(False)

        #Creating a canvas to make the main frame scrollable

        self.canvas = tk.Canvas(self.main_frame, background='blue')
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.vertical_scroll_bar = tk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command = self.canvas.yview)
        self.vertical_scroll_bar.grid(row=0, column=1, sticky='ns')
        self.canvas.config(yscrollcommand = self.vertical_scroll_bar.set)

        self.internal_frame = tk.Frame(self.canvas)
        self.frame_id = self.canvas.create_window((0, 0), window=self.internal_frame, anchor='nw')

        self.canvas.itemconfig(self.frame_id, width = self.canvas.winfo_width())

        self.internal_frame.update_idletasks()

        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        #Creating the side frame for the line count
        self.side_frame = tk.Frame(self.internal_frame, background=TEXT_BG_COLOR)
        self.side_frame.grid(row=0, column=0, rowspan=2, sticky='ns')
        self.side_frame.grid_columnconfigure(0, weight=1)
        self.side_frame.grid_rowconfigure(0, weight=1)

        CODE_FONT = ('consolas', 11)

        self.line_count = tk.Label(self.side_frame, anchor='nw', justify=tk.LEFT, width=3, background=TEXT_BG_COLOR, font=CODE_FONT)
        
        self.line_count.grid(row=0,column=0, sticky='n')
        
        # Creating the textbox
        
        self.textbox = tk.Text(self.internal_frame, font=CODE_FONT, wrap='none')
        self.textbox.grid(row=0,column=1, sticky='nsew')
        self.update_line_count()

        self.root.update()
        self.handle_resize()
        self.root.bind("<Configure>", self.handle_resize)

        self.textbox.bind('<KeyPress>', self.handle_textbox_keypress)

        # root grid configuration
        self.root.columnconfigure(0,weight=0) # Explorer
        self.root.columnconfigure(1,weight=1) # Main frame
        self.root.rowconfigure(1,weight=1) # Main frame

        # internal frame grid configuration
        self.internal_frame.columnconfigure(1,weight=1)
        self.internal_frame.rowconfigure(1,weight=0) # textbox scrollbar
        
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
    
    def update_line_count(self) -> None:
        line_count_text = ''.join((f'{i}\n' for i in range(1, self.get_texbox_lines() + 1)))
        self.line_count.config(text=line_count_text)
    
    def handle_textbox_keypress(self, event: tk.Event) -> None:
        # The line count is updated only if ctrl + key (state == 12) or the keys below are pressed
        if event.state == 12 or event.keysym in ('BackSpace', 'Return', 'Delete'):

            # The after_idle method calls the parameter function only after doing everything in the mainloop
            # It is being used to refresh the text widget before updating the line count
            self.textbox.after_idle(self.update_line_count)
            self.textbox.configure(height=self.get_texbox_lines())
    
    def handle_resize(self, event=None):
        self.main_frame.config(width=self.get_screen_width(),height=self.get_screen_height())
        self.canvas.itemconfig(self.frame_id, width = self.get_screen_width())
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def test(self):
        print('test')

def main():
    text_editor = Text_Editor()

if __name__ == '__main__':
    main()
from typing import List, Dict, Callable
import tkinter as tk

class Text_Editor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Text Editor')

        screen_width = int(self.getScreenWidth()*0.8)
        screen_height = int(self.getScreenHeight()*0.8)

        self.root.geometry(f'{screen_width}x{screen_height}')
        self.root.state('zoomed')
        
        # Creating the menus
        self.menubar = self.newMenu(self.root)

        self.testmenu = self.newMenu(self.menubar, options={
            'Hello': test
        })

        self.menubar.add_cascade(menu=self.testmenu, label="Test")

        self.root.config(menu=self.menubar)

        # Creating a header to put the action buttons
        self.header = tk.Frame(self.root)
        self.header.pack(fill=tk.X, side=tk.TOP)

        # Creating and placing the buttons
        self.new_file_btn = tk.Button(self.header, text='New File')
        self.open_file_btn = tk.Button(self.header, text='Open File')
        self.save_file_btn = tk.Button(self.header, text='Save File')

        HEADER_BUTTON_PADDING = 5
        self.new_file_btn.pack(side=tk.LEFT, padx=HEADER_BUTTON_PADDING, pady=HEADER_BUTTON_PADDING)
        self.open_file_btn.pack(side=tk.LEFT, padx=HEADER_BUTTON_PADDING, pady=HEADER_BUTTON_PADDING)
        self.save_file_btn.pack(side=tk.LEFT, padx=HEADER_BUTTON_PADDING, pady=HEADER_BUTTON_PADDING)


        # Creating the textbox
        TEXTBOX_FONT = ('Arial', 11)
        self.textbox = tk.Text(self.root, font=TEXTBOX_FONT)
        self.textbox.pack(fill=tk.BOTH, expand=True, padx=5, side=tk.RIGHT)

        # self.side_frame = tk.Frame(self.root)
        # self.side_frame.pack(side=tk.LEFT, width=20)
        #

        self.root.mainloop()
    
    def getScreenWidth(self):
        return self.root.winfo_screenwidth()
    
    def getScreenHeight(self):
        return self.root.winfo_screenheight()
    
    def newMenu(self, 
            target: tk.Widget,
            separators: List[int] or None = None, 
            options: Dict[str, Callable] or None = None) -> tk.Menu:

        if separators == None:
            separators = []

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
            cascades: Dict[str, tk.Menu]):

        for label, menu in cascades.items():
            target_menu.add_cascade(menu, label)

def test():
    print('hello world')

def main():
    text_editor = Text_Editor()

if __name__ == '__main__':
    main()
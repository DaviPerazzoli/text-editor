from typing import List, Dict, Callable
import tkinter as tk
def ph():
    print('hello world')
class Text_Editor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Text Editor')


        screen_width = int(self.getScreenWidth()*0.8)
        screen_height = int(self.getScreenHeight()*0.8)

        self.root.geometry(f'{screen_width}x{screen_height}')
        self.root.state('zoomed')

        self.menubar = self.newMenu(self.root)

        self.testmenu = self.newMenu(self.menubar, options={
            'Hello': ph
        })

        self.menubar.add_cascade(menu=self.testmenu, label="Test")

        self.root.config(menu=self.menubar)
        

        self.root.mainloop()
    
    def getScreenWidth(self):
        return self.root.winfo_screenwidth()
    
    def getScreenHeight(self):
        return self.root.winfo_screenheight()
    
    def newMenu(self, 
        target,
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



def main():
    text_editor = Text_Editor()

if __name__ == '__main__':
    main()
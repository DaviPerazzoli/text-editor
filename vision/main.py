import tkinter as tk

class Text_Editor:
    def __init__(self):
        self.root = tk.Tk()

        screen_width = int(self.getScreenWidth()*0.8)
        screen_height = int(self.getScreenHeight()*0.8)

        self.root.geometry(f'{screen_width}x{screen_height}')
        self.root.state('zoomed')
        self.root.mainloop()
    
    def getScreenWidth(self):
        return self.root.winfo_screenwidth()
    
    def getScreenHeight(self):
        return self.root.winfo_screenheight()


def main():
    text_editor = Text_Editor()

if __name__ == '__main__':
    main()
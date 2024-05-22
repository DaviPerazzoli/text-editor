import tkinter as tk
from tkinter import messagebox

class MyGUI:

    def __init__(self):
        self.root = tk.Tk()

        # adding a menu (see the result when running)
        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close without question", command=exit)

        self.actionmenu = tk.Menu(self.root, tearoff=0)
        self.actionmenu.add_command(label="Show message", command=self.show_message)


        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")

        self.root.config(menu=self.menubar)
        
        self.label = tk.Label(self.root, text="Your Message", font=('Arial', 18))
        self.label.pack(padx=10, pady= 10)

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        self.textbox.pack(padx=10, pady=10)
        # making an event start when a keypress is detected
        self.textbox.bind('<KeyPress>', self.shortcut)

        # here we are creating a variable to store the state of the checkbox
        self.check_state = tk.IntVar()

        # the checkbox needs to have this parameter variable
        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Arial', 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        # in this button, we pass a function to the command property
        self.button = tk.Button(self.root, text="Show Message", font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        # a btn to clear the textbox
        self.clearbtn = tk.Button(self.root, text="Clear", font=('Arial', 18), command=self.clear)
        self.clearbtn.pack(padx=10, pady=10)

        # when the application is closed, makes something

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
    
    def show_message(self):
        # implementing the functionality:
        if self.check_state.get() == 0:
            # reading what the textbox has into it
            print(self.textbox.get('1.0', tk.END))
        else:
            # using the messagebox import
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))
    
    # the event is passed by the bind method, it has some parameters,
    # mouse coordinates, keysymbol, char, keycode, state
    def shortcut(self, event):
        # print(event.keysym)
        # print(event.state)

        # tested what ctrl + enter did and specified it here
        if event.state == 12 and event.keysym == 'Return':
            self.show_message()
    
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()
    
    def clear(self):
        self.textbox.delete('1.0', tk.END)
            

def main():
    myGUI = MyGUI()

if __name__ == '__main__':
    main()
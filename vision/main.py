import tkinter as tk

# tk.Tk() is the constructor, it returns a new window
root = tk.Tk()

# root.title(string) sets the window title
root.title("Text Editor")

# .geometry("WxH") - define o tamanho inicial da janela 
root.geometry("800x500")

# tk.Label is a label, the first parameter is the parent
label = tk.Label(root, text="Hello world!", font=('Arial', 18))

# the pack is the way to make the element appear
label.pack(padx=20, pady=20)

# Text is a textbox, used to insert Text
# an Entry is just like an input in HTML
text = tk.Text(root ,font=('Arial', 10))
text.pack(padx=10)

# *entry = tk.Entry(root)
# *entry.pack()

# *button = tk.Button(root, text="Click me", font=('Arial', 14))
# *button.pack()

# grid layout is a little bit more interesting

buttonFrame = tk.Frame(root)
#this configures the collumns that the grid has
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonFrame, text='1', font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)





root.mainloop()
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
text = tk.Text(root ,font=('Arial', 10), height=5)
text.pack(padx=10)

# *entry = tk.Entry(root)
# *entry.pack()

# *button = tk.Button(root, text="Click me", font=('Arial', 14))
# *button.pack()

# grid layout is a little bit more interesting

buttonFrame = tk.Frame(root)
#this configures the collumns the grid has
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)
# buttonFrame.rowconfigure(0, weight=1)
# buttonFrame.rowconfigure(1, weight=1)

#creating a lot of buttons and putting them into the frame

btn1 = tk.Button(buttonFrame, text='1', font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonFrame, text='2', font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonFrame, text='3', font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonFrame, text='4', font=('Arial', 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonFrame, text='5', font=('Arial', 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonFrame, text='6', font=('Arial', 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

# fill='x' streches the context on the x axis
buttonFrame.pack(fill='x')

# placing a widget with absolute position
anotherbtn = tk.Button(root, text="test")
anotherbtn.place(x=200,y=200, height=100, width=100)

root.mainloop()
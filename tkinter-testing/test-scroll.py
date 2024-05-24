import tkinter as tk
from tkinter import ttk

# Cria a janela principal
root = tk.Tk()
root.title("Exemplo de Barra de Rolagem")

# Cria um Canvas para permitir a rolagem
canvas = tk.Canvas(root)
canvas.grid(row=0, column=0, sticky='nsew')

# Cria uma Scrollbar vertical ligada ao Canvas
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.grid(row=0, column=1, sticky='ns')

# Configura o Canvas para usar a Scrollbar
canvas.configure(yscrollcommand=scrollbar.set)

# Cria um Frame dentro do Canvas
scrollable_frame = ttk.Frame(canvas)

# Adiciona o Frame ao Canvas com um window_create
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Configura o redimensionamento do Canvas
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Função para redimensionar o Canvas conforme o conteúdo do Frame
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", on_frame_configure)

# Adiciona muitos widgets ao Frame para testar a rolagem
for i in range(50):
    tk.Label(scrollable_frame, text=f"Label {i}").grid(row=i, column=0, padx=10, pady=5)

# Inicia o loop principal da aplicação
root.mainloop()

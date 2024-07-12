import tkinter as tk
from tkinter import filedialog
from pygments import lex
from pygments.lexers import PythonLexer
from pygments.styles import get_style_by_name

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Texto com Syntax Highlighting")
        self.text = tk.Text(self.root, wrap="word", undo=True)
        self.text.pack(expand=1, fill="both")
        self.text.bind("<KeyRelease>", self.on_key_release)

        # Menu
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        file_menu = tk.Menu(self.menu, tearoff=0)
        file_menu.add_command(label="Abrir", command=self.open_file)
        file_menu.add_command(label="Salvar Como", command=self.save_as)
        self.menu.add_cascade(label="Arquivo", menu=file_menu)

        # Configuração do estilo do Pygments
        self.lexer = PythonLexer()
        self.style = get_style_by_name('default')
        self.configure_tags()

    def configure_tags(self):
        for token, style in self.style:
            fg_color = style['color']
            if fg_color:
                self.text.tag_configure(str(token), foreground=f"#{fg_color}")

    def on_key_release(self, event=None):
        self.highlight_syntax()

    def highlight_syntax(self):
        content = self.text.get("1.0", tk.END)
        tokens = lex(content, self.lexer)
        self.text.mark_set("range_start", "1.0")

        for token, content in tokens:
            self.text.mark_set("range_end", f"range_start + {len(content)}c")
            self.text.tag_add(str(token), "range_start", "range_end")
            self.text.mark_set("range_start", "range_end")

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.INSERT, content)
                self.highlight_syntax()

    def save_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text.get(1.0, tk.END)
                file.write(content)

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()

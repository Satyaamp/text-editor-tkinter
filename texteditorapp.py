import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor")
        self.root.geometry("800x600")

        # Optional: Set a custom icon
        try:
            self.root.iconbitmap("editor_icon.ico")  # Add a custom icon if available
        except Exception as e:
            print("Icon file not found, proceeding without it.")

        # Menu bar setup
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        # File menu setup
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        # Text widget setup
        self.text = tk.Text(self.root, wrap=tk.WORD, font=("Helvetica", 14), fg="black", bg="#f0f0f0")
        self.text.pack(expand=tk.YES, fill=tk.BOTH)

    def new_file(self):
        """Clear the current text area to create a new file."""
        self.text.delete(1.0, tk.END)

    def open_file(self):
        """Open an existing text file and display its content."""
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    self.text.delete(1.0, tk.END)
                    self.text.insert(tk.END, file.read())
            except Exception as e:
                messagebox.showerror("Error", f"Could not open the file: {e}")

    def save_file(self):
        """Save the current text to a file."""
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(self.text.get(1.0, tk.END))
                    messagebox.showinfo("Info", "File saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save the file: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()

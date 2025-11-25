import tkinter as tk

root = tk.Tk()
root.title("Test Window")
root.geometry("800x600")
root.resizable(False, False)
my_label = tk.Label(root, text = "Hello world", fg="blue" )
my_label.grid(row=0, column=0)
my_button = tk.Button(root, text="clieck me" )
my_button.grid(row=4, column=5)

root.mainloop()
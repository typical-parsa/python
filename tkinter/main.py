import tkinter as tk

root = tk.Tk()
root.title("Test Window")
root.geometry("800x600")
root.resizable(False, False)
my_label = tk.Label(root, text = "Hello world", fg="blue" )
my_label.pack()
my_button = tk.Button(root, text="clieck me" )
my_button.pack()

root.mainloop()
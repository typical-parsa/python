import tkinter as tk

root = tk.Tk()
root.title("Test Window")
root.geometry("800x600")
root.resizable(False, False)
my_label = tk.Label(root, text = "Hello world", fg="blue" )
my_label.grid(row=0, column=0)
my_label2 = tk.Label(root, text="Not clicked yet", fg="red")
my_label2.grid(row=3, column=3)

def clicked():
    my_label2.config(text="you've clicked the button", fg="green")
    my_label.config(text="By by world", fg="pink")


my_button = tk.Button(root, text="click me", command= clicked )
my_button.grid(row=4, column=5)

entry_box = tk.Entry(root, width=300)
entry_box.grid(row=20, column=20)
root.mainloop()
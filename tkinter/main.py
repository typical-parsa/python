import tkinter as tk

root = tk.Tk()
root.title("Test Window")
root.geometry("800x600")
root.resizable(False, False)
my_label = tk.Label(root, text = "Hello world", fg="blue" )
my_label.pack()
my_label2 = tk.Label(root, text="Not clicked yet", fg="red")
my_label2.pack()
my_label3 = tk.Label(root, text="", fg="black")
my_label3.pack()
global my_label4
my_label4 = tk.Label(root, text="test text", fg="black")
my_label4.pack()
entry_box = tk.Entry(root, width=300)
entry_box.pack()

def clicked():
    my_label2.config(text="you've clicked the button", fg="green")
    my_label.config(text="By by world", fg="purple")
    input_text = entry_box.get()
    my_label3.config(text=input_text, fg="black")

def hide():
    my_label4.pack_forget()

def show():
    my_label4.pack()

my_button = tk.Button(root, text="click me", command= clicked )
my_button.pack()
hide_button = tk.Button(root, text="Hide", command=hide)
hide_button.pack()
show_button = tk.Button(root, text="Show", command=show)
show_button.pack()



root.mainloop()
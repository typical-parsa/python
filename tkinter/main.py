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
entry_box = tk.Entry(root, width=300)
entry_box.pack()

def clicked():
    my_label2.config(text="you've clicked the button", fg="green")
    my_label.config(text="By by world", fg="purple")
    input_text = entry_box.get()
    my_label3.config(text=input_text, fg="black")


my_button = tk.Button(root, text="click me", command= clicked )
my_button.pack()



root.mainloop()
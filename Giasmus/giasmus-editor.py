# Chiasmus editor v0.1
import tkinter as tk
from tkinter import filedialog


def make_chiasm():
    # Gets all of the current text, and inserts it at the end, with the lines
    # in reversed order.
    print("LOG: Pressed 'chiasmate'")
    t = text.get("1.0", "end-1c").splitlines()
    t.reverse()
    # print(t)
    for ct in t:
        text.insert(tk.END, "\n"+ct, 'chiasm_color')


def saveas():
    # Save the current text as a plain-text file
    t = text.get("1.0", "end-1c")
    save_loc = filedialog.asksaveasfile()
    save_file = open(save_loc.name+".txt", "w+")
    save_file.write(t)
    save_file.close()


if __name__ == "__main__":
    # Make a tkinter text-widget
    root = tk.Tk("Chiasmus Editor")
    text = tk.Text(root)
    text.grid()
    # Configure the text color for the chiasmated text
    text.tag_configure('chiasm_color', foreground='#808080')
    # Define and add a button to chiasmate the text
    chiasm_button = tk.Button(root, text="Chiasmate", command=make_chiasm)
    chiasm_button.grid()
    # Define and add a save button
    save_button = tk.Button(root, text="Save", command=saveas)
    save_button.grid()
    # Run the text-widget
    root.mainloop()

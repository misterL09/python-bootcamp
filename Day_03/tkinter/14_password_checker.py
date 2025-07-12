import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.title("Password Checker")
root.geometry("400x200")

label = tkinter.Label(root, text="Enter your password:")
label.pack()

entry = tkinter.Entry(root,show="*")
entry.pack()


user_input = tkinter.StringVar(root, value="Enter your password and press Enter.")
label2 = tkinter.Label(root, textvariable=user_input)
label2.pack()

def show_input(event):
    new_message = None
    given_text = entry.get()
    if entry.get() =="pass":
        new_message = "Password correct! Access granted"
    else:
        new_message = "Incorrect password. Try again"
        messagebox.showerror(
            "Error",
            "This is an error message."
        )
    user_input.set(new_message)



root.bind("<Return>", show_input)
root.bind("<space>", show_input)

root.mainloop()
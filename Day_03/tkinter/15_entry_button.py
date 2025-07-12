import tkinter

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

def show_input():
    if entry.get() =="pass":
        new_message = "Password correct! Access granted"
    else:
        new_message = "Incorrect password. Try again"
    user_input.set(new_message)

button = tkinter.Button(root, text ="Submit", command =show_input)
button.pack()

root.mainloop()
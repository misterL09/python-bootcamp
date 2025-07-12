import tkinter
root = tkinter.Tk()

count = tkinter.IntVar(root, value=0)
label = tkinter.Label(root, textvariable=count)
label.pack()

def increment():
    new_value = count.get() + 1
    count.set(new_value)

def decrement():
    new_value = count.get() - 1

    if new_value <0:
        new_value = 0
    count.set(new_value)

button = tkinter.Button(root, text=" + ", command=increment)
button.pack()

button2 = tkinter.Button(root, text=" - ", command=decrement)
button2.pack()

root.mainloop()
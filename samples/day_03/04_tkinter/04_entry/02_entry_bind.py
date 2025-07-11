import tkinter

root = tkinter.Tk()

entry = tkinter.Entry(root)
entry.pack()

def show_input(event):
	print("Enter pressed")

root.bind("<Return>", show_input)
root.mainloop()

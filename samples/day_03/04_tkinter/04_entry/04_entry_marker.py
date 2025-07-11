import tkinter

root = tkinter.Tk()

entry = tkinter.Entry(root)
entry.pack()

def show_input(event):
	user_input= entry.get()
	print(user_input)

root.bind("<Return>", show_input)
root.bind("<space>", show_input)
root.mainloop()

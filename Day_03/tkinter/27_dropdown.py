import tkinter
root = tkinter.Tk()
dropdown_var = tkinter.StringVar(value="Choice 1")
dropdown_menu = tkinter.OptionMenu(
root, dropdown_var,
"Choice 1",
"Choice 2",
"Choice 3"
)
dropdown_menu.pack()
root.mainloop()
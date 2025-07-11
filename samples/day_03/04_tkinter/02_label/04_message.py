import tkinter

root = tkinter.Tk()

text = "Sentence 1 Sentence 2 Sentence 3"
message = tkinter.Message(root, text=text)
message.pack()

root.mainloop()

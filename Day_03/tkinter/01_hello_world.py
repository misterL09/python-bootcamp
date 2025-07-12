import tkinter

root = tkinter.Tk()
root.title("Sample GUI Application")
root.geometry("1200x400")

label = tkinter.Label(root, text="Hello World")
label.pack()
tkinter.Label(root, text="Hi nathan").pack()

message = """
HELLO
WORLD
"""
label2 = tkinter.Label(root, text = message)
label2.pack()

text = "Sentence 1 Sentence 2 Sentence 3"
message = tkinter.Message(root, text=text)
message.pack()


root.mainloop()
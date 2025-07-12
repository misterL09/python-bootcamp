import tkinter
from tkinter import font

root = tkinter.Tk()
root.title("Sample GUI Application")
root.geometry("1200x400")
all_fonts = font.families()
print(all_fonts)

label = tkinter.Label(
    root,
    text =  "Loops within loops spim, "
            "A silent function returns, "
            "The Logic is clear.",
    font = ("Arial", 14, "bold italic")


)
label.pack()

text = "Loops within loops spim, A silent function returns, The Logic is clear."
message = tkinter.Message(root, text=text)
message.pack()

label3 = tkinter.Label(
    root,text ="Hello",
    fg="red",
    bg="Black",
    font =("Chiller",100),
    width = 800,
    height = 350,
    padx = 10,
    pady = 200
)
label3.pack(side = "right")

tkinter.Label(root, text ="haha").pack(side="right")


root.mainloop()
import tkinter
import json

root = tkinter.Tk()
root.title("User Setting")
root.geometry("200x600")

form_frame = tkinter.Frame(root, padx=50, pady=50)
form_frame.pack()
tkinter.Label(form_frame, text="Name:").grid(row=0, column=0)
entry1 = tkinter.Entry(form_frame)
entry1.grid(row=0, column=1, columnspan=3)
tkinter.Label(form_frame, text="Age:").grid(row=1, column=0)
entry2 = tkinter.Entry(form_frame, show="*")
entry2.grid(row=1, column=1, columnspan=3)
tkinter.Label(form_frame, text="Preferred Theme:").grid(row=2, column=0)
radio1 = tkinter.Radiobutton(form_frame, text="Light", value="Light").grid(row=2, column=1)
radio2 = tkinter.Radiobutton(form_frame, text="Dark", value="Dark").grid(row=2, column=2)

check_value = tkinter.BooleanVar()
checkbox = tkinter.Checkbutton(
root,
text="Subscribe to newsletter",
variable=check_value
)
checkbox.pack()

label3 = tkinter.Label(root, text="Rate us")
label3.pack()
slider_value = tkinter.IntVar(value=0)
slider = tkinter.Scale(
root,
from_=1,
to=5,
orient="horizontal",
variable=slider_value
)
slider.pack()

user_input = tkinter.StringVar(root)
def get_all_input():
    name = entry1.get()
    age = entry2.get()
    theme = radio_var.get()
    subcribe = check_value.get()
    rate = slider_value.get()

    data = [
        {'Name': name, 'Age':age, 'Theme': theme, 'Subcribe':subcribe ,'Rate': rate },
    ]

    """Save  to filepath"""
    with open("user",'w') as file:
        json.dump(data, file)

button = tkinter.Button(root, text ="Submit", command =get_all_input)
button.pack()

root.mainloop()
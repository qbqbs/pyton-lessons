
import tkinter
import random


window = tkinter.Tk() 
window.title("моё окно") 
window.geometry("600x500") 

label = tkinter.Label(text="0", fg="pink", bg="yellow", font="Arial 22")
label.place(x=25, y=25)

def random_color():
    colors = ["red", "green", "blue"]
    label["bg"] = random.choice(colors)

def count():
    random_color()
    num = int(label["text"])
    num = num + 1
    label["text"] = str(num)


button = tkinter.Button(text="change", command = count)
button.place(x=25, y=100)




window.mainloop()
import tkinter

window = tkinter.Tk()
window.title("Hello MF")
window.minsize(width=800, height=500)

my_label = tkinter.Label(text="Aduvip", font=("Arial", 20, "bold"))
my_label.grid(column=0, row=0)


def button_clicked():
    my_label.config(text=input.get())


my_button = tkinter.Button(text="Click me", command=button_clicked)
my_button.grid(column=1, row=1)

button2 = tkinter.Button(text="2nd Button")
button2.grid(column=3, row=0)


input = tkinter.Entry(width=20)
input.grid(column=4, row=3)







window.mainloop()

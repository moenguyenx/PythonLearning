from tkinter import *

window = Tk()
window.title("Miles to Km converter")
window.minsize(width=500, height=300)


def convert():
    km_equivalent.config(text=round(float(mile_entry.get()) * 1.6, 2))


mile_entry = Entry()
mile_entry.grid(column=2, row=1)
mile_label = Label(text="miles", font="arial")
mile_label.grid(column=3, row=1)

equal_title = Label(text="is equal to:", font="arial")
equal_title.grid(column=1, row=2)

km_equivalent = Label(text=0, font="arial")
km_equivalent.grid(column=2, row=2)

km_label = Label(text="km", font="arial")
km_label.grid(column=3, row=2)

convert_button = Button(text="Convert", command=convert)
convert_button.grid(column=2, row=3)

window.mainloop()

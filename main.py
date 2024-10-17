from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=100, height=100)
window.config(padx=25, pady=25)
def calculate():
    miles = float(input.get())
    kilometers = miles*1.609
    km.config(text=f"{kilometers}")

input = Entry(width=10)
input.grid(row=0, column=1)

label1 = Label(text="is equal to", font=("Arial", 24))
label1.grid(row=1, column=0)

label2 = Label(text="Miles", font=("Arial", 24))
label2.grid(row=0, column=2)

km = Label(text="0", font=("Arial", 24))
km.grid(row=1, column=1)

label3 = Label(text="Km", font=("Arial", 24))
label3.grid(row=1, column=2)

button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()
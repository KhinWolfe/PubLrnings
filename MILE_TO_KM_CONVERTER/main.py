from tkinter import*


def calculate():
    out = float(entry.get()) * 1.609
    output_label.config(text=out)
window = Tk()
window.title("Mile to km converter")
window.config(padx=20, pady=20)
#todo input for miles
entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1, row=0)
#todo label for miles
mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)
#todo label for "is equal to"
equal_label = Label(text="is equal to:")
equal_label.grid(column=0, row=1)
#todo label for output
output_label = Label(text="0")
output_label.grid(column=1, row=1)
#todo label for output units
km_label = Label(text="km")
km_label.grid(column=2, row=1)
#todo button for calculate
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)
#TODO FUNCTION TO CALCULATE DIFFERENCE
window.mainloop()
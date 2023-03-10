from tkinter import *


# Global Layout

conv = Tk()
conv.geometry('480x360')
conv.title('convertisseur-de-monnaie')
frame = Frame(conv, width=480, height=480, bg='gray60')
frame.grid(row=0, column=0)
label_historic = []
historic = Listbox(conv, listvariable=label_historic, bg='gray40', width=30)
historic.place(x=280, y=180)


# Set list of currency and StringVar

list_currency = ['Dollar', 'Euro', 'Livre Sterling', 'Yen']
value1 = StringVar()
value2 = StringVar()
change = ''
result = StringVar()

# Button and choice layout

from_currency_label = Label(frame, text='FROM:', justify=LEFT)
from_currency_label.place(x=20, y=30)
to_currency_label = Label(frame, text='TO:', justify=RIGHT)
to_currency_label.place(x=240, y=30)

value1.set(list_currency[0])
from_currency_menu = OptionMenu(frame, value1, *list_currency)
from_currency_menu.place(x=20, y=60)

value2.set(list_currency[1])
to_currency_menu = OptionMenu(frame, value2, *list_currency)
to_currency_menu.place(x=240, y=60)

amount_label = Label(frame, text='AMOUNT:')
amount_label.place(x=20, y=120)

amount_entry = Entry(frame, width=55, textvariable=result)
amount_entry.place(x=20, y=150)

convert_button = Button(frame, width=30, height=5, text="CONVERT", bg='grey40', fg='white', command=lambda: convert_calc())
convert_button.place(x=20, y=200)

clear_history_button = Button(frame, text="CLEAR HISTORY", bg='grey40', fg='white', command=lambda: clear_history())
clear_history_button.place(x=367, y=150)

# Function to convert each currency into another


def convert_calc():
    global change
    change = str(float(result.get()))       # Store input value for the historic result
    historic_memo = change

    # Dollar

    if value1.get() == "Dollar" and value2.get() == "Euro":
        change = str(float(result.get()) * 0.90)
        result.set(change)

    elif value1.get() == "Dollar" and value2.get() == "Livre Sterling":
        change = str(float(result.get()) * 0.80)
        result.set(change)

    elif value1.get() == "Dollar" and value2.get() == "Yen":
        change = str(float(result.get()) * 130)
        result.set(change)

    # Livre Sterling

    elif value1.get() == "Livre Sterling" and value2.get() == "Euro":
        change = str(float(result.get()) * 1.1)
        result.set(change)

    elif value1.get() == "Livre Sterling" and value2.get() == "Dollar":
        change = str(float(result.get()) * 1.2)
        result.set(change)

    elif value1.get() == "Livre Sterling" and value2.get() == "Yen":
        change = str(float(result.get()) * 160)
        result.set(change)

    # Euro

    elif value1.get() == "Euro" and value2.get() == "Dollar":
        change = str(float(result.get()) * 1.08)
        result.set(change)

    elif value1.get() == "Euro" and value2.get() == "Livre Sterling":
        change = str(float(result.get()) * 0.88)
        result.set(change)

    elif value1.get() == "Euro" and value2.get() == "Yen":
        change = str(float(result.get()) * 141)
        result.set(change)

    # Yen

    elif value1.get() == "Yen" and value2.get() == "Dollar":
        change = str(float(result.get()) * 0.008)
        result.set(change)

    elif value1.get() == "Yen" and value2.get() == "Livre Sterling":
        change = str(float(result.get()) * 0.006)
        result.set(change)

    elif value1.get() == "Yen" and value2.get() == "Euro":
        change = str(float(result.get()) * 0.007)
        result.set(change)

    # Display operation values + results

    historic_result = historic_memo + value1.get() + "=" + change + value2.get()
    historic.insert(0, historic_result)  # Display operation values + results

# Button to clear history


def clear_history():
    historic.delete(0, END)



conv.mainloop()
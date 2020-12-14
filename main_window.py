from tkinter import * # importing all options from tkinter for the GUI

class foreign_currency():
    '''This class has a method when called it will take a string to determine the currency value and return it'''
    def determine_foreign_currency(self, selection=""):
        currency = 0.0
        option = selection
        if option == "Australia":
            currency = .74
        elif option == "China":
            currency = .15
        elif option == "India":
            currency = .014
        elif option == "Africa":
            currency = .006
        elif option == "Europe":
            currency = 1.21
        elif option == "Canada":
            currency = .78
        elif option == "Bermudia":
            currency = 1.00
        elif option == "Brazil":
            currency = 5.16
        elif option == "Mexico":
            currency = .051
        elif option == "Russia":
            currency = .013
        elif option == "Japan":
            currency = .0096
        elif option == "Costa Rica":
            currency = .0017
        else:
            print("You need to select a country. Cannot use 'none' in the conversion.")

        return currency



def check_selected_currency():
    """The user will use the dropdown to select what country they are visiting. This will convert the amount
    entered from dollar to the new currency."""
    try:
        dollar_amount = dollar_currency.get()
        parse_entry = int(dollar_amount)

        if parse_entry > 0:
            use_selection = selected.get()
            currency = foreign_currency()
            new_currency = currency.determine_foreign_currency(use_selection)
            new_amount_one = f"{float(new_currency)}"
            new_amount_two = f"{float(parse_entry)}"
            final_amount = float(new_amount_one) * float(new_amount_two)
            answer_label["text"] = final_amount
        else:
            print("You need to enter something besides zero")

    except ValueError:
        print("Invalid selection")



'''Create the GUI'''
display = Tk()
display.title("Currency Converter Calculator")
display.resizable(width=True, height=True)


Options = [
    "none",
    "Australia",
    "China",
    "India",
    "Africa",
    "Brazil"
    "Europe",
    "Canada",
    "Bermudia",
    "Mexico",
    "Russia",
    "Japan",
    "Costa Rica"
]
'''set the default dropdown to none'''
selected = StringVar()
selected.set(Options[0])
'''all options are viewable when clicked'''
dropdown = OptionMenu(display, selected, *Options)



'''create text, label, grid, and buttons for GUI'''
user_input = Frame(master=display)
dollar_currency = Entry(master=user_input, width=20)
label_currency = Label(master=user_input, text="$ Dollars")
new_label = Label(master=display, text="New Currency:")

dollar_currency.grid(row=0, column=0, sticky="e")
label_currency.grid(row=0, column=1, sticky="w")

conversion_button = Button(master=display, text="Convert", command=check_selected_currency)

answer_label = Label(master=display, text="")

'''organize the GUI'''
user_input.grid(row=0, column=0, padx=20)
conversion_button.grid(row=0, column=1, pady=20)
dropdown.grid(row=0, column=3, padx=20)
new_label.grid(row=0, column=4, padx=20)
answer_label.grid(row=1, column=4, padx=20)

'''button will close the GUI when clicked'''
button_exit = Button(display, text='Exit', width=25, command=display.destroy)
button_exit.grid(row=1, column=0, padx=20)

'''execute GUI'''
display.mainloop()


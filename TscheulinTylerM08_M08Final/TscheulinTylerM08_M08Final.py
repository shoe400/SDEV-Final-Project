# Tyler Tscheulin Date 2-15-22, SDEV 140 M08 Final Project
# This program will allow the user to input their/check their bank account.
# Version 0.1 2-19-22, Version 0.2 2-21-22, Version 0.3 2-23-22, Version 0.4 2-24-22, Version 0.5 2-28-22
# Version 0.6 3-1/2/3-22. Version 0.7 3-5-22, Version 0.8 3-7-22, Final Version 0.9 3-9-22
# Version 0.1 Setting up a function that will be called inside the program.
# Version 0.2 Setting up the window that will be used along with setting up a better function for buttons.
# Version 0.3 Setting up where it will display the amount and running balance.
# Version 0.4 Setting up font color for the types and checking to see if user has the amount in the bank.
# Version 0.5 Setting up Popup window and fixing The credit debit bug.
# Version 0.6 Setting up the size and lining up things, along with setting up the date when a button is pressed.
# Version 0.7 Setting up the date and getting it to run.
# Version 0.8 Setting up the pictures to work on the Popup Window. Along with the if statement
# Version 0.9 Setting up a pop-up window for the error when the user inputs too much in debit.
# Goal: Setting up GUI that acts like a virtual check book, There will be buttons that ask for the choice of
# the user to add or subtract money from their account.
# Along with printing the balance and what was done at the sametime.
# It will also look like a check book.

from tkinter import *
from datetime import date
from tkinter import messagebox

# Variables
red = (255, 0, 0)
green = (0, 255, 0)
balance = 0
today = date.today()  # date
d3 = today.strftime("%m/%d/%y")  # setting up what I want the date to be


def credit(enter_Amount_label_entry):  # the credit (adding money to account) function
    global balance
    credit = float(enter_Amount_label_entry.get())  # allowing the user to input a float
    balance = (balance + credit) # the equation for changing the balance
    display_type_label["text"] += str('Credit') + "\n"  # these are just showing where things are.
    display_amount_label["text"] += str('{:.2f}'.format(credit)) + "\n"
    display_balance_label["text"] += str('{:.2f}'.format(balance)) + "\n"
    display_date_label["text"] += d3 + "\n"

def debit(enter_Amount_label_entry):  # debit function removing money from the account
    global balance
    debit = float(enter_Amount_label_entry.get())
    if debit <= balance:  # if statement making sure that user has enough money in the account.
        balance = (balance - debit)
        display_type_label["text"] += str('Debit') + "\n"
        display_amount_label["text"] += str('{:.2f}'.format(debit)) + "\n"
        display_balance_label["text"] += str('{:.2f}'.format(balance)) + "\n"
        display_date_label["text"] += d3 + "\n"  # setting the date and showing it.
    else:
        messagebox.showerror("Error", "Not Enough Money in the Account!")  # small pop-up for errors


def open_popup():  # second window function
    window2 = Toplevel(window)
    window2.geometry("400x400")
    window2.title("Enter Amount")

    enter_Amount_Label = Label(window2, text="Enter Amount")  # pop up window
    enter_Amount_label_entry = Entry(window2)  # The amount the user will enter

    # buttons
    credit_button = Button(window2, image=p, command=lambda: credit(enter_Amount_label_entry)) #  the buttons with the commands
    debit_button = Button(window2, image=m, command=lambda: debit(enter_Amount_label_entry))

    # grid
    credit_button.grid(row=2, column=1) # showing where things go on the pop-up window.
    debit_button.grid(row=2, column=2)
    enter_Amount_Label.grid(row=0, column=0)
    enter_Amount_label_entry.grid(row=0, column=1)


def close(): # the exit button that is on the first page.
    window.quit()


# One to show a summary, and the other to do entering amounts.
window = Tk()
window.title("Check Book")  # Title of window
window.geometry("500x350")

# images being called in and ran from top window.
p = PhotoImage(file='Plus.gif')
m = PhotoImage(file='Minus.png')

# Labels
date_label = Label(window, text="Date", width=8)
type_label = Label(window, text="Type", width=8)
amount_label = Label(window, text="Amount", width=8)  # showing amount
balance_label = Label(window, text="Balance", width=8)  # showing the balance
display_type_label = Label(window)  # showing the type
display_amount_label = Label(window)  # showing the amount
display_balance_label = Label(window)  # showing the balance
display_date_label = Label(window)  # showing the date

# Four Buttons: One for Credit Function, Debit Function, Exit, and then Enter amount Popup window (On second screen)
enter_button = Button(window, text="Enter Amount", command=open_popup, width=10)
exit_button = Button(window, text="Exit", command=close, width=10)

# Showing where things are in the window
enter_button.grid(row=1, column=0)
exit_button.grid(row=1, column=10)
# Label Names of what goes here # These are being called from the pop-up window to the front/root window.
date_label.grid(row=3, column=1)
type_label.grid(row=3, column=2)
amount_label.grid(row=3, column=4)
balance_label.grid(row=3, column=6)


# Showing Credit or debit under typ
display_type_label.grid(row=4, column=2)

# the amounts
display_amount_label.grid(row=4, column=4)
display_balance_label.grid(row=4, column=6)
display_date_label.grid(row=4, column=1)

window.mainloop()

import customtkinter
from tkinter import *
from tkinter import messagebox
def convert(entry_of_amount,combobox_var,combobox_var2):
    test = entry_of_amount.get()
    test2 = 1
    if (test == ""):
        messagebox.showerror("Error", "Please Enter Currency Amount")
        test2 = 0

    currency_from_left = combobox_var.get()
    currency_from_right = combobox_var2.get()

    if(test2 == 1 & (currency_from_left == "Select Currency" or currency_from_right == "Select Currency") ):
        messagebox.showerror("Error", "Please Select Currency Properly")

    elif currency_from_left == "United States Dollar":
        entry_of_amount1 = float(entry_of_amount.get())
        entry_of_amount2 = round(entry_of_amount1, 2)
        if currency_from_right == "United States Dollar":
            messagebox.showinfo("Result" , f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2)} {currency_from_right}" )
        elif currency_from_right == "Euro":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.86)} {currency_from_right}")
        elif currency_from_right == "Japanese Yen":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 114.38)} {currency_from_right}")
        elif currency_from_right == "Pound Sterling":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.73)} {currency_from_right}")
        elif currency_from_right == "Australian Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 *1.35)} {currency_from_right}")
        elif currency_from_right == "Canadian Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1.24)} {currency_from_right}")
        elif currency_from_right == "Swiss Franc":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.92)} {currency_from_right}")
        elif currency_from_right == "Chinese Yuan":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 6.44)} {currency_from_right}")
        elif currency_from_right == "Hong Kong Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 7.78)} {currency_from_right}")
        elif currency_from_right == "New Zealand Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1.42)} {currency_from_right}")
        elif currency_from_right == "INR":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 81.5)} {currency_from_right}")

    elif currency_from_left == "Euro":
        entry_of_amount1 = float(entry_of_amount.get())
        entry_of_amount2 = round(entry_of_amount1, 2)
        if currency_from_right == "Euro":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1)} {currency_from_right}")
        elif currency_from_right == "United States Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1.16)} {currency_from_right}")
        elif currency_from_right == "Japanese Yen":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 132.54)} {currency_from_right}")
        elif currency_from_right == "Pound Sterling":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.84)} {currency_from_right}")
        elif currency_from_right == "Australian Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1.56)} {currency_from_right}")
        elif currency_from_right == "Canadian Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1.44)} {currency_from_right}")
        elif currency_from_right == "Swiss Franc":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1.07)} {currency_from_right}")
        elif currency_from_right == "Chinese Yuan":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 7.47)} {currency_from_right}")
        elif currency_from_right == "Hong Kong Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 9.02)} {currency_from_right}")
        elif currency_from_right == "New Zealand Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1.64)} {currency_from_right}")
        elif currency_from_right == "INR":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 88.1)} {currency_from_right}")

    elif currency_from_left == "Pound Sterling":
        entry_of_amount1 = float(entry_of_amount.get())
        entry_of_amount2 = round(entry_of_amount1, 2)
        if currency_from_right == "Pound Sterling":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1)} {currency_from_right}")
        elif currency_from_right == "United States Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1.37)} {currency_from_right}")
        elif currency_from_right == "Euro":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1.19)} {currency_from_right}")
        elif currency_from_right == "Japanese Yen":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 157.22)} {currency_from_right}")
        elif currency_from_right == "Australian Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1.85)} {currency_from_right}")
        elif currency_from_right == "Canadian Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1.70)} {currency_from_right}")
        elif currency_from_right == "Swiss Franc":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1.27)} {currency_from_right}")
        elif currency_from_right == "Chinese Yuan":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 8.85)} {currency_from_right}")
        elif currency_from_right == "Hong Kong Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 10.69)} {currency_from_right}")
        elif currency_from_right == "New Zealand Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1.94)} {currency_from_right}")
        elif currency_from_right == "INR":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 100.27)} {currency_from_right}")

    elif currency_from_left == "Japanese Yen":
        entry_of_amount1 = float(entry_of_amount.get())
        entry_of_amount2 = round(entry_of_amount1, 2)
        if currency_from_right == "Japanese Yen":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1)} {currency_from_right}")
        elif currency_from_right == "United States Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.0088)} {currency_from_right}")
        elif currency_from_right == "Euro":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.0075)} {currency_from_right}")
        elif currency_from_right == "Pound Sterling":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.0064)} {currency_from_right}")
        elif currency_from_right == "Australian Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.012)} {currency_from_right}")
        elif currency_from_right == "Canadian Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.011)} {currency_from_right}")
        elif currency_from_right == "Swiss Franc":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.0081)} {currency_from_right}")
        elif currency_from_right == "Chinese Yuan":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.056)} {currency_from_right}")
        elif currency_from_right == "Hong Kong Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.068)} {currency_from_right}")
        elif currency_from_right == "New Zealand Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.012)} {currency_from_right}")
        elif currency_from_right == "INR":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.62)} {currency_from_right}")

    elif currency_from_left == "Australian Dollar":
        entry_of_amount1 = float(entry_of_amount.get())
        entry_of_amount2 = round(entry_of_amount1, 2)
        if currency_from_right == "Australian Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1)} {currency_from_right}")
        elif currency_from_right == "United States Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.74)} {currency_from_right}")
        elif currency_from_right == "Euro":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.64)} {currency_from_right}")
        elif currency_from_right == "Pound Sterling":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.54)} {currency_from_right}")
        elif currency_from_right == "Japanese Yen":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 84.71)} {currency_from_right}")
        elif currency_from_right == "Canadian Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.92)} {currency_from_right}")
        elif currency_from_right == "Swiss Franc":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.68)} {currency_from_right}")
        elif currency_from_right == "Chinese Yuan":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 4.77)} {currency_from_right}")
        elif currency_from_right == "Hong Kong Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 5.77)} {currency_from_right}")
        elif currency_from_right == "New Zealand Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1.05)} {currency_from_right}")
        elif currency_from_right == "INR":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 56.64)} {currency_from_right}")

    elif currency_from_left == "Canadian Dollar":
        entry_of_amount1 = float(entry_of_amount.get())
        entry_of_amount2 = round(entry_of_amount1, 2)
        if currency_from_right == "Canadian Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1)} {currency_from_right}")
        elif currency_from_right == "United States Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.81)} {currency_from_right}")
        elif currency_from_right == "Euro":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.70)} {currency_from_right}")
        elif currency_from_right == "Pound Sterling":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.59)} {currency_from_right}")
        elif currency_from_right == "Australian Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1.09)} {currency_from_right}")
        elif currency_from_right == "Japanese Yen":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 92.34)} {currency_from_right}")
        elif currency_from_right == "Swiss Franc":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.75)} {currency_from_right}")
        elif currency_from_right == "Chinese Yuan":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 5.20)} {currency_from_right}")
        elif currency_from_right == "Hong Kong Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 6.29)} {currency_from_right}")
        elif currency_from_right == "New Zealand Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1.14)} {currency_from_right}")
        elif currency_from_right == "INR":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 61.23)} {currency_from_right}")

    elif currency_from_left == "Swiss Franc":
        entry_of_amount1 = float(entry_of_amount.get())
        entry_of_amount2 = round(entry_of_amount1, 2)
        if currency_from_right == "Swiss Franc":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1)} {currency_from_right}")
        elif currency_from_right == "United States Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1.08)} {currency_from_right}")
        elif currency_from_right == "Euro":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.93)} {currency_from_right}")
        elif currency_from_right == "Pound Sterling":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.79)} {currency_from_right}")
        elif currency_from_right == "Australian Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1.46)} {currency_from_right}")
        elif currency_from_right == "Canadian Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1.34)} {currency_from_right}")
        elif currency_from_right == "Japanese Yen":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 123.22)} {currency_from_right}")
        elif currency_from_right == "Chinese Yuan":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 6.97)} {currency_from_right}")
        elif currency_from_right == "Hong Kong Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 8.42)} {currency_from_right}")
        elif currency_from_right == "New Zealand Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1.53)} {currency_from_right}")
        elif currency_from_right == "INR":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 89.39)} {currency_from_right}")

    elif currency_from_left == "Chinese Yuan":
        entry_of_amount1 = float(entry_of_amount.get())
        entry_of_amount2 = round(entry_of_amount1, 2)
        if currency_from_right == "Chinese Yuan":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1)} {currency_from_right}")
        elif currency_from_right == "United States Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.16)} {currency_from_right}")
        elif currency_from_right == "Euro":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.13)} {currency_from_right}")
        elif currency_from_right == "Pound Sterling":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.11)} {currency_from_right}")
        elif currency_from_right == "Australian Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.21)} {currency_from_right}")
        elif currency_from_right == "Canadian Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.19)} {currency_from_right}")
        elif currency_from_right == "Swiss Franc":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.14)} {currency_from_right}")
        elif currency_from_right == "Japanese Yen":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 17.77)} {currency_from_right}")
        elif currency_from_right == "Hong Kong Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1.21)} {currency_from_right}")
        elif currency_from_right == "New Zealand Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.22)} {currency_from_right}")
        elif currency_from_right == "INR":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 12.03)} {currency_from_right}")

    elif currency_from_left == "Hong Kong Dollar":
        entry_of_amount1 = float(entry_of_amount.get())
        entry_of_amount2 = round(entry_of_amount1, 2)
        if currency_from_right == "Hong Kong Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1)} {currency_from_right}")
        elif currency_from_right == "United States Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.13)} {currency_from_right}")
        elif currency_from_right == "Euro":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.11)} {currency_from_right}")
        elif currency_from_right == "Pound Sterling":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.094)} {currency_from_right}")
        elif currency_from_right == "Australian Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.17)} {currency_from_right}")
        elif currency_from_right == "Canadian Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.16)} {currency_from_right}")
        elif currency_from_right == "Swiss Franc":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.12)} {currency_from_right}")
        elif currency_from_right == "Chinese Yuan":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.83)} {currency_from_right}")
        elif currency_from_right == "Japanese Yen":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 14.71)} {currency_from_right}")
        elif currency_from_right == "New Zealand Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.18)} {currency_from_right}")
        elif currency_from_right == "INR":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 10.56)} {currency_from_right}")

    elif currency_from_left == "New Zealand Dollar":
        entry_of_amount1 = float(entry_of_amount.get())
        entry_of_amount2 = round(entry_of_amount1, 2)
        if currency_from_right == "New Zealand Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1 )} {currency_from_right}")
        elif currency_from_right == "United States Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.71)} {currency_from_right}")
        elif currency_from_right == "Euro":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.61)} {currency_from_right}")
        elif currency_from_right == "Pound Sterling":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.51)} {currency_from_right}")
        elif currency_from_right == "Australian Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.95)} {currency_from_right}")
        elif currency_from_right == "Canadian Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.87)} {currency_from_right}")
        elif currency_from_right == "Swiss Franc":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.65)} {currency_from_right}")
        elif currency_from_right == "Chinese Yuan":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 4.54)} {currency_from_right}")
        elif currency_from_right == "Hong Kong Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 5.49)} {currency_from_right}")
        elif currency_from_right == "Japanese Yen":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 80.73)} {currency_from_right}")
        elif currency_from_right == "INR":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 51.5)} {currency_from_right}")

    elif currency_from_left == "INR":
        entry_of_amount1 = float(entry_of_amount.get())
        entry_of_amount2 = round(entry_of_amount1, 2)
        if currency_from_right == "INR":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1)} {currency_from_right}")
        elif currency_from_right == "United States Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.012)} {currency_from_right}")
        elif currency_from_right == "Euro":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.011)} {currency_from_right}")
        elif currency_from_right == "Pound Sterling":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.0100)} {currency_from_right}")
        elif currency_from_right == "Australian Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.018)} {currency_from_right}")
        elif currency_from_right == "Canadian Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.016)} {currency_from_right}")
        elif currency_from_right == "Swiss Franc":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.011)} {currency_from_right}")
        elif currency_from_right == "Chinese Yuan":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.083)} {currency_from_right}")
        elif currency_from_right == "Hong Kong Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.095)} {currency_from_right}")
        elif currency_from_right == "Japanese Yen":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 1.62)} {currency_from_right}")
        elif currency_from_right == "New Zealand Dollar":
            messagebox.showinfo("Result",f"{entry_of_amount2} {currency_from_left} will be {(entry_of_amount2 * 0.019)} {currency_from_right}")

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")
app = customtkinter.CTk()
app.geometry("800x400")
app.title("Currency Converter")
app.config(padx=20,pady=20)
app.resizable(False, False)

text = customtkinter.CTkLabel(app, text="Currency Converter",font=('Century Gothic',25))
text.place(relx=0.35, rely=0.15)
entry_of_amount = customtkinter.CTkEntry(master=app,corner_radius=10)
entry_of_amount.place(relx=0.40, rely=0.36, relheight=0.06, relwidth=0.21)

combo_list = ["United States Dollar","INR","Euro","Japanese Yen","Pound Sterling","Australian Dollar","Canadian Dollar","Swiss Franc","Chinese Yuan","Hong Kong Dollar","New Zealand Dollar"]
combobox_var = StringVar(value="Select Currency")
status_combobox = customtkinter.CTkComboBox(app,variable=combobox_var ,values=combo_list,state="readonly",font=("Century Gothic",14),dropdown_hover_color="green",dropdown_font=("Century Gothic",14),width = 220)
status_combobox.place(relx=0.17, rely=0.55, relheight=0.06, relwidth=0.23)

combo_list2 = ["United States Dollar","INR","Euro","Japanese Yen","Pound Sterling","Australian Dollar","Canadian Dollar","Swiss Franc","Chinese Yuan","Hong Kong Dollar","New Zealand Dollar"]
combobox_var2 = StringVar(value="Select Currency")
status_combobox2 = customtkinter.CTkComboBox(app,variable=combobox_var2 ,values=combo_list,state="readonly",font=("Century Gothic",14),dropdown_hover_color="green",dropdown_font=("Century Gothic",14),width = 220)
status_combobox2.place(relx=0.62, rely=0.55, relheight=0.06, relwidth=0.23)

convert_button = customtkinter.CTkButton(master=app,text="Convert",command=lambda : convert(entry_of_amount,combobox_var,combobox_var2))
convert_button.place(relx=0.40, rely=0.76, relheight=0.06, relwidth=0.21)

app.mainloop()
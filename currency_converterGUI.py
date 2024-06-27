import tkinter as tk
from tkinter import ttk, messagebox
from exchange_rates import exchange_rates

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()

        if from_currency not in exchange_rates or to_currency not in exchange_rates:
            raise ValueError("Invalid currency")

        converted_amount = (amount / exchange_rates[from_currency]) * exchange_rates[to_currency]
        result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# Initialize the main window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("500x500")

# Amount entry
amount_label = ttk.Label(root, text="Amount:")
amount_label.grid(row=0, column=0, padx=20, pady=20)
amount_entry = ttk.Entry(root)
amount_entry.grid(row=0, column=1, padx=20, pady=20)

# From currency dropdown
from_currency_var = tk.StringVar()
from_currency_label = ttk.Label(root, text="From:")
from_currency_label.grid(row=1, column=0, padx=20, pady=20)
from_currency_menu = ttk.Combobox(root, textvariable=from_currency_var, values=list(exchange_rates.keys()))
from_currency_menu.grid(row=1, column=1, padx=20, pady=20)
from_currency_menu.current(0)  # Set default value

# To currency dropdown
to_currency_var = tk.StringVar()
to_currency_label = ttk.Label(root, text="To:")
to_currency_label.grid(row=2, column=0, padx=20, pady=20)
to_currency_menu = ttk.Combobox(root, textvariable=to_currency_var, values=list(exchange_rates.keys()))
to_currency_menu.grid(row=2, column=1, padx=20, pady=20)
to_currency_menu.current(1)  # Set default value

# Convert button
convert_button = ttk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, padx=50, pady=50)

# Result label
result_label = ttk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=50, pady=50)

# Start the main event loop
root.mainloop()
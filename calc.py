import tkinter as tk
from math import factorial

# Function to handle button click events
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

# Function to clear the entry field
def button_clear():
    entry.delete(0, tk.END)

# Function to calculate the result
def button_equal():
    expression = entry.get()
    if "%" in expression:
        expression = expression.replace("%", "/100")
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to calculate factorial
def factorial_calc():
    num = int(entry.get())
    try:
        result = factorial(num)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        

# Function to calculate percentage
def percentage_calc():
    expression = entry.get()
    try:
        result = eval(expression) / 100
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Modern Calculator")
root.configure(bg='black')

# Entry field for displaying input and results
entry = tk.Entry(root, width=30, font=("Helvetica", 14), bg='#ef5e0f', fg='black')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# List of buttons with their text, row, and column positions
buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    ("0", 4, 0),
    (".", 4, 1),
    ("+", 4, 2),
    ("!", 4, 3),
    ("%", 5, 0)
]

# Create buttons and place them in the grid
for button_text, row, column in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=10, font=("Helvetica", 12), bg='#ef5e0f', fg='white', command=lambda text=button_text: button_click(text))
    button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")

# Additional buttons
clear_button = tk.Button(root, text="C", padx=20, pady=10, font=("Helvetica", 12), bg='#ef5e0f', fg='white', command=button_clear)
clear_button.grid(row=5, column=1, columnspan=2, padx=5, pady=5, sticky="nsew")

equal_button = tk.Button(root, text="=", padx=20, pady=10, font=("Helvetica", 12), bg='#ef5e0f', fg='white', command=button_equal)
equal_button.grid(row=5, column=3, padx=5, pady=5, sticky="nsew")

factorial_button = tk.Button(root, text="!", padx=20, pady=10, font=("Helvetica", 12), bg='#ef5e0f', fg='white', command=factorial_calc)
factorial_button.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

percentage_button = tk.Button(root, text="%", padx=20, pady=10, font=("Helvetica", 12), bg='#ef5e0f', fg='white', command=percentage_calc)
percentage_button.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

# Configure resizing behavior
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Start the main event loop
root.mainloop()

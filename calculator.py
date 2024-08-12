import tkinter as tk

# Function to update the expression in the entry box
def press(key):
    current_expression = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_expression + key)

# Function to evaluate the expression in the entry box
def equal_press():
    try:
        current_expression = entry.get()
        result = str(eval(current_expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry box
def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry box
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Define the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create and place the buttons
row_val = 1
col_val = 0
for button in buttons:
    if button == "=":
        tk.Button(root, text=button, width=10, height=3, font=('Arial', 18), command=equal_press).grid(row=row_val, column=col_val, columnspan=2)
        col_val += 2
    else:
        tk.Button(root, text=button, width=5, height=3, font=('Arial', 18), command=lambda key=button: press(key)).grid(row=row_val, column=col_val)
        col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create and place the Clear button
tk.Button(root, text='C', width=10, height=3, font=('Arial', 18), command=clear).grid(row=row_val, column=0, columnspan=2)

# Run the application
root.mainloop()

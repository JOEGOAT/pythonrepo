import tkinter as tk
from tkinter import ttk

# Create the main window.
window = tk.Tk()
window.title("Scientific Calculator")

# Create the display.
display = ttk.Entry(window, width=30)
display.grid(row=0, column=0, columnspan=4)

# Create the buttons.
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+"),
]

for row, row_buttons in enumerate(buttons):
    for column, button_text in enumerate(row_buttons):
        button = ttk.Button(window, text=button_text)
        button.grid(row=row+1, column=column)

# Define the button click handler.
def button_click(button_text):
    if button_text == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(0, result)
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")
    elif button_text == ".":
        if "." not in display.get():
            display.insert(tk.END, button_text)
    else:
        display.insert(tk.END, button_text)

# Bind the button click handler to the buttons.
for button in buttons:
    for button_text in button:
        button =buttons(command=lambda button_text=button: button_click(button_text))

# Run the main loop.
window.mainloop()

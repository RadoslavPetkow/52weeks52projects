import tkinter as tk

symbols_list = []


def on_click(button_text):
    global symbols_list
    current_text = entry.get()

    if button_text == "=":
        try:
            if "%" in symbols_list:
                for i, symbol in enumerate(symbols_list):
                    if symbol == "%":
                        symbols_list[i] = "/100*"

                modified_expression = "".join(symbols_list)
                result = eval(modified_expression)
            else:
                result = eval(current_text)

            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
            symbols_list = ["="]
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
            symbols_list = []
    elif button_text == "C":
        entry.delete(0, tk.END)
        symbols_list = []
    elif button_text == "%":
        entry.insert(tk.END, "%")
        symbols_list.append("%")
    else:
        entry.insert(tk.END, button_text)
        symbols_list.append(button_text)


root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=16, font=('Arial', 20), justify='right')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C', '%', '(', ')'
]

row_val = 1
col_val = 0

button_width = 5
button_height = 2

for button in buttons:
    tk.Button(root, text=button, width=button_width, height=button_height, font=('Arial', 14), command=lambda btn=button: on_click(btn)).grid(
        row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()

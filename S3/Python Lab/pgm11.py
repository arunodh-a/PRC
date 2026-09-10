import tkinter as tk

def click(key):
    if key == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif key == "C":
        entry.delete(0, tk.END)

    else:
        entry.insert(tk.END, key)


root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    "789/",
    "456*",
    "123-",
    "C0+="
]

row_num = 1

for row_string in buttons:
    col_num = 0

    for char in row_string:
        btn = tk.Button(
            root,
            text=char,
            width=5,
            height=2,
            command=lambda ch=char: click(ch)
        )

        btn.grid(row=row_num, column=col_num)

        col_num += 1

    row_num += 1

root.mainloop()
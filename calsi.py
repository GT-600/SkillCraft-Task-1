import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Smart Calculator")
root.geometry("340x460")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

style = ttk.Style()
style.configure("TButton",
                font=("Arial", 14, "bold"),
                padding=10)
style.map("TButton",
          background=[("active", "#3a3a3a")],
          foreground=[("active", "white")])

entry = tk.Entry(root, font=("Consolas", 22), borderwidth=0,
                 relief="flat", justify="right", bg="#2d2d2d", fg="white")
entry.place(x=10, y=20, width=320, height=60)

frame = tk.Frame(root, bg="#2d2d2d")
frame.place(x=10, y=100, width=320, height=340)

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Division by zero is not allowed.")
        entry.delete(0, tk.END)
    except Exception:
        messagebox.showerror("Error", "Invalid Input")
        entry.delete(0, tk.END)

def on_key(event):
    key = event.char
    if key in "0123456789+-*/.()":
        entry.insert(tk.END, key)
    elif key == "\r": 
        calculate()
    elif key == "\x08": 
        backspace()

root.bind("<Key>", on_key)

buttons = [
    ("C", 1, 0, "#ff4d4d"), ("←", 1, 1, "#ff9933"), ("/", 1, 2, "#ff9933"), ("*", 1, 3, "#ff9933"),
    ("7", 2, 0, "#4d4d4d"), ("8", 2, 1, "#4d4d4d"), ("9", 2, 2, "#4d4d4d"), ("-", 2, 3, "#ff9933"),
    ("4", 3, 0, "#4d4d4d"), ("5", 3, 1, "#4d4d4d"), ("6", 3, 2, "#4d4d4d"), ("+", 3, 3, "#ff9933"),
    ("1", 4, 0, "#4d4d4d"), ("2", 4, 1, "#4d4d4d"), ("3", 4, 2, "#4d4d4d"), ("=", 4, 3, "#00cc66"),
    ("0", 5, 0, "#4d4d4d"), (".", 5, 1, "#4d4d4d"), ("(", 5, 2, "#4d4d4d"), (")", 5, 3, "#4d4d4d")
]

for (text, row, col, color) in buttons:
    action = lambda t=text: click(t)
    if text == "C":
        action = clear
    elif text == "=":
        action = calculate
    elif text == "←":
        action = backspace

    btn = tk.Button(frame, text=text, command=action, fg="white",
                    bg=color, font=("Arial", 14, "bold"),
                    borderwidth=0, activebackground="#666666", relief="flat")
    btn.grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

for i in range(6):
    frame.rowconfigure(i, weight=1)
for j in range(4):
    frame.columnconfigure(j, weight=1)

root.mainloop()

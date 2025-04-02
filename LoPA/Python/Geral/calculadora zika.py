import tkinter as tk
from tkinter import Entry, Button

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = entry_var.get().replace("x", "*")  # Substituir 'x' por '*'
            result = eval(expression)
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Erro")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

# Criando a janela
root = tk.Tk()
root.title("Calculadora")
root.geometry("300x400")
root.configure(bg="#2c3e50")  # Fundo da janela

title_label = tk.Label(root, text="Calculadora", font="Arial 16 bold", bg="#2c3e50", fg="white")
title_label.pack()

entry_var = tk.StringVar()
entry = Entry(root, textvariable=entry_var, font="Arial 20", justify='right', bd=10, relief=tk.GROOVE, bg="#ecf0f1")
entry.pack(fill=tk.BOTH, padx=10, pady=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "x"],  # Alterado de '*' para 'x' para melhor visualização
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

frame = tk.Frame(root, bg="#2c3e50")
frame.pack()

button_colors = {"C": "#e74c3c", "=": "#27ae60", "+": "#f39c12", "-": "#f39c12", "x": "#f39c12", "/": "#f39c12"}

def get_button_color(text):
    return button_colors.get(text, "#bdc3c7")  # Cor padrão

for row in buttons:
    row_frame = tk.Frame(frame, bg="#2c3e50")
    row_frame.pack()
    for btn_text in row:
        btn = Button(row_frame, text=btn_text, font="Arial 15", height=2, width=5, bg=get_button_color(btn_text), fg="black")
        btn.pack(side=tk.LEFT, padx=5, pady=5)
        btn.bind("<Button-1>", on_click)

root.mainloop()

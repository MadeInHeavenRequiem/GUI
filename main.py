import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Приветствие", "Добро пожаловать в мою программу!")

def on_checkbox_click():
    if checkbox_var.get():
        checkbox_label.config(text="Флажок установлен")
    else:
        checkbox_label.config(text="Флажок сброшен")

# Создаем главное окно
root = tk.Tk()
root.title("Пример программы с GUI")

# Метка
label = tk.Label(root, text="Пример программы с GUI", padx=20, pady=20)
label.pack()

# Кнопка
button = tk.Button(root, text="Показать сообщение", command=show_message)
button.pack()

# Текстовое поле
entry = tk.Entry(root, width=30)
entry.pack()

# Флажок
checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text="Флажок", variable=checkbox_var, command=on_checkbox_click)
checkbox.pack()
checkbox_label = tk.Label(root, text="")
checkbox_label.pack()

# Радиокнопки
radio_var = tk.StringVar()
radio_var.set("1")
radio1 = tk.Radiobutton(root, text="Вариант 1", variable=radio_var, value="1")
radio2 = tk.Radiobutton(root, text="Вариант 2", variable=radio_var, value="2")
radio1.pack()
radio2.pack()

# Выпадающий список
options = ["Опция 1", "Опция 2", "Опция 3"]
option_var = tk.StringVar()
option_var.set(options[0])
option_menu = tk.OptionMenu(root, option_var, *options)
option_menu.pack()

# Текстовое поле для вывода
output_text = tk.Text(root, height=10, width=40)
output_text.pack()


# Запускаем цикл обработки событий
root.mainloop()

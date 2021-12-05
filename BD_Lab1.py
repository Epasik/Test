# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 12:08:37 2021

@author: Егор
"""

import redis
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

client = redis.Redis(host="192.168.112.103", password="student")

items = {"kay1": "вапр", 
         
        "вампр": "вапр"}

window = tk.Tk()
window.title("New window")
global myfont
global myfg


def pr(event):
    label7["text"] = text5message.get()


def dl():
    label7["text"] = ""


def user_settings(argument):
    user = list_of_users.get()

    text1_font = client.get("22306-Revin-" + user + "-text1")
    text2_size = client.get("22306-Revin-" + user + "-text2")
    text3_color = client.get("22306-Revin-" + user + "-text3")
    text4_type = client.get("22306-Revin-" + user + "-text4")

    text1.delete(0, "end")
    text1.insert(0, text1_font)

    text2.delete(0, "end")
    text2.insert(0, text2_size)

    text3.delete(0, "end")
    text3.insert(0, text3_color)

    text4.delete(0, "end")
    text4.insert(0, text4_type)

    label7.config(
        text=text5message.get(),
        font=(text1message.get() + " " + text2message.get() + " " + text4message.get()),
        fg=(text3message.get()),
    )


# Функция сохранения введённых настроек
def save():
    text1_font = text1.get()
    text2_size = text2.get()
    text3_color = text3.get()
    text4_type = text4.get()
    user = list_of_users.get()

    # Добавляем в БД
    client.set("22306-Revin-" + user + "-text1", text1_font)
    client.set("22306-Revin-" + user + "-text2", text2_size)
    client.set("22306-Revin-" + user + "-text3", text3_color)
    client.set("22306-Revin-" + user + "-text4", text4_type)


text1message = StringVar()
text1 = tk.Entry(window, width=10, textvariable=text1message)
text1.grid(column=2, row=2)
label1 = tk.Label(text="Название шрифта")
label1.grid(column=1, row=2)

text2message = StringVar()
text2 = tk.Entry(window, width=10, textvariable=text2message)
text2.grid(column=2, row=3)
label2 = tk.Label(text="Размер шрифта")
label2.grid(column=1, row=3)

text3message = StringVar()
text3 = tk.Entry(window, width=10, textvariable=text3message)
text3.grid(column=2, row=4)
label3 = tk.Label(text="Цвет шрифта")
label3.grid(column=1, row=4)

text4message = StringVar()
text4 = tk.Entry(window, width=10, textvariable=text4message)
text4.grid(column=2, row=5)
label4 = tk.Label(text="Начертание")
label4.grid(column=1, row=5)

text5message = StringVar()
text5 = tk.Entry(window, width=15, textvariable=text5message)
text5.grid(column=2, row=8)
text5.bind("<Enter>", pr)
label5 = tk.Label(text="Введите текст")
label5.grid(column=1, row=8)

label6 = tk.Label(text="Отформатированный текст:")
label6.grid(column=1, row=9)

label7 = tk.Label(text="")
label7.grid(column=2, row=9)

button1 = tk.Button(
    window,
    text="Сохранить",
    font="Arial 8",
    command=save,
    padx="10",  # отступ от границ до содержимого по горизонтали
    pady="10",  # отступ от границ до содержимого по вертикал
    height="1",
    width="18",
)
button1.grid(column=1, row=6)

# button1= tk.Button(window, text = "Применить", font = "Arial 8", command = pr,
# padx="10", # отступ от границ до содержимого по горизонтали
# pady="10", # отступ от границ до содержимого по вертикал
# height = "1",
# width = "18")
# button1.grid(column = 1, row = 7)


button2 = tk.Button(
    window,
    text="Очистить",
    font="Arial 8",
    command=dl,
    padx="10",  # отступ от границ до содержимого по горизонтали
    pady="10",  # отступ от границ до содержимого по вертикал
    height="1",
    width="18",
)
button2.grid(column=2, row=6)

label_users = tk.Label(window, text="Выберите пользователя")
label_users.grid(row=10, column=1)
list_of_users = ttk.Combobox(window, values=["User1", "User2", "User3"])
list_of_users.grid(row=10, column=2)
list_of_users.bind("<<ComboboxSelected>>", user_settings)
client.close()
window.mainloop()

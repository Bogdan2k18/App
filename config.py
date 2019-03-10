from tkinter import messagebox

def error(mess):
    messagebox.showerror("Упс", mess)

def info(mess):
    messagebox.showinfo("Все ок!", mess)


class User_config:
    bot_token = ""

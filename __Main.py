from tkinter import *
from telegram_bot import *
from config import User_config
win = Tk()
#   Constatnts
SW = win.winfo_screenwidth()
SH = win.winfo_screenheight()

def connect_bot(win):
    root = Toplevel(win)
    root.title("Connect")
    root.geometry("400x300")
    root.resizable(0, 0)
    root["bg"] = '#eaf7a3'
    root.grab_set()
    root.focus_set()
    Label(root, text="Задайте название и токен телеграм-бота").pack(padx=10,pady=10)
    Label(root, text="Название").pack(padx=10,pady=10)
    name = Entry(root, width=20)
    name.pack(padx=10, pady=10)
    Label(root, text="Токен").pack(padx=10,pady=10)
    token = Entry(root, width=100)
    token.pack(padx=10, pady=10)
    Button(root, text='Подтвердить', command = lambda token=token, name=name: bot_init(token, name)).pack(padx=10,pady=10)
    
    root.wait_window()

def choose_bot(win):
    root = Toplevel(win)
    root.title("Choose")
    root.geometry("400x300")
    root.resizable(0, 0)
    root["bg"] = '#eaf7a3'
    root.grab_set()
    root.focus_set()
    Label(root, text="Выберите бота имя из списка").pack(padx=10,pady=10)
    box = Listbox(root, selectmode=EXTENDED)
    box.pack()
    for e, value in BOTS_.items():
        box.insert(END, e)
    Button(root, text='Подтвердить', command = lambda name=box.get(box.curselection()): choose(name)).pack(padx=10,pady=10)
    root.wait_window()



if __name__ == "__main__":
    
    User = User_config()

    #   Config
    win.title("APP BOT SYSTEM")
    win.geometry("700x400")
    win.resizable(0, 0)
    win["bg"] = '#eaf7a3'

    Label(win, text="Подключите телеграм-бота").grid(column=0, row=0, padx=10,pady=10)
    Button(win, text='Добавить', command = lambda win=win: connect_bot(win)).grid(column=0, row=1, padx=10,pady=10)
    Button(win, text='Выбрать', command = lambda win=win: choose_bot(win)).grid(column=0, row=2, padx=10,pady=10)
    Button(win, text='Проверить связь').grid(column=0, row=3, padx=10,pady=10)


    Label(win, text="Выберите сайт для парсинга").grid(column=1, row=0, padx=10,pady=10)
    Button(win, text='Выбрать сайт').grid(column=1, row=1, padx=10,pady=10)
    Listbox(win).grid(column=1, row=2, rowspan=10)


    Label(win, text="Добавте команду боту").grid(column=2, row=0, padx=10,pady=10)
    Button(win, text='Добавить').grid(column=2, row=1, padx=10,pady=10)




    win.mainloop()





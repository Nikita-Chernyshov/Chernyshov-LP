import tkinter as tk
from tkinter import *
from tkinter import messagebox
import json

def write():
    if rep.get() == "Nixpkgs":
        with open("data.txt",'w',encoding='utf-8') as file:
            json.dump(dat,file,indent=4)
        messagebox.showinfo('Save', 'Файл сохранён как data')
    else:
        messagebox.showerror('Error', 'Репозиторий не найден')

infa="""
{
"company": null,
"created_at": "2015-02-09T13:45:22Z",
"email": null,
"id": 1214096158,
"name": "NixOS nixpkgs",
"url": "https://github.com/NixOS/nixpkgs"
}"""
dat = json.loads(infa)
win = Tk()
win.geometry("600x300")
win['bg'] ='#005000'
win.title('Чернышов Никита')
rep = StringVar()
lbl = Label(win, text="Введите название репозитория",bg="#005000",fg='#008000')
lbl.grid(column=300, row=300)
lbl.place(x=300, y=60,width=200, height=200,anchor=CENTER)
vvod = Entry(win,textvariable=rep)
vvod.place(x=200, y=100, width=210, height=20)
Enter = Button(win,text = 'Ввод',bg='#009000',fg='#001000',activebackground='#013220',
          activeforeground='#008000',command=write)
Enter.place(x=400, y=100, width=50, height=21)

win.mainloop()
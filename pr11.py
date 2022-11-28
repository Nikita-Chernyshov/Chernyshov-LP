from tkinter import*

def mycom():
    e = edit.get()
    if e == 'Apache Spark':
        f = open(data.json, 'r')
    f.read()


window = Tk()
window.title("Чернышов Никита")
window.geometry('650x150')

t1 = Label(window, text='Введите название репозитория:', fg='black')
t1.config(font=('Colibry', 24))
t1.pack()

edit = Entry(window, width = 60, bg = 'grey')
edit.pack()

but = Button(window, text='Продолжить', command = mycom)
but.pack()

window.mainloop()

import json
from pprint import pprint
def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding = 'utf-8') as file:
        json.dump(data, file, indent = 4)

n_data = {
'company': None,
'created_at': '2015-02-09T13:45:22Z',
'email': None,
'id': 1214096158,
'name':'Nixpkgs',
'url':'https://github.com/NixOS/nixpkgs'
}
write(n_data, 'data.json')
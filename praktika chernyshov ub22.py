from tkinter import *
import os
import random
 
def generator_parolya():
    chars = 'abcdefghijklnopqrstuvwxyz1234567890'
    number = 1
    length = 8
    number = int(number)
    length = int(length)
    for n in range(number):
        password =''
        for i in range(length):
            password += random.choice(chars)
        r = Tk()
        r.clipboard_append(password)
        r.title("")
        r.geometry("200x180")

        Label(r, text="").pack()
        Label(r, text="").pack()
        Label(r,text="Your password is:").pack()
        Label(r,text=password, font='38').pack()
    
        r.mainloop()
        
        print(password)
    
# Designing window for password generate 

def generate():
    global generate_screen
    generate_screen = Toplevel(main_screen)
    generate_screen.title("Generate password")
    generate_screen.geometry("420x250")

    global generate_password
    global generate_entry 
    generate_password = StringVar()
    
    Label(generate_screen,text="Please click the button below").pack()
    Label(generate_screen, text="").pack()
    generate_lable = Label(generate_screen, text="Generate new password (The new password will be copied to the clipboard)")
    generate_lable.pack()
    generate_entry = Entry(generate_screen, textvariable=generate_password)
    Label(generate_screen, text="").pack()
    Button(generate_screen, text="Generate", width=10, height=1, bg="white", command = generator_parolya).pack()    

def rem():

    r = Tk()
    r.clipboard_append(password_info)
    r.title("")
    r.geometry("200x180")

    Label(r, text="").pack()
    Label(r, text="").pack()
    Label(r,text="Your password is:").pack()
    Label(r,text=password_info, font='38').pack()
    
    r.mainloop()
    
    print(password_info)
    
#Designing window for remind password
def remind():   
    
    global remind_screen
    remind_screen = Toplevel(main_screen)
    remind_screen.title("Remind password")
    remind_screen.geometry("300x250")

    global remind_password
    global remind_password_entry
    remind_password = StringVar()
    
    Label(remind_screen, text = "Please enter your name below", bg="white").pack()
    Label(remind_screen, text="").pack()
    remind_lable = Label(remind_screen, text="Your name is...")
    remind_lable.pack()
    remind_password_entry = Entry(remind_screen, textvariable=remind_password)
    remind_password_entry.pack()
    Label(remind_screen, text = "").pack()
    Button(remind_screen, text="Remind password" ,width=15, height=1, bg="white", command = rem).pack()

# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="white").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="white", command = register_user).pack()
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()

# Implementing event on register button
 
def register_user():
 
    global password_info
    global itog
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    
    alfavit_EU =  'abcdefghijklnopqrstuvwxyz1234567890'
    smeshenie = 1
    message = password_info.lower()
    itog = ''

    for i in message:
        mesto = alfavit_EU.find(i)
        new_mesto = mesto + smeshenie
        if i in alfavit_EU:
            itog += alfavit_EU[new_mesto]
        else:
            itog += i

    print (itog)

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    print(username_info)
    
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x350")
    main_screen.title("Чернышов Никита")
    Label(text="Select Your Choice", bg="white", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
    Label(text="").pack()
    Button(text="Generate", height="2", width="30", command=generate).pack()
    Label(text="").pack()
    Button(text="Remind password", height="2", width="30", command=remind).pack()
 
    main_screen.mainloop()
 
main_account_screen()
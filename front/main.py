from tkinter import *
import requests
import json


tk = Tk()  
API_ENDPOINT = "http://127.0.0.1:8000"

head = {'Content-Type' : 'application/x-www-form-urlencoded'}

def on_click():
    payload = {"username":username.get(),"password":password.get()}
    response = requests.post(API_ENDPOINT+"/token", payload, headers = head)
    


tk.geometry('800x600')  
tk.title('Tkinter Login Form - pythonexamples.org')

#username label and text entry box
usernameLabel = Label(tk, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tk, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tk,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tk, textvariable=password, show='*').grid(row=1, column=1)  

loginButton = Button(tk, text="Login", command = on_click).grid(row=4, column=0)  

tk.mainloop()
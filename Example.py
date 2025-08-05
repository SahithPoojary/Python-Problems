# import numpy as np
# a=np.array([3,3,3])
# b=np.array([4,5,6])
# print(a+b)
# print(a*b)
# print(a ** 2)
# print(np.dot(a,b))
# print(a.sum())
# a.max()
# a.min()
# print(a.mean())
# print(a.std())


import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

def receive():
    while True:
        try:
            msg = client_socket.recv(1024).decode("utf-8")
            chat_area.config(state='normal')
            chat_area.insert(tk.END, "Friend: " + msg + "\n")
            chat_area.config(state='disabled')
        except:
            break

def send():
    msg = msg_entry.get()
    msg_entry.delete(0, tk.END)
    client_socket.send(msg.encode("utf-8"))
    chat_area.config(state='normal')
    chat_area.insert(tk.END, "You: " + msg + "\n")
    chat_area.config(state='disabled')

win = tk.Tk()
win.title("Client Chat")

chat_area = scrolledtext.ScrolledText(win, state='disabled', width=50, height=20)
chat_area.pack()

msg_entry = tk.Entry(win, width=40)
msg_entry.pack(side=tk.LEFT)

send_btn = tk.Button(win, text="Send", command=send)
send_btn.pack(side=tk.RIGHT)


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("10.166.153.23", 9999))
print("Connected to server")

threading.Thread(target=receive).start()
win.mainloop()
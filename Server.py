import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

def receive():
    while True:
        try:
            msg = client_socket.recv(1024).decode("utf-8")
            chat_area.config(state='normal')
            chat_area.insert(tk.END, "Friend: " + msg + "\n")
            chat_area.config(state='disabled')
            chat_area.see(tk.END)
        except:
            messagebox.showerror("Error", "Disconnected from server.")
            break

def send():
    msg = msg_entry.get()
    if msg:
        msg_entry.delete(0, tk.END)
        client_socket.send(msg.encode("utf-8"))
        chat_area.config(state='normal')
        chat_area.insert(tk.END, "You: " + msg + "\n")
        chat_area.config(state='disabled')
        chat_area.see(tk.END)

win = tk.Tk()
win.title("Client Chat")
win.geometry("400x400")

chat_area = scrolledtext.ScrolledText(win, state='disabled', width=50, height=20)
chat_area.pack(pady=10)

msg_entry = tk.Entry(win, width=30)
msg_entry.pack(side=tk.LEFT, padx=5)

send_btn = tk.Button(win, text="Send", command=send)
send_btn.pack(side=tk.RIGHT, padx=5)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect(("10.166.153.23", 9999))
    threading.Thread(target=receive, daemon=True).start()
except ConnectionRefusedError:
    messagebox.showerror("Connection Error", "Could not connect to server.")
    win.destroy()

win.mainloop()

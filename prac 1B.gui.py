import tkinter as tk
from tkinter import messagebox


# ---------------- Rail Fence Encryption ----------------

def encrypt(text, key):
    rail = ['' for _ in range(key)]

    row = 0
    direction = 1

    for ch in text:
        rail[row] += ch
        row += direction

        if row == 0 or row == key - 1:
            direction *= -1

    return ''.join(rail)


# ---------------- Rail Fence Decryption ----------------

def decrypt(cipher, key):
    pattern = [['' for _ in range(len(cipher))] for _ in range(key)]

    row = 0
    direction = 1

    # Mark the zig-zag pattern
    for col in range(len(cipher)):
        pattern[row][col] = '*'
        row += direction

        if row == 0 or row == key - 1:
            direction *= -1

    # Fill the pattern
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if pattern[i][j] == '*':
                pattern[i][j] = cipher[index]
                index += 1

    # Read plaintext
    result = ""
    row = 0
    direction = 1

    for col in range(len(cipher)):
        result += pattern[row][col]
        row += direction

        if row == 0 or row == key - 1:
            direction *= -1

    return result


# ---------------- GUI Functions ----------------

def encrypt_message():
    try:
        text = message_entry.get()
        key = int(key_entry.get())

        if key < 2:
            messagebox.showerror("Error", "Rails must be at least 2")
            return

        result = encrypt(text, key)
        output_label.config(text="Encrypted: " + result)

    except:
        messagebox.showerror("Error", "Enter a valid number of rails")


def decrypt_message():
    try:
        text = message_entry.get()
        key = int(key_entry.get())

        if key < 2:
            messagebox.showerror("Error", "Rails must be at least 2")
            return

        result = decrypt(text, key)
        output_label.config(text="Decrypted: " + result)

    except:
        messagebox.showerror("Error", "Enter a valid number of rails")


# ---------------- Main Window ----------------

root = tk.Tk()
root.title("Rail Fence Cipher")
root.geometry("450x320")
root.resizable(False, False)

title = tk.Label(root, text="Rail Fence Cipher", font=("Arial", 16, "bold"))
title.pack(pady=10)

tk.Label(root, text="Enter Message").pack()

message_entry = tk.Entry(root, width=45)
message_entry.pack(pady=5)

tk.Label(root, text="Enter Number of Rails").pack()

key_entry = tk.Entry(root, width=10)
key_entry.pack(pady=5)

encrypt_btn = tk.Button(root, text="Encrypt", width=15, command=encrypt_message)
encrypt_btn.pack(pady=5)

decrypt_btn = tk.Button(root, text="Decrypt", width=15, command=decrypt_message)
decrypt_btn.pack(pady=5)

output_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
output_label.pack(pady=20)

root.mainloop()

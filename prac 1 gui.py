import tkinter as tk
from tkinter import ttk, messagebox

# ---------------- Caesar Cipher ----------------
def caesar_encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            start = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch)-start+shift)%26+start)
        else:
            result += ch
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# ---------------- Playfair Cipher ----------------
def generate_table(key):
    key = key.upper().replace("J","I")
    table=[]
    used=set()

    for ch in key:
        if ch.isalpha() and ch not in used:
            table.append(ch)
            used.add(ch)

    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in used:
            table.append(ch)

    return [table[i:i+5] for i in range(0,25,5)]

def find(table,ch):
    for i in range(5):
        for j in range(5):
            if table[i][j]==ch:
                return i,j

def prepare(text):
    text=text.upper().replace("J","I")
    text=''.join(c for c in text if c.isalpha())

    result=""
    i=0

    while i<len(text):
        a=text[i]

        if i+1<len(text):
            b=text[i+1]
            if a==b:
                result+=a+"X"
                i+=1
            else:
                result+=a+b
                i+=2
        else:
            result+=a+"X"
            i+=1

    return result

def playfair_encrypt(text,key):
    table=generate_table(key)
    text=prepare(text)
    cipher=""

    for i in range(0,len(text),2):
        a,b=text[i],text[i+1]
        r1,c1=find(table,a)
        r2,c2=find(table,b)

        if r1==r2:
            cipher+=table[r1][(c1+1)%5]
            cipher+=table[r2][(c2+1)%5]

        elif c1==c2:
            cipher+=table[(r1+1)%5][c1]
            cipher+=table[(r2+1)%5][c2]

        else:
            cipher+=table[r1][c2]
            cipher+=table[r2][c1]

    return cipher

def playfair_decrypt(text,key):
    table=generate_table(key)
    plain=""

    for i in range(0,len(text),2):
        a,b=text[i],text[i+1]
        r1,c1=find(table,a)
        r2,c2=find(table,b)

        if r1==r2:
            plain+=table[r1][(c1-1)%5]
            plain+=table[r2][(c2-1)%5]

        elif c1==c2:
            plain+=table[(r1-1)%5][c1]
            plain+=table[(r2-1)%5][c2]

        else:
            plain+=table[r1][c2]
            plain+=table[r2][c1]

    return plain

# ---------------- GUI ----------------

def encrypt():
    algo=algorithm.get()

    if algo=="Caesar":
        output.config(text=caesar_encrypt(message.get(),int(key.get())))
    else:
        output.config(text=playfair_encrypt(message.get(),key.get()))

def decrypt():
    algo=algorithm.get()

    if algo=="Caesar":
        output.config(text=caesar_decrypt(message.get(),int(key.get())))
    else:
        output.config(text=playfair_decrypt(message.get(),key.get()))

root=tk.Tk()
root.title("Substitution Cipher")
root.geometry("400x350")

algorithm=tk.StringVar(value="Caesar")

tk.Label(root,text="Substitution Cipher",font=("Arial",16)).pack(pady=10)

ttk.Radiobutton(root,text="Caesar Cipher",variable=algorithm,value="Caesar").pack()
ttk.Radiobutton(root,text="Playfair Cipher",variable=algorithm,value="Playfair").pack()

tk.Label(root,text="Message").pack()
message=tk.Entry(root,width=40)
message.pack()

tk.Label(root,text="Key (Shift or Playfair Key)").pack()
key=tk.Entry(root,width=30)
key.pack()

tk.Button(root,text="Encrypt",command=encrypt).pack(pady=5)
tk.Button(root,text="Decrypt",command=decrypt).pack()

output=tk.Label(root,text="",fg="blue",font=("Arial",12))
output.pack(pady=20)

root.mainloop()

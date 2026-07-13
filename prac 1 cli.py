# Practical 1A

# ---------------- Caesar Cipher ----------------

def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# ---------------- Playfair Cipher ----------------

def generate_key_table(key):
    key = key.upper().replace("J", "I")

    table = []
    used = set()

    for ch in key:
        if ch.isalpha() and ch not in used:
            table.append(ch)
            used.add(ch)

    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in used:
            table.append(ch)
            used.add(ch)

    matrix = []
    for i in range(0, 25, 5):
        matrix.append(table[i:i+5])

    return matrix


def find_position(table, ch):
    for i in range(5):
        for j in range(5):
            if table[i][j] == ch:
                return i, j


def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = ''.join(c for c in text if c.isalpha())

    result = ""
    i = 0

    while i < len(text):
        a = text[i]

        if i + 1 < len(text):
            b = text[i + 1]

            if a == b:
                result += a + "X"
                i += 1
            else:
                result += a + b
                i += 2
        else:
            result += a + "X"
            i += 1

    return result


def playfair_encrypt(text, key):
    table = generate_key_table(key)
    text = prepare_text(text)

    cipher = ""

    for i in range(0, len(text), 2):
        a = text[i]
        b = text[i + 1]

        r1, c1 = find_position(table, a)
        r2, c2 = find_position(table, b)

        if r1 == r2:
            cipher += table[r1][(c1 + 1) % 5]
            cipher += table[r2][(c2 + 1) % 5]

        elif c1 == c2:
            cipher += table[(r1 + 1) % 5][c1]
            cipher += table[(r2 + 1) % 5][c2]

        else:
            cipher += table[r1][c2]
            cipher += table[r2][c1]

    return cipher


def playfair_decrypt(text, key):
    table = generate_key_table(key)

    plain = ""

    for i in range(0, len(text), 2):
        a = text[i]
        b = text[i + 1]

        r1, c1 = find_position(table, a)
        r2, c2 = find_position(table, b)

        if r1 == r2:
            plain += table[r1][(c1 - 1) % 5]
            plain += table[r2][(c2 - 1) % 5]

        elif c1 == c2:
            plain += table[(r1 - 1) % 5][c1]
            plain += table[(r2 - 1) % 5][c2]

        else:
            plain += table[r1][c2]
            plain += table[r2][c1]

    return plain


# ---------------- Main Menu ----------------

while True:

    print("\n========== Substitution Cipher ==========")
    print("1. Caesar Encrypt")
    print("2. Caesar Decrypt")
    print("3. Playfair Encrypt")
    print("4. Playfair Decrypt")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        message = input("Enter Message: ")
        key = int(input("Enter Shift Key: "))
        print("Encrypted Message:", caesar_encrypt(message, key))

    elif choice == "2":
        message = input("Enter Cipher Text: ")
        key = int(input("Enter Shift Key: "))
        print("Decrypted Message:", caesar_decrypt(message, key))

    elif choice == "3":
        key = input("Enter Playfair Key: ")
        message = input("Enter Message: ")
        print("Encrypted Message:", playfair_encrypt(message, key))

    elif choice == "4":
        key = input("Enter Playfair Key: ")
        message = input("Enter Cipher Text: ")
        print("Decrypted Message:", playfair_decrypt(message, key))

    elif choice == "5":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")

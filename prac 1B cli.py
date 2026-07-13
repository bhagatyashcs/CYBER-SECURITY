# Practical 1B
# Rail Fence Cipher (Transposition Technique)

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


def decrypt(cipher, key):
    pattern = [['' for _ in range(len(cipher))] for _ in range(key)]

    row = 0
    direction = 1

  
    for col in range(len(cipher)):
        pattern[row][col] = '*'

        row += direction

        if row == 0 or row == key - 1:
            direction *= -1

   
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if pattern[i][j] == '*':
                pattern[i][j] = cipher[index]
                index += 1

    
    result = ""
    row = 0
    direction = 1

    for col in range(len(cipher)):
        result += pattern[row][col]

        row += direction

        if row == 0 or row == key - 1:
            direction *= -1

    return result


while True:
    print("\n===== Rail Fence Cipher =====")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        text = input("Enter Plain Text: ")
        key = int(input("Enter Number of Rails: "))
        print("Encrypted Text:", encrypt(text, key))

    elif choice == "2":
        text = input("Enter Cipher Text: ")
        key = int(input("Enter Number of Rails: "))
        print("Decrypted Text:", decrypt(text, key))

    elif choice == "3":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")

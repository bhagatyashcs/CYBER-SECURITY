from rsa_core import generate_keys, encrypt, decrypt

public_key = None
private_key = None
ciphertext = None


def main():
    global public_key, private_key, ciphertext

    while True:
        print("\n===== RSA Encryption and Decryption =====")
        print("1. Generate Keys")
        print("2. Encrypt Message")
        print("3. Decrypt Message")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            p = 61
            q = 53

            public_key, private_key = generate_keys(p, q)

            print("\nKeys Generated Successfully!")
            print("Public Key :", public_key)
            print("Private Key:", private_key)

        elif choice == "2":
            if public_key is None:
                print("\nPlease generate keys first.")
                continue

            message = input("Enter message: ")

            try:
                ciphertext = encrypt(message, public_key)

                print("\nOriginal Message:", message)
                print("Encrypted Message:", ciphertext)

            except ValueError as error:
                print("Error:", error)

        elif choice == "3":
            if private_key is None:
                print("\nPlease generate keys first.")
                continue

            if ciphertext is None:
                print("\nPlease encrypt a message first.")
                continue

            message = decrypt(ciphertext, private_key)

            print("\nEncrypted Message:", ciphertext)
            print("Decrypted Message:", message)

        elif choice == "4":
            print("\nExiting RSA program...")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()

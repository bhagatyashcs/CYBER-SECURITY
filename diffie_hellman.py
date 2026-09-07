# Diffie-Hellman Key Exchange

print("==========================================")
print("       DIFFIE-HELLMAN KEY EXCHANGE")
print("==========================================")

# Public values
p = int(input("\nEnter a prime number (p): "))
g = int(input("Enter a generator (g): "))

# Private keys
a = int(input("Enter Alice's private key: "))
b = int(input("Enter Bob's private key: "))

# Calculate public keys
A = pow(g, a, p)
B = pow(g, b, p)

print("\n--- Public Key Exchange ---")
print("Alice's public key:", A)
print("Bob's public key:", B)

# Calculate shared secret keys
alice_shared_key = pow(B, a, p)
bob_shared_key = pow(A, b, p)

print("\n--- Shared Secret Keys ---")
print("Alice's shared key:", alice_shared_key)
print("Bob's shared key:", bob_shared_key)

# Verify
if alice_shared_key == bob_shared_key:
    print("\nKey Exchange Successful!")
    print("Both Alice and Bob have the same shared secret key.")
else:
    print("\nKey Exchange Failed!")

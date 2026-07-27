import hmac
import hashlib

def generate_mac(key, message):
    return hmac.new(
        key.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()


def verify_mac(key, message, received_mac):
    computed_mac = generate_mac(key, message)
    return hmac.compare_digest(computed_mac, received_mac)


key = input("Enter the secret key: ")
message = input("Enter the message: ")


mac = generate_mac(key, message)
print("\nGenerated MAC:", mac)


received_mac = input("\nEnter the MAC to verify: ")

if verify_mac(key, message, received_mac):
    print("✅ MAC Verification Successful: Message is authentic.")
else:
    print("❌ MAC Verification Failed: Message has been altered or the MAC is incorrect.")

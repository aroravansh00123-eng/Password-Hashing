import hashlib
import secrets
import string


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))


print("=" * 60)
print("        PASSWORD SECURITY TOOL")
print("=" * 60)

print("""
1. Hash your password
2. Generate a secure password
3. Verify a password
4. Exit
""")

choice = input("ENTER YOUR CHOICE: ")

if choice == "1":

    password = input("ENTER YOUR PASSWORD: ")

    hashed_password = hash_password(password)

    print("\nPASSWORD HASHED SUCCESSFULLY!")
    print("SHA-256 Hash:")
    print(hashed_password)

elif choice == "2":

    length = int(input("ENTER PASSWORD LENGTH: "))

    if length < 8:
        print("Password length should be at least 8 characters.")
    else:
        password = generate_password(length)

        print("\nSECURE PASSWORD GENERATED:")
        print(password)

elif choice == "3":

    original_hash = input("ENTER THE STORED HASH: ")
    password = input("ENTER PASSWORD FOR VERIFICATION: ")

    new_hash = hash_password(password)

    if new_hash == original_hash:
        print("\nPASSWORD VERIFIED SUCCESSFULLY!")
    else:
        print("\nWRONG PASSWORD!")

elif choice == "4":

    print("Exiting...")

else:

    print("INVALID CHOICE!")

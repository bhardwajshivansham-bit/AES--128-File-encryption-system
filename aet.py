from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

# AES-128 key (16 bytes)
KEY = b"1234567890abcdef"

def encrypt_file(file_name):
    cipher = AES.new(KEY, AES.MODE_CBC)

    with open(file_name, "rb") as f:
        data = f.read()

    encrypted_data = cipher.iv + cipher.encrypt(
        pad(data, AES.block_size)
    )

    with open(file_name + ".enc", "wb") as f:
        f.write(encrypted_data)

    print("File Encrypted Successfully!")

def decrypt_file(file_name):
    with open(file_name, "rb") as f:
        iv = f.read(16)
        encrypted_data = f.read()

    cipher = AES.new(KEY, AES.MODE_CBC, iv)

    decrypted_data = unpad(
        cipher.decrypt(encrypted_data),
        AES.block_size
    )

    output_file = "decrypted_" + os.path.basename(file_name[:-4])

    with open(output_file, "wb") as f:
        f.write(decrypted_data)

    print("File Decrypted Successfully!")

# Menu
while True:
    print("\nAES-128 File Encryption System")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        file = input("Enter file name: ")
        encrypt_file(file)

    elif choice == "2":
        file = input("Enter encrypted file name: ")
        decrypt_file(file)

    elif choice == "3":
        break

    else:
        print("Invalid Choice!")
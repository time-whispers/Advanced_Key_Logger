from cryptography.fernet import Fernet

key = "YmKQ7kVhpDnB8lKlOuL2X12uzIWofbRBAumlPlhRz0o=" #  Enter the key value generated from the GenerateKey.py

keys_information_e = "e_keys_logged.txt"
system_information_e = "e_system.txt"
clipboard_information_e = "e_clipboard.txt"


encrypted_files = [keys_information_e, system_information_e, clipboard_information_e]
count = 0

for decrypting_file in encrypted_files:
    with open(encrypted_files[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open(encrypted_files[count], 'wb') as f:
        f.write(decrypted)

    count += 1

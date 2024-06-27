def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    while True:
        choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? (E/D): ").upper()
        if choice not in ['E', 'D']:
            print("Invalid choice, please select 'E' for encrypt or 'D' for decrypt.")
            continue
        
        message = input("Enter the message: ")
        try:
            shift = int(input("Enter the shift value: "))
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue
        
        if choice == 'E':
            result = encrypt(message, shift)
            print(f"Encrypted message: {result}")
        else:
            result = decrypt(message, shift)
            print(f"Decrypted message: {result}")
        
        again = input("Do you want to encrypt/decrypt another message? (Y/N): ").upper()
        if again != 'Y':
            break

if __name__ == "__main__":
    main()

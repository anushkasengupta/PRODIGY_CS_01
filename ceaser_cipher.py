def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():

            offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Program")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()
    
    if choice not in ('e', 'd'):
        print("Invalid choice. Please enter 'E' or 'D'.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (integer): "))
    except ValueError:
        print("Shift must be an integer.")
        return

    if choice == 'e':
        encrypted = caesar_cipher_encrypt(message, shift)
        print(f"Encrypted message: {encrypted}")
    else:
        decrypted = caesar_cipher_decrypt(message, shift)
        print(f"Decrypted message: {decrypted}")

if __name__ == "__main__":
    main()

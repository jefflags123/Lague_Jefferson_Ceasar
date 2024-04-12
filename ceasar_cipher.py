# Caesar cipher encryption function
def caesar_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            if char.isupper():
                encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_char = char  # Leave non-alphabetic characters unchanged
        encrypted_text += encrypted_char
    return encrypted_text

# Caesar cipher decryption function
def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            if char.isupper():
                decrypted_char = chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                decrypted_char = chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            decrypted_char = char  # Leave non-alphabetic characters unchanged
        decrypted_text += decrypted_char
    return decrypted_text

# Test the encryption and decryption functions
if __name__ == "__main__":
    # Sample message and shift value
    message = "Jefferson Lague."
    shift = 3

    # Encrypting the message
    encrypted_message = caesar_encrypt(message, shift)
    print("Encrypted message:", encrypted_message)

    # Decrypting the message
    decrypted_message = caesar_decrypt(encrypted_message, shift)
    print("Decrypted message:", decrypted_message)
def caesar_cipher(text, shift, encrypt):
    result = ""
    shift = shift if encrypt else -shift
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr(start + (ord(char) - start + shift) % 26)
        else:
            result += char
    return result

plaintext = "HELLO WORLD"
shift = 3
encrypted = caesar_cipher(plaintext, shift, 1)
decrypted = caesar_cipher(encrypted, shift, 0)

print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")

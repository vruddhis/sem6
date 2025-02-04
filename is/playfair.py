import itertools

def generate_playfair_matrix(key):
    key = "".join(dict.fromkeys(key.upper().replace("J", "I"))) 
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = key + "".join(c for c in alphabet if c not in key)
    return [list(matrix[i:i+5]) for i in range(0, 25, 5)]

def find_position(matrix, letter):
    for row, line in enumerate(matrix):
        if letter in line:
            return row, line.index(letter)

def playfair_cipher(text, key, encrypt=True):
    matrix = generate_playfair_matrix(key)
    text = text.upper().replace("J", "I")
    text_pairs = []
    
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) and text[i] != text[i+1] else "X"
        text_pairs.append((a, b))
        i += 2 if text[i] != text[i+1] else 1

    result = ""
    shift = 1 if encrypt else -1
    
    for a, b in text_pairs:
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:  
            result += matrix[row1][(col1 + shift) % 5] + matrix[row2][(col2 + shift) % 5]
        elif col1 == col2:  
            result += matrix[(row1 + shift) % 5][col1] + matrix[(row2 + shift) % 5][col2]
        else: 
            result += matrix[row1][col2] + matrix[row2][col1]

    return result

plaintext = "HELLO"
key = "KEYWORD"
encrypted = playfair_cipher(plaintext, key, encrypt=True)
decrypted = playfair_cipher(encrypted, key, encrypt=False)

print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")

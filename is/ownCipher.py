from sympy import mod_inverse

def encrypt(text, k, b):
    if gcd(k, 26) != 1:
        raise ValueError("k must be coprime to 26 for invertibility.")
    
    text = text.upper()
    encrypted_text = ""
    
    for char in text:
        if 'A' <= char <= 'Z':
            x = ord(char) - ord('A') + 1  
            y = (k * x + b) % 26  
            encrypted_text += chr((y - 1) % 26 + ord('A'))
        else:
            encrypted_text += char  
    
    return encrypted_text

def decrypt(text, k, b):
    k_inv = mod_inverse(k, 26)  
    text = text.upper()
    decrypted_text = ""
    
    for char in text:
        if 'A' <= char <= 'Z':
            y = ord(char) - ord('A') + 1
            x = (k_inv * (y - b)) % 26  
            decrypted_text += chr((x - 1) % 26 + ord('A'))
        else:
            decrypted_text += char
    
    return decrypted_text

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


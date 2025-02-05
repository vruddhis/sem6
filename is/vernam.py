def find_binary_ascii(char):
    ascii = ord(char)
    return bin(ascii).replace("0b", "") 

def xor(a, b):
    na = len(a)
    nb = len(b)
    if nb < na:
        b = '0' * (na - nb) + b
    else:
        a = '0' * (nb - na) + a
    ans = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            ans += '0'
        else:
            ans += '1'

def bin_ascii_to_char(binary_num):
    decimal = int(binary_num, 2)
    return chr(decimal)

def encrypt():
    key = (input("What is your key?"))
    m = input("What is your plaintext?")
    if len(key) != len(m):
        print("Invalid input. Lengths of key and plaintext should be same")
        return
    ans = ''
    for i in range(len(m)):
        ans += bin_ascii_to_char(xor(find_binary_ascii(m[i]), find_binary_ascii(key[i])))
    print("Ciphertext is ", ans)

def decrypt():
    key = (input("What is your key?"))
    m = input("What is your ciphertext?")
    if len(key) != len(m):
        print("Invalid input. Lengths of key and ciphertext should be same")
        return
    ans = ''
    for i in range(len(m)):
        ans += bin_ascii_to_char(xor(find_binary_ascii(m[i]), find_binary_ascii(key[i])))
    print("Plaintext is ", ans)
    
print("Encryption:\n")
encrypt()

print("Decryption:\n")
decrypt()

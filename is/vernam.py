def find_binary_ascii(char):
    ascii_val = ord(char)
    return format(ascii_val, '08b')  # Ensures 8-bit binary representation

def xor(a, b):
    na = len(a)
    nb = len(b)
    if nb < na:
        b = '0' * (na - nb) + b
    else:
        a = '0' * (nb - na) + a
    ans = ''
    for i in range(len(a)):
        ans += '0' if a[i] == b[i] else '1'
    return ans  # Add return statement to get the XOR result

def bin_ascii_to_char(binary_num):
    decimal = int(binary_num, 2)
    return chr(decimal)

def encrypt():
    key = input("What is your key? ")
    m = input("What is your plaintext? ")
    if len(key) != len(m):
        print("Invalid input. Lengths of key and plaintext should be the same.")
        return
    ans = ''
    for i in range(len(m)):
        xor_result = xor(find_binary_ascii(m[i]), find_binary_ascii(key[i]))
        ans += bin_ascii_to_char(xor_result)
    print("Ciphertext is:", ans)

def decrypt():
    key = input("What is your key? ")
    m = input("What is your ciphertext? ")
    if len(key) != len(m):
        print("Invalid input. Lengths of key and ciphertext should be the same.")
        return
    ans = ''
    for i in range(len(m)):
        xor_result = xor(find_binary_ascii(m[i]), find_binary_ascii(key[i]))
        ans += bin_ascii_to_char(xor_result)
    print("Plaintext is:", ans)

print("Encryption:\n")
encrypt()

print("\nDecryption:\n")
decrypt()

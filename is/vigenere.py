LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
def isAlphabet(char):
    return char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' 
def make_valid(m):
    ans = ''
    for char in m:
        if isAlphabet(char):
            ans += (char.upper())
        elif char == ' ':
            continue
        else:
            print("Only whitespaces and letters allowed")
            return -1
    return ans
def find_shift(key):
    shift = []
    for char in key:
        if char not in LETTERS:
            print("invalid key")
            return -1
        shift.append(LETTERS.index(char))
    return shift
def encrypt():
    key = (input("What is your key?"))
    m = input("What is your plaintext?")
    if make_valid(m) == -1:
        return
    if find_shift(key) == -1:
        return
    m = make_valid(m)
    key = find_shift(key)
    i = 0
    n = len(key)
    ans = ''
    for char in m:
        j = LETTERS.index(char)
        ans += LETTERS[(j + key[i]) % 26]
        i = (i + 1) % n
    print("Ciphertext is ", ans)


print("Encryption:\n")
encrypt()       

def isValid(m):
    for char in m:
        if char not in LETTERS:
            print("ciphertext is invalid")
            return False
    return True
def decrypt():
    key = (input("What is your key?"))
    m = input("What is your ciphertext?")
    if find_shift(key) == -1:
        print("INVALID KEY")
        return
    if not isValid(m):
        print("invalid ciphertext")
        return
    key = find_shift(key)
    n = len(key)
    ans = ''
    i = 0
    for char in m:
        j = LETTERS.index(char)
        ans += LETTERS[(j - key[i]) % 26]
        i = (i + 1) % n
    print("Plaintext is ", ans)

print("Decryption\n")
decrypt()

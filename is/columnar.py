def toCipher(key, plaintext):
    numCols = len(key)
    orderKey = [(key[i], i) for i in range(numCols)]
    orderKey.sort(key = lambda x:x[0])
    order = [0] * numCols
    for i in range(numCols):
        order[orderKey[i][1]] = i
    if len(plaintext) % numCols == 0:
        numRows = len(plaintext) // numCols
    else:
        numRows = len(plaintext) // numCols + 1
    matrix = [[0]*numCols for _ in range(numRows)]
    rem = numRows * numCols - len(plaintext)
    plaintext += 'X' * rem
    i = 0
    for row in range(numRows):
        for col in range(numCols):
            matrix[row][col] = plaintext[i]
            i += 1
    ciphertext = ''
    i = 0
    while i < numCols:
        colNumber = order.index(i)
        i += 1
        for j in range(numRows):
            ciphertext += matrix[j][colNumber]
    return ciphertext

        
def toPlain(key, ciphertext):
    numCols = len(key)
    orderKey = [(key[i], i) for i in range(numCols)]
    orderKey.sort(key = lambda x:x[0])
    order = [0] * numCols
    for i in range(numCols):
        order[orderKey[i][1]] = i
    if len(ciphertext) % numCols == 0:
        numRows = len(ciphertext) // numCols
    else:
        print("Something is wrong. Length of ciphertext is not divisible by lenght of key")
        return
    matrix = [[0]*numCols for _ in range(numRows)]
    i = 0
    cipherIndex = 0
    while i < numCols:
        colNumber = order.index(i)
        i += 1
        for row in range(numRows):
            matrix[row][colNumber] = ciphertext[cipherIndex]
            
            cipherIndex += 1
            
    plaintext = ''
    for row in range(numRows):
        for col in range(numCols):
            plaintext += matrix[row][col]
    return plaintext


    
def doubleColumnarEncryption(key1, key2, plaintext):
    firstEncryption = toCipher(key1, plaintext)
    return toCipher(key2, firstEncryption)

def doubleColumnarDecryption(key1, key2, cipher):
    firstDecryption = toPlain(key2, cipher)
    return toPlain(key1, firstDecryption)

def removeWhitespace(text):
    return ''.join(text.split())

def removeXs(cipher):
    return cipher.rstrip('X')

print(  toCipher('apple', removeWhitespace('I love cryptography')))
print(removeXs(toPlain('apple', toCipher('apple', removeWhitespace('I love cryptography')))))

CIPHER = (doubleColumnarEncryption('lemon', 'apple', removeWhitespace('I LOVE CRYPTOGRAPHY')))

print(CIPHER)
          
PLAIN = removeXs(doubleColumnarDecryption('lemon', 'apple', CIPHER))
print(PLAIN)

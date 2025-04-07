import math

def makeBlocks(binary_message):
    binary_message += '1'
    while (len(binary_message) + 64) % 512 != 0:
        binary_message += '0'
    original_length = len(binary_message) - 1 
    length_bits = bin(original_length)[2:].zfill(64)
    binary_message += length_bits
    blocks = [binary_message[i:i+512] for i in range(0, len(binary_message), 512)]
    return blocks

def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def sha1(binary_message):
    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476
    E = 0xC3D2E1F0
    blocks = makeBlocks(binary_message)

    for b in blocks:
        w = [int(b[i*32:(i+1)*32], 2) for i in range(16)]
        for i in range(16, 80):
            w.append(left_rotate(w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16], 1))
        
        a, b, c, d, e = A, B, C, D, E
        

        for i in range(80):
            if 0 <= i <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6
            
            temp = (left_rotate(a, 5) + f + e + k + w[i]) & 0xFFFFFFFF
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp
        

        A = (A + a) & 0xFFFFFFFF
        B = (B + b) & 0xFFFFFFFF
        C = (C + c) & 0xFFFFFFFF
        D = (D + d) & 0xFFFFFFFF
        E = (E + e) & 0xFFFFFFFF

    hh = (A << 128) | (B << 96) | (C << 64) | (D << 32) | E
    return hh
    


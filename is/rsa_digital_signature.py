from sha import sha1

p = 61  
q = 53  
n = p * q 
phi = (p - 1) * (q - 1)  
e = 17  


def mod_inverse(e, phi):
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise Exception("Modular inverse does not exist")
    return x % phi

d = mod_inverse(e, phi) 



def rsa_signature(message):
    digest = sha1(message)
    print(len(str(digest)))
    digital_signature = pow(digest, d, n) 
    return digital_signature


message = "1011111000101"
signature = rsa_signature(message)
print("Digital Signature:", signature)
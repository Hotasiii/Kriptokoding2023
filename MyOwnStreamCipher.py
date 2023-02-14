# MyOwnStreamCipher: Modified RC4
import random
# Key-Scheduling Algorithm (KSA)

def KSA(key):
    # Inisialisasi array "S"
    S = [0 for i in range(256)]

    # Inisialisasi array S dengan bilangan genap, diikuti dengan bilangan ganjil
    for i in range(128):
        S[i] = i*2

    for i in range(128, 256):
        S[i] = (i - 128)*2 + 1

    # Mengacak array S
    random.seed(len(key) % 256)
    random.shuffle(S)

    return S

# Pseudo-random generation algorithm (PRGA)
def PRGA(S, plainText: bytes):
    # S = array KSA
    

    C = []

    # Mengubah byte plaintext menjadi array
    P = []
    for byte in plainText:
        P.append(byte)
    
    i = 0
    j = 0
    
    for k in range(len(plainText)):   
        i = (i + 1) % 256
        j = (j + S[i]) % 256

        # Swap elemen di dalam array
        S[i], S[j] = S[j], S[i]

        keyStream = S[(S[i] + S[j]) % 256]

        C.append(keyStream ^ ord(P[k]))
        
    return bytes(C)

def main(key, base):
    S = KSA(key)
    result = PRGA(S, base)
    
    return result



print(main("asdf", "kriptografi") )


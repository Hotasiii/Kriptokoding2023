# Vigenere Cipher standard (26 huruf alfabet)
def vigenereStandardEncrypt(plainText: str, key: str) -> str:
    # Key handling if len(key) < len(plainText)
    if len(key) < len(plainText):
        key = list(key) # Key harus diubah menjadi list terlebih dahulu agar bisa diappend
        for i in range(len(plainText) - len(key)):
            key.append(key[i % len(key)])  
        "".join(key)          

    # Encrypt algorithm
    cipherText = []
    for i in range(len(plainText)):
        encrpyt = (ord(plainText[i]) + ord(key[i])) % 26
        encrpyt += ord('A')
        cipherText.append(chr(encrpyt))
    return print("".join(cipherText))

def vigenereStandardDecrpyt(cipherText: str, key: str) -> str:
    origText = []
    # Decrypt algorithm
    for i in range(len(cipherText)):
        decrpyt = (ord(cipherText[i]) - ord(key[i]) + 26) % 26 # Ditambah 26 sebelum di modulo karena modulo negative numbers in Python kind of works differently
        decrpyt += ord('A')
        origText.append(chr(decrpyt))
    return print("".join(origText))

# Extended Vigenere Cipher: Auto-key (256 karakter ASCII)
def vigenereAutoKeyEncrypt(plainText: str, key: str) -> str:
    # Kode
    return 0

def vigenereAutoKeyDecrypt(plainteks: str, key: str) -> str:
    # Kode
    return 0

# Playfair Cipher (26 huruf alfabet)
# One-time pad (26 huruf alfabet)
# Bonus: Enigma Cipher dengan 3-rotor (26 huruf alfabet)

# Input
plainText, key= input(), input()
# vigenereStandardEncrypt(plainText, key)
# vigenereStandardDecrpyt(plainText, key)





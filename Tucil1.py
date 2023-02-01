# Vigenere Cipher standard (26 huruf alfabet)
def vigenereStandardKeyGenerator(plainText: str, key: str) -> str:
    # Key handling if len(key) < len(plainText)
    if len(key) < len(plainText):
        key = list(key) # Key harus diubah menjadi list terlebih dahulu agar bisa diappend
        for i in range(len(plainText) - len(key)):
            key.append(key[i % len(key)])  

            # Case if key not alphabet
        return "".join(key)          

def vigenereStandardEncrypt(plainText: str, key: str) -> str:
    cipherText = []
    for i in range(len(plainText)):
        # Case if plainText or key not alphabet 
        # Abaikan numerik, spesial karakter, spasi
        # Kode

        # Main encrypt algorithm
        encrpyt = (ord(plainText[i]) + ord(key[i])) % 26
        encrpyt += ord('A')
        cipherText.append(chr(encrpyt))
    return print("".join(cipherText), key)


def vigenereStandardDecrpyt(cipherText: str, key: str) -> str:
    origText = []

    
    # Decrypt algorithm
    for i in range(len(cipherText)):

        # Case if plainText or key not alphabet 
        # Abaikan numerik, spesial karakter, spasi
        # Kode

        # Main decrypt algorithm
        decrpyt = (ord(cipherText[i]) - ord(key[i]) + 26) % 26 # Ditambah 26 sebelum di modulo karena modulo negative numbers in Python kind of works differently
        decrpyt += ord('A')
        origText.append(chr(decrpyt))
    return print("".join(origText))

# Extended Vigenere Cipher: Auto-key (256 karakter ASCII)
def vigenereAutoKeyGenerator(plainText: str, key: str) -> str:
    # Read file as a file of bytes, special characters, numbers, spaces included (256 ASCII)
    # Extended vigenere cipher: Auto-key Vigenere - Key handling if len(key) > len(plainText)
    if len(key) > len(plainText):
        key = list(key)
        for i in range(len(plainText) - len(key)):
            key.append(plainText[i % len(plainText)])
        return "".join(key)

# Playfair Cipher (26 huruf alfabet)
# One-time pad (26 huruf alfabet)
# Bonus: Enigma Cipher dengan 3-rotor (26 huruf alfabet)

# Input from keyboard
plainText, key= input(), input()
vigenereStandardEncrypt(plainText, key)

# Input from file, read file (ex: .txt/word)

# Simpan cipherteks ke dalam file = not yet done 
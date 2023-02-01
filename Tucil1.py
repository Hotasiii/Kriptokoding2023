# Vigenere Cipher standard (26 huruf alfabet)
def VigenereStandardEncrypt(plainText: str, key: str) -> str:
    # Hanya mengambil 26 huruf alfabet 
    newPlainText = ""
    newKey = ""

    for i in plainText:
        if (ord(i) >= 65 and ord(i) <= 122):
            newPlainText += i 

    for j in key:
        if (ord(j) >= 65 and ord(i) <= 122):
            newKey += j 
    
    # Standardizing all plainText and Key to uppercase
    newPlainText = newPlainText.upper()
    newKey = newKey.upper()

    # Key handling if len(key) < len(plainText)
    if len(newKey) < len(newPlainText):
        newKey = list(newKey) # Key harus diubah menjadi list terlebih dahulu agar bisa diappend
        for i in range(len(newPlainText) - len(newKey)):
            newKey.append(newKey[i % len(newKey)])  
        "".join(newKey)    

    # Main encrypt algorithm       
    result = []
    for i in range(len(newPlainText)):
        cipherText = ((ord(newPlainText[i]) + ord(newKey[i])) % 26) + ord('A')
        result.append(chr(cipherText))
    return print("".join(result))

def VigenereStandardDecrpyt(plainText: str, key: str) -> str:
    # Hanya mengambil 26 huruf alfabet 
    newPlainText = ""
    newKey = ""

    for i in plainText:
        if (ord(i) >= 65 and ord (i) <= 122):
            newPlainText += i 

    for j in key:
        if (ord(j) >= 65 and ord(i) <= 122):
            newKey += j 
    
    # Standardizing all plainText and Key to uppercase
    newPlainText = newPlainText.upper()
    newKey = newKey.upper()

    # Key handling if len(key) < len(plainText)
    if len(newKey) < len(newPlainText):
        newKey = list(newKey) # Key harus diubah menjadi list terlebih dahulu agar bisa diappend
        for i in range(len(newPlainText) - len(newKey)):
            newKey.append(newKey[i % len(newKey)])  
        "".join(newKey)    

    # Main decrypt algorithm
    result = []
    for i in range(len(plainText)):
        origText = ((ord(plainText[i]) - ord(newKey[i]) + 26) % 26) + ord('A') # Ditambah 26 sebelum di modulo karena modulo negative numbers in Python kind of works differently
        result.append(chr(origText))

    return print("".join(result))

# Extended Vigenere Cipher: Auto-key (256 karakter ASCII)
def vigenereExtendedEncrypt(plain, key: bytes):
    result = ""

    for i in range(len(plain)):
        if ord(plain[i]) >= 0 and ord(plain[i]) <= 255:
            cipherText = (ord(plain[i]) + ord(key[i % len(key)])) % 256
            result += chr(cipherText)
        else:
            result += plain[i]    
    return print(result)

def vigenereExtendedDecrypt(plain, key: bytes):
    result = ""

    for i in range(len(plain)):
        if ord(plain[i]) >= 0 and ord(plain[i]) <= 255:
            origText = (ord(plain[i]) - ord(key[i % len(key)])) % 256
            result += chr(origText)
        else:
            result += plain[i]    
    return print(result) 


# Input from keyboard
plainText, key= input(), input()
# VigenereStandardEncrypt(plainText, key) Works
# VigenereStandardDecrpyt(plainText, key) Works
# vigenereExtendedEncrypt(plainText, key)
vigenereExtendedDecrypt(plainText, key)

# Input from file, read file (ex: .txt/word)

# Simpan cipherteks ke dalam file = not yet done 
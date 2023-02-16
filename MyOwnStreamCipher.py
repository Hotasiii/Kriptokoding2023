# MyOwnStreamCipher: Modified RC4
# Key-Scheduling Algorithm (KSA)
from playfair_cipher import *
from Tucil1 import *
from bitarray import bitarray

# Dalam list alfabet ini dibuang huruf 'j' agar terdapat 25 huruf
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def Binary_to_Decimal(binary):
    decimal, i = 0, 0 
    while(binary != 0):
        temp = binary % 10
        decimal = decimal + temp * pow(2, i)
        binary = binary//10
        i += 1
    return (decimal)   
    
def Binary_to_String(binary_text):
    string_text = ''
    for i in range(0, len(binary_text), 7):
        temp = int(binary_text[i:i + 7])
        decimal = Binary_to_Decimal(temp)
        string_text += chr(decimal)
    return string_text

def KSA(key, cipher):
    # Inisialisasi array "S"
    S = [0 for i in range(256)]

    # Inisialisasi array S dengan bilangan genap, diikuti dengan bilangan ganjil
    for i in range(128):
        S[i] = i*2

    for i in range(128, 256):
        S[i] = (i - 128)*2 + 1

    # Konversi kunci dari bentuk string of character menjadi string of bytes
    key_byte = bytearray(key, encoding='utf-8')

    # Permutasi pertama nilai-nilai dalam array "S" dengan kunci "key"
    index_baru = 0
    for i in range(255):
        index_baru = (index_baru + S[i] + key_byte[(i % len(key_byte))]) % 256
        temp_value = S[index_baru]
        S[index_baru] = S[i]
        S[i] = temp_value

    # Permutasi kedua nilai-nilai dalam array "S" dengan kunci "key" yang telah dienkripsi
    # Plainteks digantikan dengan string tetap 'kriptografi'
    teks = "kriptografi"
    if (cipher == '1'):
        key_encrypted = vigenereExtendedEncrypt(teks, key)
    else:
        key_encrypted = Playfair_Cipher_Encrypt(generate_encryption_key_matrix(key, alphabet_list), teks)
    index_baru = 0
    # Setelah dienkripsi, kunci yang masih dalam bentuk string diubah menjadi bentuk byte
    key_encrypted = bytearray(key_encrypted, encoding='utf-8')
    for i in range(255):
        index_baru = (index_baru + S[i] + key_encrypted[(i % len(key_encrypted))]) % 256
        temp_value = S[index_baru]
        S[index_baru] = S[i]
        S[i] = temp_value

    # Permutasi ketiga nilai-nilai dalam array "S" dengan kunci "key_encrypted" yang mengalami LFSR
    key_LFSR = key_encrypted
    key_final = []
    for i in range(len(key_LFSR)):
        byte_n = key_LFSR[0]
        for j in range(1, len(key_LFSR)):
            byte_n = byte_n ^ key_LFSR[j]
        key_final.append(key_LFSR[len(key_LFSR)-1])
        for k in range(len(key_LFSR), 1, -1):
            key_LFSR[k-1] = key_LFSR[k-2]
        key_LFSR[0] = byte_n
    index_baru = 0
    for i in range(255):
        index_baru = (index_baru + S[i] + key_final[(i % len(key_final))]) % 256
        temp_value = S[index_baru]
        S[index_baru] = S[i]
        S[i] = temp_value
    
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

def main(key, base, cipher):
    S = KSA(key, cipher)
    result = PRGA(S, base)
    
    return result


plainteks = input("Masukkan plainteks: ")
key = input("Masukkkan kunci rahasia: ")
print("1. Extended Vigenere Cipher")
print("2. Playfair Cipher")
cipher = input("Masukkan jenis cipher yang ingin digunakan: ")
while (cipher != '1' and cipher != '2'):
    print("Masukkan input yang valid!")
    cipher = input("Masukkan jenis cipher yang ingin digunakan: ")
print(main(key, plainteks, cipher))


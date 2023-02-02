import tkinter
from tkinter import *
from tkinter import filedialog

from .playfair_cipher import *

# Fungsi untku membuka file
def open_file():
   file_path = filedialog.askopenfilename(title="Open a Text File", filetypes=(("text    files","*.txt"), ("all files","*.*")))
   if (file_path == ''):
    return ''
   else:
    file = open(file_path,'r')
    text = file.read()
    file.close()
    return text

menu_input = int(input("Apa yang mau dilakukan? \n 1. Enkripsi Text \n 2. Dekripsi Text \n"))
while (menu_input != 1 and menu_input != 2):
    print("Masukkan Angka yang Valid!")
    menu_input = int(input("Apa yang mau dilakukan? \n 1. Enkripsi Text \n 2. Dekripsi Text \n"))
    print("1. Enkripsi Text")
    print("2. Dekripsi Text")
if (menu_input == 1):
    user_input = input("Masukkan teks yang akan dienkripsi:")
    key = input("Masukkan kunci enkripsi:").lower()
    removed_space_input = remove_space(user_input.lower())
    grouped_input = group_fill(removed_space_input)
    if ("j" in user_input or "j" in key):
        encryption_table = generate_encryption_key_matrix(key,alphabet_list_i)
    else:
        encryption_table = generate_encryption_key_matrix(key,alphabet_list_j)
    encrypted_text_array = Playfair_Cipher_Encrypt(encryption_table,grouped_input)
    encrypted_text = ''
    for i in range(len(encrypted_text_array)):
        encrypted_text += encrypted_text_array[i]
    print("Plain Text: " + user_input)
    print("Encryption Key: " + key)
    print("Encrypted Text: " + encrypted_text)

    text_file = open("./Data.txt", "w")
    text_file.write(encrypted_text)
    text_file.close()

else:
    input_type = int(input("Lewat apa teks akan didekripsi? \n 1. Ketik teks di terminal \n 2. Lewat file \n"))
    while (input_type != 1 and input_type != 2):
        print("Masukkan Angka yang Valid!")
        input_type = int(input("Lewat apa teks akan didekripsi? \n 1. Ketik teks di terminal \n 2. Lewat file \n"))
    if (input_type == 1):
        encrypted_text = input("Masukkan teks yang terenkripsi: ")
    else:
        # Create an instance of window
        # win=Tk()
        # Set the geometry of the window
        # win.geometry("0x0")
        win=Tk().withdraw()
        encrypted_text = open_file()
        while (encrypted_text == ''):
            print("Jangan di cancel dong :(")
            encrypted_text = open_file()
    key = input("Masukkan kunci enkripsi yang digunakan: ")
    decrypted_text_array = Playfair_Cipher_Decrypt(encrypted_text,key)
    decrypted_text = ''
    for i in range(len(decrypted_text_array)):
        decrypted_text += decrypted_text_array[i]
    print("Decrypted Text: " + decrypted_text)


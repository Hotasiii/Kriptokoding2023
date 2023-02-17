from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox

from playfair_cipher import *
from otp import *
from Tucil1 import *
from MyOwnStreamCipher import *
import json

# Fungsi untuk start main menu
def start_menu(menu_awal):
    menu = Tk()
    menu_awal.destroy()
    window_setting(menu)

    # Label untuk input user manual
    label=Label(menu, text="Pilih Jenis Cipher yang Ingin Digunakan", font=("Courier 22 bold"), wraplength=450)
    label.pack()

    #Setiap tombol mengarah ke menu masing-masing jenis cipher
    ttk.Button(menu, text= "Our Stream Cipher", width= 20, command= lambda: stream_cipher_window_start(menu)).pack(pady=20)

# Fungsi untuk setting geometry window tk
def window_setting(menu):
    w = 700 # Lebar window menu
    h = 700 # Tinggu window menu

    # get screen width and height
    ws = menu.winfo_screenwidth() # lebar layar
    hs = menu.winfo_screenheight() # tinggi layar

    # Hitung koordinat x,y dari window menu
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # Letak window menu di tengah layar
    menu.geometry('%dx%d+%d+%d' % (w, h, x, y))

# Fungsi untuk konversi angka biner ke bentuk decimal
def Binary_to_Decimal(binary):
    decimal, i = 0, 0 
    while(binary != 0):
        temp = binary % 10
        decimal = decimal + temp * pow(2, i)
        binary = binary//10
        i += 1
    return (decimal)   

# Fungsi untuk menampilkan cipherteks/plainteks sebagai satu string
def whole_text_show(menu, text):
    label=Label(menu, text="Converted Text: \n" + text, font=("Courier 12 bold"))
    label.pack(pady=20)
    save_prompt(menu, text)

# Fungsi untuk membuka file
def open_file():
    file_path = filedialog.askopenfilename(title="Open a Text File", filetypes=(("text    files","*.txt"), ("all files","*.*")))
    # Jika pengguna pencet tombol 'cancel'
    if (file_path == ''):
        return ''
    else:
        # Jika file yang disubmit adalah file biner
        if (file_path[-3:] == 'bin'):
            file = open(file_path,'r', encoding="utf-8")
            bin_text = file.read()
            file.close()
            string_text = ''
            # Mengonversi data biner ke bentuk decimal, lalu ke string
            for i in range(0, len(bin_text), 7):
                temp = int(bin_text[i:i + 7])
                decimal = Binary_to_Decimal(temp)
                string_text += chr(decimal)
            return string_text
        else:
            file = open(file_path,'r', encoding="utf-8")
            text = file.read()
            file.close()
            return text

# Check input dari user, keluarkan alert message box jika input tidak valid
def check_input(menu, input, cipher_type):
    # Kalau input valid
    if (input == '1' or input == '2'):
        if (cipher_type == 'stream'):
            stream_cipher_menu(menu, input)
        elif (cipher_type == 'stream_enkripsi'):
            stream_cipher_enkripsi(menu,input)
        elif (cipher_type == 'stream_dekripsi'):
            stream_cipher_dekripsi(menu,input)
    
    # kalau input tidak valid
    else:
        messagebox.showinfo(title="Error", message="Pilihlah angka yang valid!")
        if (cipher_type == 'stream'):
            stream_cipher_window_start(menu) 
        
        
# Menyimpan hasil ciphertext ke dalam file data.txt
def save_text(menu, encrypted_text):
    file = open("./Data.txt", "w", encoding="utf-8")
    file.write(encrypted_text)
    file.close()
    messagebox.showinfo(title="Saved", message="Hasil berhasil disimpan.")
    start_menu(menu)

# Fungsi yang menampilkan opsi untku simpan teks dalam file eksternal
def save_prompt(menu, text):
    label=Label(menu, text="Simpan hasil dalam file eksternal?", font=("Courier 16 bold"), wraplength=450)
    label.pack(pady=20)

    button = ttk.Button(menu, text= "Simpan",width= 20, command = lambda: save_text(menu, text))
    button.pack(pady=5)

    button = ttk.Button(menu, text= "Tidak Simpan",width= 20, command = lambda: start_menu(menu))
    button.pack(pady=5)

# Fungsi untuk menapilkan teks dari input pada GUI 
def show_encrypted_text(menu, text, key, cipher_type, permutation):
    if (cipher_type == 'stream'):
        encrypted_text_array = enkripsi_RC4(key, text, permutation)
        encrypted_text = ''
        for i in range(len(encrypted_text_array)):
            encrypted_text += encrypted_text_array[i]

    # Di sini intinya udah harus ada encrypted_text dari setiap jenis cipher
    label=Label(menu, text="Bagimana cipherteks ditampilkan?", font=("Courier 16 bold"), wraplength=450)
    label.pack(pady=10)

    button = ttk.Button(menu, text= "Tampilkan dalam satu kalimat panjang",width= 50, command = lambda: whole_text_show(menu, encrypted_text))
    button.pack(pady=5, padx= 20)

def show_decrypted_text(menu, text, key, cipher_type):
    decrypted_text_array = dekripsi_RC4(KSA(key, cipher_type), text)
    decrypted_text = ''
    for i in range(len(decrypted_text_array)):
        decrypted_text += decrypted_text_array[i]

    # Di sini intinya udah harus ada decrypted_text dari setiap jenis cipher
    label=Label(menu, text="Bagimana plainteks ditampilkan?", font=("Courier 16 bold"), wraplength=450)
    label.pack(pady=10)

    button = ttk.Button(menu, text= "Tampilkan dalam satu kalimat panjang",width= 50, command = lambda: whole_text_show(menu, decrypted_text))
    button.pack(pady=5, padx= 20)

# Fungsi yang memunculkan window baru untuk Stream Cipher
def stream_cipher_window_start(menu):
    menu_stream = Tk()
    menu.destroy()
    window_setting(menu_stream)
    # Teks
    label=Label(menu_stream, text="Apa yang mau dilakukan? \n 1. Enkripsi Text \n 2. Dekripsi Text \n", font=("Courier 15 bold"))
    label.pack()
    # Entry widget untuk input user
    menu_input= Entry(menu_stream, width= 5)
    menu_input.focus_set()
    menu_input.pack()

    # Tombol untuk submit
    button = ttk.Button(menu_stream, text= "Submit",width= 20, command = lambda: check_input(menu_stream, menu_input.get(), "stream"))
    button.pack(pady=20)

# Fungsi yang memunculkan window enkripsi/dekripsi tergantung input user
def stream_cipher_menu(menu, menu_input):
    # user pilih enkripsi stream 
    if (menu_input == '1'):
        menu_enkripsi = Tk()
        menu.destroy()
        window_setting(menu_enkripsi)
        # Teks
        label=Label(menu_enkripsi, text="Lewat apa teks akan dienkripsi? \n 1. Ketik teks di terminal \n 2. Lewat file \n", font=("Courier 15 bold"), wraplength=450)
        label.pack()

        # Entry widget untuk input user
        menu_input= Entry(menu_enkripsi, width= 5)
        menu_input.focus_set()
        menu_input.pack()

        #CTombol untuk submit
        button = ttk.Button(menu_enkripsi, text= "Submit",width= 20, command = lambda: check_input(menu_enkripsi, menu_input.get(), "stream_enkripsi"))
        button.pack(pady=20)

    # user pilih dekripsi stream
    else:
        menu_dekripsi = Tk()
        window_setting(menu_dekripsi)
        menu.destroy()
        # Teks
        label=Label(menu_dekripsi, text="Lewat apa teks akan didekripsi? \n 1. Ketik teks di terminal \n 2. Lewat file \n", font=("Courier 15 bold"), wraplength=450)
        label.pack()

        # Entry widget untuk input user
        menu_input= Entry(menu_dekripsi, width= 5)
        menu_input.focus_set()
        menu_input.pack()

        #CTombol untuk submit
        button = ttk.Button(menu_dekripsi, text= "Submit",width= 20, command = lambda: check_input(menu_dekripsi, menu_input.get(), "stream_dekripsi"))
        button.pack(pady=20)

# Fungsi enkripsi stream
def stream_cipher_enkripsi(menu, input_type):
    if (input_type == '1'):
        menu_enkripsi_1 = Tk()
        window_setting(menu_enkripsi_1)
        menu.destroy()

        # Input Teks
        label=Label(menu_enkripsi_1, text="Masukkan teks yang akan dienkripsi: ", font=("Courier 15 bold"))
        label.pack()
        # Entry widget untuk input user
        menu_input_teks= Entry(menu_enkripsi_1, width= 30)
        menu_input_teks.focus_set()
        menu_input_teks.pack()

        # Input Key
        label=Label(menu_enkripsi_1, text="Masukkan kunci: ", font=("Courier 15 bold"))
        label.pack()
        # Entry widget untuk input user
        menu_input_key= Entry(menu_enkripsi_1, width= 20)
        menu_input_key.focus_set()
        menu_input_key.pack()

        # Input cipher permutasi KSA stream Cipher
        label=Label(menu_enkripsi_1, text="Apa jenis cipher yang ingin digunakan untuk permutasi KSA sebelum enkripsi? \n 1. Extended Vigenere Cipher \n 2. Playfair Cipher \n", font=("Courier 15 bold"), wraplength=450)
        label.pack()
        # Entry widget untuk input user
        menu_input_permutation= Entry(menu_enkripsi_1, width= 20)
        menu_input_permutation.focus_set()
        menu_input_permutation.pack()
        
        button = ttk.Button(menu_enkripsi_1, text= "Simpan",width= 20, command = lambda: show_encrypted_text(menu_enkripsi_1, menu_input_teks.get(), menu_input_key.get(), 'stream', menu_input_permutation.get()))
        button.pack(pady=20)

    # Teks
    else:
        text = open_file()
        while (text == ''):
            print("Jangan di cancel dong :(")
            text = open_file()
        menu_enkripsi_2 = Tk()
        window_setting(menu_enkripsi_2)
        menu.destroy()

        label=Label(menu_enkripsi_2, text="Masukkan kunci: ", font=("Courier 15 bold"))
        label.pack()
        # Entry widget untuk input user
        menu_input= Entry(menu_enkripsi_2, width= 20)
        menu_input.focus_set()
        menu_input.pack()

        # Input cipher permutasi KSA stream Cipher
        label=Label(menu_enkripsi_2, text="Apa jenis cipher yang ingin digunakan untuk permutasi KSA sebelum enkripsi? \n 1. Extended Vigenere Cipher \n 2. Playfair Cipher \n", font=("Courier 15 bold"), wraplength=450)
        label.pack()
        # Entry widget untuk input user
        menu_input_permutation= Entry(menu_enkripsi_2, width= 30)
        menu_input_permutation.focus_set()
        menu_input_permutation.pack()

        button = ttk.Button(menu_enkripsi_2, text= "Simpan",width= 20, command = lambda: show_encrypted_text(menu_enkripsi_2, text, menu_input.get(), 'stream', menu_input_permutation.get()))
        button.pack(pady=20)

# Fungsi dekripsi stream
def stream_cipher_dekripsi(menu, input_type):
    if (input_type == '1'):
        menu_dekripsi_1 = Tk()
        window_setting(menu_dekripsi_1)
        menu.destroy()

        # Input Teks
        label=Label(menu_dekripsi_1, text="Masukkan teks yang akan didekripsi: ", font=("Courier 15 bold"))
        label.pack()
        # Entry widget untuk input user
        menu_input_teks= Entry(menu_dekripsi_1, width= 30)
        menu_input_teks.focus_set()
        menu_input_teks.pack()

        # Input Key
        label=Label(menu_dekripsi_1, text="Masukkan kunci: ", font=("Courier 15 bold"))
        label.pack()
        # Entry widget untuk input user
        menu_input_key= Entry(menu_dekripsi_1, width= 20)
        menu_input_key.focus_set()
        menu_input_key.pack()

        # Input cipher permutasi KSA stream Cipher
        label=Label(menu_dekripsi_1, text="Apa jenis cipher yang ingin digunakan untuk permutasi KSA sebelum enkripsi? \n 1. Extended Vigenere Cipher \n 2. Playfair Cipher \n", font=("Courier 15 bold"), wraplength=450)
        label.pack()
        # Entry widget untuk input user
        menu_input_permutation= Entry(menu_dekripsi_1, width= 30)
        menu_input_permutation.focus_set()
        menu_input_permutation.pack()

        button = ttk.Button(menu_dekripsi_1, text= "Simpan",width= 20, command = lambda: show_decrypted_text(menu_dekripsi_1, menu_input_teks.get(), menu_input_key.get(), menu_input_permutation.get()))
        button.pack(pady=20)

    else:
        text = open_file()
        while (text == ''):
            print("Jangan di cancel dong :(")
            text = open_file()
        menu_dekripsi_2 = Tk()
        window_setting(menu_dekripsi_2)
        menu.destroy()

        label=Label(menu_dekripsi_2, text="Masukkan kunci: ", font=("Courier 15 bold"))
        label.pack()
        # Entry widget untuk input user
        menu_input= Entry(menu_dekripsi_2, width= 20)
        menu_input.focus_set()
        menu_input.pack()

        # Input cipher permutasi KSA stream Cipher
        label=Label(menu_dekripsi_2, text="Apa jenis cipher yang ingin digunakan untuk permutasi KSA sebelum enkripsi? \n 1. Extended Vigenere Cipher \n 2. Playfair Cipher \n", font=("Courier 15 bold"), wraplength=450)
        label.pack()
        # Entry widget untuk input user
        menu_input_permutation= Entry(menu_dekripsi_2, width= 30)
        menu_input_permutation.focus_set()
        menu_input_permutation.pack()

        button = ttk.Button(menu_dekripsi_2, text= "Simpan",width= 20, command = lambda: show_decrypted_text(menu_dekripsi_2, text, menu_input.get(), menu_input_permutation.get()))
        button.pack(pady=20)

# Start
menu = Tk()
start_menu(menu)
menu.mainloop()

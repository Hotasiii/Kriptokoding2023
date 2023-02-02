from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox

from playfair_cipher import *

# Fungsi untuk start main menu
def start_menu(menu_awal):
    menu = Tk()
    menu_awal.destroy()
    window_setting(menu)

    # Label untuk input user manual
    label=Label(menu, text="Pilih Jenis Cipher yang Ingin Digunakan", font=("Courier 22 bold"), wraplength=450)
    label.pack()

    #Create a Button to validate Entry Widget
    ttk.Button(menu, text= "Playfair Cipher",width= 20, command= lambda: playfair_cipher_window_start(menu)).pack()

# Fungsi untuk setting geometry window tk
def window_setting(menu):
    w = 700 # Lebar window menu
    h = 500 # Tinggu window menu

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

# Fungsi untuk membuka file
def open_file():
    file_path = filedialog.askopenfilename(title="Open a Text File", filetypes=(("text    files","*.txt"), ("all files","*.*")))
    # Jika pengguna pencet tombol 'cancel'
    if (file_path == ''):
        return ''
    else:
        # Jika file yang disubmit adalah file biner
        if (file_path[-3:] == 'bin'):
            file = open(file_path,'r')
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
            file = open(file_path,'r')
            text = file.read()
            file.close()
            return text

# Check input dari user, keluarkan alert message box jika input tidak valid
def check_input(menu, input, cipher_type):
    # Kalau input valid
    if (input == '1' or input == '2'):
        if (cipher_type == 'playfair'):
            playfair_cipher_menu(menu, input)
        elif (cipher_type == 'playfair_enkripsi'):
            playfair_cipher_enkripsi(menu,input)
        elif (cipher_type == 'playfair_dekripsi'):
              playfair_cipher_dekripsi(menu,input)
            # TAMBAH JENIS CIPHER LAIN

    # kalau input tidak valid
    else:
        messagebox.showinfo(title="Error", message="Pilihlah angka yang valid!")
        if (cipher_type == 'playfair'):
            playfair_cipher_window_start(menu) # TAMBAH JENIS CIPHER LAIN
        
# Menyimpan hasil ciphertext ke dalam file data.txt
def save_text(menu, encrypted_text):
    text_file = open("./Data.txt", "w")
    text_file.write(encrypted_text)
    text_file.close()
    messagebox.showinfo(title="Saved", message="Ciphertext berhasil disimpan")
    start_menu(menu)

# Fungsi untuk menapilkan teks dari input pada GUI 
def show_encrypted_text(menu, text, key, cipher_type):
    if (cipher_type == 'playfair'):
        removed_space_input = remove_space(text.lower())
        grouped_input = group_fill(removed_space_input)
        if ("j" in text or "j" in key):
            encryption_table = generate_encryption_key_matrix(key,alphabet_list_i)
        else:
            encryption_table = generate_encryption_key_matrix(key,alphabet_list_j)
        encrypted_text_array = Playfair_Cipher_Encrypt(encryption_table,grouped_input)
        encrypted_text = ''
        for i in range(len(encrypted_text_array)):
            encrypted_text += encrypted_text_array[i]
    # TAMBAH JENIS CIPHER LAIN

    # Di sini intinya udah harus ada encrypted_text dari setiap jenis cipher
    label=Label(menu, text="Ciphertext: " + encrypted_text, font=("Courier 22 bold"), wraplength= 450)
    label.pack(pady=20)

    label=Label(menu, text="Simpan ciphertext dalam file eksternal?", font=("Courier 16 bold"), wraplength=450)
    label.pack(pady=20)

    button = ttk.Button(menu, text= "Simpan",width= 20, command = lambda: save_text(menu, encrypted_text))
    button.pack(pady=20)

    button = ttk.Button(menu, text= "Tidak Simpan",width= 20, command = lambda: start_menu(menu))
    button.pack(pady=20)

def show_decrypted_text(menu, text, key, cipher_type):
    if (cipher_type == 'playfair'):
        decrypted_text_array = Playfair_Cipher_Decrypt(text, key)
        decrypted_text = ''
        for i in range(len(decrypted_text_array)):
            decrypted_text += decrypted_text_array[i]
    # TAMBAH JENIS CIPHER LAIN

    # Di sini intinya udah harus ada decrypted_text dari setiap jenis cipher
    label=Label(menu, text="Plaintext: " + decrypted_text, font=("Courier 22 bold"), wraplength= 450)
    label.pack(pady=20)

    label=Label(menu, text="Simpan plaintext dalam file eksternal?", font=("Courier 16 bold"), wraplength=450)
    label.pack(pady=20)

    button = ttk.Button(menu, text= "Simpan",width= 20, command = lambda: save_text(menu, decrypted_text))
    button.pack(pady=20)

    button = ttk.Button(menu, text= "Tidak Simpan",width= 20, command = lambda: start_menu(menu))
    button.pack(pady=20)

# Fungsi yang memunculkan window baru untuk playfair cipher
def playfair_cipher_window_start(menu):
    menu_playfair = Tk()
    menu.destroy()
    window_setting(menu_playfair)
    # Teks
    label=Label(menu_playfair, text="Apa yang mau dilakukan? \n 1. Enkripsi Text \n 2. Dekripsi Text \n", font=("Courier 15 bold"))
    label.pack()
    # Entry widget untuk input user
    menu_input= Entry(menu_playfair, width= 5)
    menu_input.focus_set()
    menu_input.pack()

    #CTombol untuk submit
    button = ttk.Button(menu_playfair, text= "Submit",width= 20, command = lambda: check_input(menu_playfair, menu_input.get(), "playfair"))
    button.pack(pady=20)
# Fungsi yang memunculkan window enkripsi/dekripsi tergantung input user
def playfair_cipher_menu(menu, menu_input):
    # user pilih enkripsi playfair cipher
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
        button = ttk.Button(menu_enkripsi, text= "Submit",width= 20, command = lambda: check_input(menu_enkripsi, menu_input.get(), "playfair_enkripsi"))
        button.pack(pady=20)
    # user pilih dekripsi playfair cipher
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
        button = ttk.Button(menu_dekripsi, text= "Submit",width= 20, command = lambda: check_input(menu_dekripsi, menu_input.get(), "playfair_dekripsi"))
        button.pack(pady=20)
# Fungsi enkripsi playfair
def playfair_cipher_enkripsi(menu, input_type):
    if (input_type == '1'):
        menu_enkripsi_1 = Tk()
        menu_enkripsi_1.geometry("500x500")
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

        button = ttk.Button(menu_enkripsi_1, text= "Simpan",width= 20, command = lambda: show_encrypted_text(menu_enkripsi_1, menu_input_teks.get().lower(), menu_input_key.get().lower(), 'playfair'))
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

        button = ttk.Button(menu_enkripsi_2, text= "Simpan",width= 20, command = lambda: show_encrypted_text(menu_enkripsi_2, text, menu_input.get().lower(), 'playfair'))
        button.pack(pady=20)
# Fungsi dekripsi playfair
def playfair_cipher_dekripsi(menu, input_type):
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

        button = ttk.Button(menu_dekripsi_1, text= "Simpan",width= 20, command = lambda: show_decrypted_text(menu_dekripsi_1, menu_input_teks.get().lower(), menu_input_key.get().lower(), 'playfair'))
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

        button = ttk.Button(menu_dekripsi_2, text= "Simpan",width= 20, command = lambda: show_decrypted_text(menu_dekripsi_2, text, menu_input.get().lower(), 'playfair'))
        button.pack(pady=20)

# Start
menu = Tk()
start_menu(menu)
menu.mainloop()

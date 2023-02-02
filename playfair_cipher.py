# Playfair Cipher

# Dalam list alfabet ini dibuang huruf 'j' agar terdapat 25 huruf
alphabet_list_j = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# Jika dalam kalimat/key terdapat huruf 'j', yang dihapus adalah huruf 'i' karena posisinya di matriks akan sama
alphabet_list_i = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']

# Menghilangkan spasi pada input
def remove_space(input):
    removed_space = ""
    # removed_space akan berisi kalimat input tanpa spasi
    for i in input:
        if i in alphabet_list_i or i in alphabet_list_j:
            removed_space += i 
    return removed_space

# Mengelompokan 2 karakter pada kalimat, lalu menambahkan filler apabila kedua huruf sama atau hanya tersisa satu huruf saja
def group_fill(input):
    final_input = []
    k = len(input)
    current_index = 0
    while (current_index < k):
        # Jika belum sampai akhir kalimat, grouping dilakukan secara normal
        if (current_index != k-1):
            # Jika kedua huruf beda, digabungkan
            if (input[current_index] != input[current_index+1]):
                final_input.append(input[current_index] + input[current_index+1])
                current_index += 2
            # Jika kedua huruf sama, huruf pertama digabung dengan huruf "x"
            else:
                final_input.append(input[current_index] + "x")
                current_index += 1
        # Jika sisa satu karakter terakhir, digavung dengan huruf "z"
        else:
            final_input.append(input[current_index] + "z")
            current_index += 1
    return final_input

# Membuat matriks 5x5 kunci enkripsi
def generate_encryption_key_matrix(key, alphabet_list):
    # input_letters berisi semua karakter/huruf yang terdapat pada kunci enkripsi
    input_letters = []
    for i in key:
        if i not in input_letters:
            input_letters.append(i)
 
    mixed_letters = []
    # Menambahkan semua karakter dari key ke dalam mixed_letters
    for i in input_letters:
        if i not in mixed_letters:
            mixed_letters.append(i)
    # Menambahkan sisa karakter dari alfabet ke dalam mixed_letters
    for i in alphabet_list:
        if i not in mixed_letters:
            mixed_letters.append(i)
 
    matrix = []
    while mixed_letters != []:
        # Menambahkan 5 baris pada matriks sejumlah 5 karakter
        matrix.append(mixed_letters[:5])
        mixed_letters = mixed_letters[5:]
 
    return matrix

# Mengembalikan indeks dimana ditemukan elemen input pada matriks
def search_matrix(matrix, element):
    for i in range(5):
        for j in range(5):
            if (matrix[i][j] == element):
                return i,j

# Fungsi Enkripsi
def Playfair_Cipher_Encrypt(encryption_matrix,input):
    Encrypted_Text = []
    for i in range(0, len(input)):
        first_letter = input[i][0]
        second_letter = input[i][1]
        row_first_letter, column_first_letter = search_matrix(encryption_matrix, first_letter)
        row_second_letter, column_second_letter = search_matrix(encryption_matrix, second_letter)
        # Enkripsi apabila kedua huruf terdapat pada baris yang sama di tabel enkripsi
        if (row_first_letter == row_second_letter):
            # Apabila karakter terdapat pada kolom terkanan matriks, maka huruf enkripsi diambil dari kolom paling kiri
            encrypted_first_letter = encryption_matrix[row_first_letter][(column_first_letter + 1)%5]
            encrypted_second_letter = encryption_matrix[row_second_letter][(column_second_letter + 1)%5]
        
        # Enkripsi apabila kedua huruf terdapat pada kolom yang sama di tabel enkripsi
        elif (column_first_letter == column_second_letter):
            # Apabila karakter terdapat pada baris terbawah matriks, maka huruf enkripsi diambil dari baris paling atas
            encrypted_first_letter = encryption_matrix[(row_first_letter+1)%5][column_first_letter]
            encrypted_second_letter = encryption_matrix[(row_second_letter+1)%5][column_second_letter]
        
        # Enkripsi apabila kedua huruf terdapat pada kolom dan baris yang berbeda di tabel enkripsi
        else:
            encrypted_first_letter = encryption_matrix[row_first_letter][column_second_letter]
            encrypted_second_letter = encryption_matrix[row_second_letter][column_first_letter]

        grouped_encrypted_cipher = encrypted_first_letter + encrypted_second_letter
        Encrypted_Text.append(grouped_encrypted_cipher)
    # Menambahkan huruf j di akhir ciphertext agar dapat diketahui list alphabet mana yang perlu dipakai pada dekripsi
    for i in range(len(input)):
        if ("j" in input[i][0] or "j" in input[i][1]):
            Encrypted_Text.append("j")
            break
    return Encrypted_Text

# Fungsi Dekripsi
def Playfair_Cipher_Decrypt(encrypted_text, key):
    removed_space_key = remove_space(key).lower()
    removed_space_encrypted_text = remove_space(encrypted_text).lower()
    if (removed_space_encrypted_text[len(removed_space_encrypted_text)-1] == "j"):
        removed_space_encrypted_text = removed_space_encrypted_text[:len(removed_space_encrypted_text)-1]
        decryption_matrix = generate_encryption_key_matrix(removed_space_key,alphabet_list_i)
    else:
        if ("j" in removed_space_key):
            decryption_matrix = generate_encryption_key_matrix(removed_space_key,alphabet_list_i)
        else:
            decryption_matrix = generate_encryption_key_matrix(removed_space_key,alphabet_list_j)
    final_encrypted_text = []
    k = len(removed_space_encrypted_text)
    for i in range(0,k,2):
        final_encrypted_text.append(removed_space_encrypted_text[i] + removed_space_encrypted_text[i+1])
    Decrypted_Text = []
    for i in range(0, len(final_encrypted_text)):
        first_letter = final_encrypted_text[i][0]
        second_letter = final_encrypted_text[i][1]
        row_first_letter, column_first_letter = search_matrix(decryption_matrix, first_letter)
        row_second_letter, column_second_letter = search_matrix(decryption_matrix, second_letter)
        # Dekripsi apabila kedua huruf terdapat pada baris yang sama di tabel enkripsi
        if (row_first_letter == row_second_letter):
            # Apabila karakter terdapat pada kolom terkiri matriks, maka huruf dekripsi diambil dari kolom paling kanan
            if (column_first_letter == 0):
                column_first_letter += 5
            if (column_second_letter == 0):
                column_second_letter += 5
            decrypted_first_letter = decryption_matrix[row_first_letter][column_first_letter - 1]
            decrypted_second_letter = decryption_matrix[row_second_letter][column_second_letter - 1]
        
        # Dekripsi apabila kedua huruf terdapat pada kolom yang sama di tabel enkripsi
        elif (column_first_letter == column_second_letter):
            # Apabila karakter terdapat pada baris teratas matriks, maka huruf dekripsi diambil dari baris paling bawah
            if (row_first_letter == 0):
                row_first_letter += 5
            if (row_second_letter == 0):
                row_second_letter += 5
            decrypted_first_letter = decryption_matrix[row_first_letter-1][column_first_letter]
            decrypted_second_letter = decryption_matrix[row_second_letter-1][column_second_letter]
        
        # Dekripsi apabila kedua huruf terdapat pada kolom dan baris yang berbeda di tabel dekripsi
        else:
            decrypted_first_letter = decryption_matrix[row_first_letter][column_second_letter]
            decrypted_second_letter = decryption_matrix[row_second_letter][column_first_letter]
        if (decrypted_second_letter == 'x' or decrypted_second_letter == 'z'):
            # Jika huruf kedua adalah huruf 'x' atau 'z', kemungkinan besar itu tidak termasuk dalam teks original sehingga dihapus
            decrypted_second_letter = ''
        grouped_decrypted_cipher = decrypted_first_letter + decrypted_second_letter
        Decrypted_Text.append(grouped_decrypted_cipher)
    return Decrypted_Text
    
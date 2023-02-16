string_text = ''
            # Mengonversi data biner ke bentuk decimal, lalu ke string
            for i in range(0, len(bin_text), 7):
                temp = int(bin_text[i:i + 7])
                decimal = Binary_to_Decimal(temp)
                string_text += chr(decimal)
            return string_text
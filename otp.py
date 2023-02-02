from Tucil1 import *
import random
import string
import os


def create_otp_key(text):
    panjang = len(text)
    list_huruf = string.ascii_lowercase
    random_key = ''
    for i in range(panjang):
        random_key += random.choice(list_huruf)
    return random_key

def create_otp_file(key):
    text_file = open("./otp_key.txt", "w")
    text_file.write(key)
    text_file.close()

def delete_otp_file():
    os.remove("./otp_key.txt")


 
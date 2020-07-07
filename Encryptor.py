import base64
import os
import time

from cryptography.fernet import Fernet


def encrypt():
    input_file = input("Enter file location ")
    output_file = input("Enter output file location ")

    # Getting filename from path
    inp = os.path.basename(input_file)
    filename, file_exten = os.path.splitext(inp)

    # Reading the file and converting to base64 format

    try:
        with open(input_file, "rb") as imgf:
            str = base64.b64encode(imgf.read())
        imgf.close()
    except IOError:
        print("There's some problem reading the file ")

    print("File found....")
    time.sleep(1)
    # using a common key for all
    key = b'lB2vMyAo_6ZbVL4BQfR81S_pFg2jOEvvlsMzX6cWgyI='

    # We can also create random keys everytime and store the key in a separate file
    # to be used by the corresponding decryptor
    # key=Fernet.generate_key()

    f = Fernet(key)
    print("Encrypting...")
    # Encrypting...
    token = f.encrypt(str)
    for i in range(5):
        print('. ', end="")
        time.sleep(0.5)
    print()
    print("Encrypted ")
    time.sleep(1)
    print("Writing to file at " + output_file + "\\" + filename + ".key")

    try:
        with open(output_file + "\\" + filename + ".key", "wb") as outf:
            outf.write(token)
        outf.close()
    except IOError:
        print("There's some problem writing to the file")
        return

    time.sleep(2)
    print("Done")


encrypt()
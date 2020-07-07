import base64
import os
import time

from cryptography.fernet import Fernet


def decrypt():
    key = b'lB2vMyAo_6ZbVL4BQfR81S_pFg2jOEvvlsMzX6cWgyI='
    f = Fernet(key)

    s = input("Enter .key file location ")
    loc = input("Enter location where you want to save the file ")
    print("Reading encrypted data ... ")
    inp = os.path.basename(s)
    filename, file_exten = os.path.splitext(inp)
    time.sleep(1)
    try:
        with open(s, "rb") as imgen:
            tok = imgen.read()
        imgen.close()
    except:
        print("Can't read the file")
        return

    print("Decrypting Data")

    for i in range(5):
        print('. ', end="")
        time.sleep(0.500)

    decrypted_data = f.decrypt(tok)
    print()
    print("Storing data to : " + loc + "\\" + filename + "_dcrptd.png")
    time.sleep(1)
    try:
        fh = open(loc + "\\" + filename + "_dcrptd.png", "wb")
        fh.write(base64.b64decode(decrypted_data))
        fh.close()
    except:
        print("Can't read the file")

    print("Done")


decrypt()
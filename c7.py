# References for challenge 7: 
# https://en.wikipedia.org/wiki/Advanced_Encryption_Standard 
# http://blog.joshuahaddad.com/cryptopals-challenges-7-8/
# https://techtutorialsx.com/2018/04/09/python-pycrypto-using-aes-128-in-ecb-mode/
# https://laconicwolf.com/2018/07/22/cryptopals-challenge-7-implement-aes-in-ecb-mode-with-python/
# https://www.adamberent.com/wp-content/uploads/2019/02/AESbyExample.pdf 

# my code 
# c7.py
# text is in c7file
# located in the same directory as this script file
"""
A text file has been encrypted using AES-128 in ECB mode
via the key "YELLOW SUBMARINE"
(all caps, space matters, ignore quote marks)

decrypt it
- write your own code, don't use a command line tool
- apparently this will be useful later on in cryptopals
"""
import base64
from Crypto.Cipher import AES

# get the text into a variable
# and convert to bytes
with open('c7file') as inp:
    text = base64.b64decode(inp.read())
print(text) # check that it worked: it did

def aes_ecb_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return(cipher.encrypt(plaintext))

def aes_ecb_decrypt(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    return(cipher.decrypt(ciphertext))

cle="YELLOW SUBMARINE"
print(aes_ecb_decrypt(cle, text))

new = aes_ecb_decrypt(cle, text)

# turn new thing back to hex string from bytes
new_hex = new.hex()

# write solution to file
with open("newtext.txt", "w") as output:
    output.write(new_hex)

# the encrypt it again :)
new_byt = base64.b64decode(new_hex)
print(aes_ecb_encrypt(new_byt, cle))

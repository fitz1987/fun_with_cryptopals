# set 1 challenge 8 solution
"""
In this file are a bunch of hex-encoded ciphertexts.

One of them has been encrypted with ECB.

Detect it.

Remember that the problem with ECB is that it is stateless and deterministic;
the same 16 byte plaintext block will always produce the same 16 byte
ciphertext.
"""

# what i'm learning here is that we don't want patterns in our ciphertext
# discussion refernced: http://blog.joshuahaddad.com/cryptopals-challenges-7-8/

import base64
from Crypto.Cipher import AES

def find_ecb(ciphertext):
    blocks = [ciphertext[i*16:(i+1)*16] for i in range(int(len(ciphertext)/16))]
    # set: give the unique values only in an array
    # use to detect duplicates in the blocks
    duplicates = len(blocks) - len(set(blocks))
   #print("num dups is: ", duplicates)
    if (duplicates >= 1):
        return True, duplicates
    else:
        return False, 0

duplicate_counter = 0
line_counter = 0

with open('c8file') as f:
# check each line of a file for duplicates
    for line in f:
        line_counter += 1
        ECB, duplicates = find_ecb(line)

        if (ECB != 0):
            #AES_Cipher = cipher
            duplicate_counter = duplicates
            line_number = line_counter
            line_text = line
    print("****** the encrypted line number is*****", line_number)
    print("****** the encrypted line is******", line)

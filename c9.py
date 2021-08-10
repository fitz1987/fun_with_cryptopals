# s9.py
# solution to cryptopals set 2 challenge 1, aka challenge #9

"""
A block cipher transforms a fixed-sized block (usually 8 or 16 bytes)
 of plaintext into ciphertext.
 But we almost never want to transform a single block;
 we encrypt irregularly-sized messages.

One way we account for irregularly-sized messages is by padding,
creating a plaintext that is an even multiple of the blocksize.
The most popular padding scheme is called PKCS#7.

So: pad any block to a specific block length,
by appending the number of bytes of padding to the end of the block.
For instance,

"YELLOW SUBMARINE"
... padded to 20 bytes would be:

"YELLOW SUBMARINE\x04\x04\x04\x04"
"""

def pad_text():
    inp = input("Enter the text to pad:")
    inp = bytes(inp, 'utf=8')
    text = bytearray(inp)

    pad_length = input("Enter length to pad text to:")
    pad_length = int(pad_length)

    if (len(text) < pad_length):
        padding =  pad_length - len(text)
        print(padding)
    text += bytes([padding])

    return text

print(pad_text())

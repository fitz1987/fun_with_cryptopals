# c5.py
print("~~~~~Solution to Cryptopals Set 1 Challenge 5~~~~~")
import sys
import binascii
"""
Challenge 5:
take this string:
Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal

and Encrypt it, under the key "ICE", using repeating-key XOR.

repeating key xor sequentially applies each byte of the key to each byte of then
string to be encrypted:
 the first byte of plaintext will be XOR'd against I, the next C, the next E,
then I again for the 4th byte, and so on.

"""
#outine
# save the strings as a byte string!!!
# this will save SO much time!!
# original string and key from exercise:
#str = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
#key = b"ICE"

# generalizing it
# take input from a file, save to str for the string and key for the key
print("Put your text to be encrypted in a file called file.")
print("Enter yes if this file is ready; code will proceed.")
print("Enter nope if it is not; code will exit.")
answer = input("Ready to go?")
if (answer != 'yes'):
    sys.exit("input file not ready. Later gator!")

# now make the iputs for the function
file = open("c6file", "r")
list_of_strings = [(line.strip()).split() for line in file]
file.close()

key1 = input("Please type in your key in plain ascii characters:")
key = key1.encode('utf-8')
#print(key)

#print(list_of_strings)
def keyxor(string, key):
    i = 0
    soln = []
    for i in range (0, len(string)):
        soln.append(string[i] ^ key[i % len(key)])
    return soln

for i in range(len(list_of_strings)):
    text = list_of_strings[i]
    text_str = ''.join(text)
    byt_text = text_str.encode('utf-8')
    solution = keyxor(byt_text, key)
#print(solution)

# write output to a file called out.txt
with open("out.txt", 'w') as f:
    print(solution, file=f)
print("The encoded text has been written to the file out.txt.")
print("Note: if you run this program again, out.txt will be overwritten.")
print("If saving the result is important to you, make sure to rename it.")

# now change it back just to be sure
backwards = keyxor(solution, key)
original = []
for i in range (0, len(backwards)):
    original.append(chr(backwards[i]))
print("just to double check, the original text was:", original)

final = ''.join(str(element) for element in original)
#print(final)

#print("The solution is", binascii.hexlify(bytearray(ans)))

# for checking solution against cryptopals string
#check = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
#print("The solution should match this: ", check)

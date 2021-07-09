# cleaned up solutions to cryptopals early exercises for github

# exercise 1
print("Solution to set 1 challenge 1:")
print("  ")
import codecs

def to_b64(str_hex):
    str_b64 = codecs.encode(codecs.decode(str_hex, 'hex'), 'base64').decode()
    return str_b64
hex_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

print(to_b64(hex_str))


print("  ")
print("Solution to set 1 challenge 2:")

# notes: xor: one but not both. if a and b are different,returns 1. if same, returns 0

# import binascii
# # test on the hex string from challenge 1: convert it to hex and you get
def to_ascii(str_hex):
    str_ascii = codecs.decode(str_hex, 'hex')
    return str_ascii

# original hex values
hex1 = '1c0111001f010100061a024b53535009181c'
hex2 = '686974207468652062756c6c277320657965'


# convert hex strings to integers
base = 16 # for hex
int1 = int(hex1, base)
int2 = int(hex2, base)

#convert integers to binary
bin1 = bin(int1)[2:]
bin2 = bin(int2)[2:]

goal = len(bin2)
bin1 = bin1.zfill(goal)
bin2 = bin2.zfill(goal)

# xor
soln = [int(bi1) ^ int(bi2) for bi1, bi2 in zip(bin1, bin2)]


string_soln = "".join([str(bits) for bits in soln])

# convert xor's binary output to hex
print(hex(int(string_soln, 2))[2:])

print("For comparison, answer should be: ")
print("746865206b696420646f6e277420706c6179")
print("   ")
print("  ")

print("Solution to challenge 3 of set 1")
initial_hex = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
print("Initial hex string is: ")
print(initial_hex)

text = bytearray.fromhex(initial_hex)
#print(text)

def keyxor(inp, key):
    out = b''
    for byte in inp:
        out += bytes([byte ^ key])
    return out


# stage two: make it rank the solutions based on how english-y they feel
# compare to character frequency in english and rank
# then print out the best one
def vibe_check(byt_str):
        char_freq = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
        lower = byt_str.lower()
        return sum([char_freq.get(chr(byte), 0) for byte in lower])

maybes = []
for i in range(256):
    message = keyxor(text, i)
    rank = vibe_check(message)
    vals = {
            'coded message': message,
            'rank': rank,
            'xor key': i
            }
    maybes.append(vals)
    winner = sorted(maybes, key = lambda x: x['rank'], reverse=True)[0]
print("Solutions is: ", winner['coded message'])


# References: read these for algorithm help
# https://laconicwolf.com/2018/05/29/cryptopals-challenge-3-single-byte-xor-cipher-in-python/
# https://cryptik.io/83/cryptopals-write-up-set-1-challenge-3/ 

# new c6.py because too much mess in old one

"""
The file saved as "c6file" as been encrypted with a repeating key XOR.
decrypt it
"""
import base64
import numpy as np

print("~~~~~Solution to Cryptopals Set 1 Challenge 6~~~~~")

# function to calculate hamming distance between two strings
def hamming_string(str1, str2):
    dist = 0
    for i in range(0, len(str1)):
        if ((str1[i] != str2[i])):
            dist += 1
    return dist

text1 = b'this is a test'
text2 = b'wokka wokka!!!'

def string_to_byt(text):
    byt = [byte for byte in text]
    return byt

test1 = string_to_byt(text1)
test2 = string_to_byt(text2)

#print(test1)

def hamming(byt1, byt2):
    dist = 0
    xor_soln = [b1 ^ b2 for b1, b2 in zip(byt1, byt2)]
    for byte in xor_soln:
        dist += sum([1 for bit in bin(byte) if bit =='1'])
    return dist


# testing hamming distance function on the test strings
#print("for strings: ", text1, " and ", text2)
print("For test strings, bitwise Hamming distance is: ", hamming(test1, test2))
if (hamming(test1, test2)) == 37:
    print("so far, so good")


# single character xor function, from previous cryptopals
def keyxor(inp, key): # inp is a string
    output = b''
    for byte in inp:
        output += bytes([byte ^ key])
    return output

# vibe check: rank soltuions by how "english-y" their vibes are
def vibe_check(byt_str):
        freq = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .10000
    }
        return sum([freq.get(chr(byte), 0) for byte in byt_str.lower()])

# break single character xor
def single_char_xor(coded_text):
   potential_solns = []
   for key_value in range(256):
#        check all 255 characters
       decoded = keyxor(coded_text, key_value)
       score = vibe_check(decoded)
       data = {#'message' : coded_text,
               'score' : score,
               'key' : key_value }
       potential_solns.append(data)
       # return sorted(potential_solns, key = lambda x: x['score'], reverse=True)[0]
   ans = sorted(potential_solns, key = lambda x: x['score'], reverse=True)[0]
   return ans['key']

# now move on to actual encrypted text
# get the file contents
with open('c6file') as inp:
    text = base64.b64decode(inp.read())
    hextext = inp.read()

# find likely key size for the encrypted text
def find_keysize(txt:bytes):
    # did some reading and apparently minimized normalized hamming distance
    # will give you the key length. which i already knew?
    # but seeing graphs made it click somehow.
    print("...finding likely key size, this takes ~6 seconds.")
    current_min = 10
    keysize = 2
    klist =[]
    scorelist = []
    for ksize in range(2, 41): # using the range given in problem
        blocks = [txt[i:i+ksize] for i in range(0, len(txt), ksize)]
        scores = []
        for i in range(0, len(blocks) -1, 1):
            for j in range(i+1, len(blocks), 1):
                score = hamming(blocks[i], blocks[j]) / ksize
                scores.append(score)
        #print("for ksize: ", ksize, "scores are:", scores)
        avg_score = (sum(scores) / len(scores)) # avg score for that ksize
        del scores
        # compare to min:
        if avg_score < current_min:
            current_min, keysize = avg_score, ksize
        scorelist.append(avg_score)
        klist.append(ksize)
    #print("score list:", scorelist)
    #print("~~~~~~")
    #print("ksize list: ", klist)
    soln = min(scorelist)
    index = scorelist.index(min(scorelist))
    return (index +2)

keysize = find_keysize(text)
print("the xor key size is probably: ", keysize)

def make_blocks(n, txt): # n = keylength, txt = textfile
    # make blocks of keysize keylength
    blocks_array = [txt[i:i+n] for i in range(0, len(txt), n)]
    return blocks_array

blocks = make_blocks(keysize, text)
print("length of one item in block array is: ", len(blocks[0]))
if (len(blocks[1]) == 29):
    print("so far, so good")
#    print("test block contents: ", blocks[0])
    #print(text)
# this section is commented out mostly
# but it helped me to figure out how to transpose blocks
# and that the last block needed to get extra 0's added
count = 0
for element in blocks:
    count += 1
#print("there are this number of blocks:", count)
#print("length of last block:", len(blocks[99]))
#print(blocks[99])
blocks[99] += b'000000000000000000000000'
#print("length of last block:", len(blocks[99]))
#print(blocks[99])
#blocks_tr = np.transpose(blocks)
#i'm ingnoring the last block for now
# bc i feel like all the zeros would mess with the vibe check??
blocks_tr = [[blocks[j][i] for j in range(0, count-1)] for i in range(0,29)]
#print("first transposed block:   ", blocks_tr[0])
#print("number of transposed blocks minus last one is: ", len(blocks_tr))
#print("number of elements in each transposed block:" ,len(blocks_tr[0]))

def find_key_by_block(transposed_block_list, key_length):
    key_text = []
    for element in transposed_block_list:
        # turn it into bytes
        ele = bytes(element)
        key_text.append(single_char_xor(ele))
    return key_text

#print(find_key_by_block(blocks_tr, keysize))
key_text_nums = find_key_by_block(blocks_tr, keysize)
#print(key_text_nums)
key_text_lel = []
for i in range(len(key_text_nums)):
    key_text_lel.append(chr(key_text_nums[i]))
#print(key_text_lel)

key_str = ''
for ele in key_text_lel:
    key_str += ele
print("XOR key is: ", key_str)

# for decoding the message AFTER the key is found
def repeating_xor(blocks_array, key, keysize):
    output_byt = []
    i = 0
    for byte in text:
        output_byt.append(([byte ^ key[i]]))
        if (i +1) == keysize:
            i = 0
        else:
            i += 1
    return output_byt

# make byte key
key_byte = bytes(key_str, 'utf-8')
#print(key_byte)

# decode the message
result = repeating_xor(text, key_byte, keysize)

#print("coded message is: ", result)

len_res = len(result)
# numbers -> ascii
result_ascii = []
for k in range(len_res):
    result_ascii.append(chr(result[k][0]))
print("------------------")
#print(result_ascii)

res_str = ''
for ele in result_ascii:
    res_str += ele
print(res_str)

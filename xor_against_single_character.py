import itertools
import string


"""This program is to find the key and decrypt the message for a given XOR'ed hex string against a single character
    Given Hex string is
    "26294f2e4f222e214f263c4f2029292a3d2a2b4f2e4f292e2c3b4f3827262c274
    f28202a3c4f2e282e26213c3b4f27263c4f26213c3b26212c3b3c4f272a4f3826
    23234f3c2c3d3a3b262126352a4f263b4f2c23203c2a23364f2e212b4f3a21232
    a3c3c4f3b272a4f2a39262b2a212c2a4f263c4f20392a3d38272a23222621284f
    272a4f382623234f3d2a293a3c2a4f3b204f2d2a23262a392a4f263b4f26294f2
    0214f3b272a4f203b272a3d4f272e212b4f272a4f263c4f2029292a3d2a2b4f3c
    20222a3b272621284f3827262c274f2e2929203d2b3c4f2e4f3d2a2e3c20214f2
    9203d4f2e2c3b2621284f26214f2e2c2c203d2b2e212c2a4f3b204f27263c4f26
    213c3b26212c3b3c4f272a4f382623234f2e2c2c2a3f3b4f263b4f2a392a214f2
    0214f3b272a4f3c232628273b2a3c3b4f2a39262b2a212c2a4f3b272a4f203d26
    2826214f20294f22363b273c4f263c4f2a373f232e26212a2b4f26214f3b27263
    c4f382e36"

    Author : Harish Kommineni
    Date : September 1, 2016

"""

# This method is to find the key and decrypt a given cipher text.
def key_decrypt():
    xor_text = '26294f2e4f222e214f263c4f2029292a3d2a2b4f2e4f292e2c3b4f3827262c274f28202a3c4f2e282e26213c3b4f27263c4f26213c3b26212c3b3c4f272a4f382623234f3c2c3d3a3b262126352a4f263b4f2c23203c2a23364f2e212b4f3a21232a3c3c4f3b272a4f2a39262b2a212c2a4f263c4f20392a3d38272a23222621284f272a4f382623234f3d2a293a3c2a4f3b204f2d2a23262a392a4f263b4f26294f20214f3b272a4f203b272a3d4f272e212b4f272a4f263c4f2029292a3d2a2b4f3c20222a3b272621284f3827262c274f2e2929203d2b3c4f2e4f3d2a2e3c20214f29203d4f2e2c3b2621284f26214f2e2c2c203d2b2e212c2a4f3b204f27263c4f26213c3b26212c3b3c4f272a4f382623234f2e2c2c2a3f3b4f263b4f2a392a214f20214f3b272a4f3c232628273b2a3c3b4f2a39262b2a212c2a4f3b272a4f203d262826214f20294f22363b273c4f263c4f2a373f232e26212a2b4f26214f3b27263c4f382e36'
    keys_frequency = [chr(x) for x in range(256)]
    scores = score_decodings(keys_frequency, ratio_count, xor_text)
    print ("score: %.4f key: '%s' plain_text: %s" % scores[0])

# This method returns list of decodings that are counted
def score_decodings(solutions, score_count, text):
    counts = []
    for key in solutions:
        plain_text = xor_data(key, text)
        score = score_count(plain_text)
        counts.append((score, key, plain_text))
    return sorted(counts, reverse=True)

# xor key with data, repeating key as and when necessary
def xor_data(solution, text):
    if len(solution) == 1:
        key = ord(solution)
        return ''.join(chr(ord(x) ^ key) for x in text)
    series = itertools.cycle(solution)
    return ''.join(chr(ord(x) ^ ord(y)) for x,y in itertools.izip(text, series))

ok = set(string.ascii_letters + ' ')

# ratio of ascii_letters and space to total length of the string
def ratio_count(s):
    count = sum(1 for x in s if x in ok)
    return count / float(len(s))

# Main method for the program to find key and decrypt message
if __name__ == '__main__':
    key_decrypt()
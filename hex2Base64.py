
"""This is the program to implement hex to base 64 conversion with out using the in built functions in Python
    Author  : Harish Kommineni
    Date    : September 1, 2016
"""

# This method imlements the aloorithm of hex to base 64 conversion
def hex_base64(s, padding = False):
    ascii_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    b64_value = "="
    return_value = ""
    left = 0
    for i in range(0, len(s)):
        if left == 0:
            return_value += ascii_letters[ord(s[i]) >> 2]
            left = 2
        else:
            if left == 6:
                return_value += ascii_letters[ord(s[i - 1]) & 63]
                return_value += ascii_letters[ord(s[i]) >> 2]
                left = 2
            else:
                index1 = ord(s[i - 1]) & (2 ** left - 1)
                index2 = ord(s[i]) >> (left + 2)
                index = (index1 << (6 - left)) | index2
                return_value += ascii_letters[index]
                left += 2
    if left != 0:
        return_value += ascii_letters[(ord(s[len(s) - 1]) & (2 ** left - 1)) << (6 - left)]
    if(padding):
        for i in range(0, (4 - len(return_value) % 4) % 4):
            return_value += b64_value
    return return_value


# Main method for the program Hex to base64 conversion
if __name__ == '__main__':
    hex = hex_base64(
        "26294f2e4f222e214f263c4f2029292a3d2a2b4f2e4f292e2c3b4f3827262c274f28202a3c4f2e282e26213c3b4f27263c4f26213c3b26212c3b3c4f272a4f382623234f3c2c3d3a3b262126352a4f263b4f2c23203c2a23364f2e212b4f3a21232a3c3c4f3b272a4f2a39262b2a212c2a4f263c4f20392a3d38272a23222621284f272a4f382623234f3d2a293a3c2a4f3b204f2d2a23262a392a4f263b4f26294f20214f3b272a4f203b272a3d4f272e212b4f272a4f263c4f2029292a3d2a2b4f3c20222a3b272621284f3827262c274f2e2929203d2b3c4f2e4f3d2a2e3c20214f29203d4f2e2c3b2621284f26214f2e2c2c203d2b2e212c2a4f3b204f27263c4f26213c3b26212c3b3c4f272a4f382623234f2e2c2c2a3f3b4f263b4f2a392a214f20214f3b272a4f3c232628273b2a3c3b4f2a39262b2a212c2a4f3b272a4f203d262826214f20294f22363b273c4f263c4f2a373f232e26212a2b4f26214f3b27263c4f382e36",
        False)
    print("Hexadecimal to Base64 conversion of a String is \n", hex)




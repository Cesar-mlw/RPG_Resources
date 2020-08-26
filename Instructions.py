import sys, time, random
def decoder(bin):
    binary_values = bin.split()
    decoded_text = ""
    for bv in binary_values:
        number = int(bv, 2)
        ascii_char = chr(number)
        decoded_text += ascii_char
    return decoded_text

typing_speed = 250

def slow_type(t):
    for letter in t:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*10/typing_speed)
###########################################################################################################################################################

text = "00001010 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 01000010 01000101 01000111 01000111 01001001 01001110 01001001 01001110 01000111 00100000 01001111 01000110 00100000 01001101 01000101 01010011 01010011 01000001 01000111 01000101 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00001010 01000111 01101111 01101111 01100100 00100000 01000101 01110110 01100101 01101110 01101001 01101110 01100111 00100000 01001101 01110011 00101110 00100000 01001100 01101001 01101110 01100001 00001010 00001010 01011001 01101111 01110101 00100000 01110010 01100101 01100001 01101100 01101100 01111001 00100000 01110100 01101000 01101001 01101110 01101011 00100000 01110100 01101000 01100001 01110100 00100000 01111001 01101111 01110101 00100000 01100011 01100001 01101110 00100000 01110010 01110101 01101110 00100000 01100001 01110111 01100001 01111001 00100000 01100110 01101111 01110010 01100101 01110110 01100101 01110010 00111111 00100000 01010111 01100101 00100000 01101011 01101110 01101111 01110111 00100000 01111001 01101111 01110101 00100000 01100001 01110010 01100101 00100000 01101000 01101001 01100100 01101001 01101110 01100111 00100000 01111001 01101111 01110101 01110010 00100000 01100110 01100001 01110100 01101000 01100101 01110010 00101100 00100000 01100001 01101110 01100100 00100000 01110111 01100101 00100111 01110010 01100101 00100000 01100111 01100101 01110100 01110100 01101001 01101110 01100111 00100000 01100011 01101100 01101111 01110011 01100101 00100000 01110100 01101111 00100000 01101000 01101001 01101101 00101110 00001010 00001010 01010000 01100001 01110010 01101001 01110011 00100000 01101001 01110011 00100000 01100001 00100000 01101100 01101111 01110110 01100101 01101100 01111001 00100000 01100011 01101001 01110100 01111001 00101100 00100000 01101001 01110011 01101110 00100111 01110100 00100000 01101001 01110100 00111111 00001010 00001010 00001010 00001010 01010111 01100101 00100000 01110111 01101001 01101100 01101100 00100000 01100010 01100101 00100000 01101001 01101110 00100000 01110100 01101111 01110101 01100011 01101000 00100000 01110011 01101111 01101111 01101110 00101110 00001010 00001010 01010011 01100001 01101110 01110100 01101001 01101110 01101111 00100000 01000110 01100001 01101101 01101001 01101100 01111001 00001010 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 01000101 01001110 01000100 00100000 01001111 01000110 00100000 01001101 01000101 01010011 01010011 01000001 01000111 01000101 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011 00100011"

message = decoder(text)

slow_type(message)

# Copy and Paste code on, and press run -> https://repl.it/languages/python3

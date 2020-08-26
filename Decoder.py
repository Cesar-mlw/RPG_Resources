import sys, time, random, base64, re
def binary_decoder(bin):
    binary_values = bin.split()
    decoded_text = ""
    for bv in binary_values:
        number = int(bv, 2)
        ascii_char = chr(number)
        decoded_text += ascii_char
    return decoded_text

def cheddar_decorder(string):
    message = string.split(";")
    message = message[:-1]
    decoded_message = ""
    for l in message:
        number = int(str(l).strip())
        ascii_char = chr(number)
        decoded_message += ascii_char
    return decoded_message

def encoder(string):
    values = string.split()
    encoded_text = ""
    for l in values:
        encoded_text += str(int(l, 2)) + ";"
    return encoded_text

typing_speed = 250

def slow_type(t):
    for letter in t:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*10/typing_speed)
###########################################################################################################################################################

text = open("TWA_Answer.txt", "r").read()


message = encoder(text)

file = open("TWA_Answer.txt", "w")

file.write(message)

# Copy and Paste code on, and press run -> https://repl.it/languages/python3

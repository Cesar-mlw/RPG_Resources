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

text = open("TWA_Answer.txt", "r").read()

message = decoder(text)

slow_type(message)

# Copy and Paste code on, and press run -> https://repl.it/languages/python3

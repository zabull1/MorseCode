text = input("Enter a text")
morse_code = ''

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

for a in text:
    for b in MORSE_CODE_DICT.keys():
        if a == b:
            morse_code = morse_code + MORSE_CODE_DICT[b] +" "

print(morse_code)

decipher = morse_code.split(" ")


for i,d in enumerate(decipher):
    for j,b in MORSE_CODE_DICT.items():
        if d == b:
            decipher[i] = j

print(''.join(decipher))

"""
while True:
    words = input("Please type in the words you want to encode:").lower()
    if words == "exit":
        break
    encoded_word = ""
    for letter in words:
        if letter == " ":
            encoded_word = encoded_word + word_seperator
        else:
            encoded_word = encoded_word + morse_code[letter] + letter_seperator
    print(f"Morse code:{encoded_word}")
"""

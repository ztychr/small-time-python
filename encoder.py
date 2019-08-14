#!/usr/bin/python3

import sys, getopt

encoding = {'a' : "9aLxO",
            'b' : "StaOL",
            'c' : "piHW8",
            'd' : "4QXBv",
            'e' : "LDkJp",
            'f' : "c0fCS",
            'g' : "iGiZz",
            'h' : "GsT20",
            'i' : "1BWcd",
            'j' : "1LVBz",
            'k' : "ABR9N",
            'l' : "b3tDp",
            'm' : "TL2hv",
            'n' : "uhHnQ",
            'o' : "8XcXH",
            'p' : "leCmS",
            'q' : "KuIfX",
            'r' : "X3ilW",
            's' : "mWnb5",
            't' : "nXZpK",
            'u' : "dQT4L",
            'v' : "DOtQr",
            'w' : "l5uVp",
            'x' : "DbH7V",
            'y' : "Lm8Fq",
            'z' : "Nov2R",
            'æ' : "hjQdG",
            'ø' : "Kafdg",
            'å' : "fQAh6",
            'A' : "4aL1B",
            'B' : "StaOL",
            'C' : "Th80G",
            'D' : "l4B94",
            'E' : "gMO01",
            'F' : "13Pme",
            'G' : "eF103",
            'H' : "G0Qk8",
            'I' : "x73Qe",
            'J' : "3zI8E",
            'K' : "k75Xx",
            'L' : "Gb45p",
            'M' : "5a7ZX",
            'N' : "Df4B6",
            'O' : "rK31M",
            'P' : "Ye75j",
            'Q' : "817xC",
            'R' : "Dok94",
            'S' : "vN88X",
            'T' : "jT36X",
            'U' : "mS54V",
            'V' : "mS54V",
            'W' : "oA49M",
            'X' : "rT13f",
            'Y' : "7A1iH",
            'Z' : "Rd30Q",
            'Æ' : "L6c0z",
            'Ø' : "A7c1T",
            'Å' : "Qg1N2",
            ' ' : "i0DQd"}

decoding = {'9aLxO' : "a",
            'StaOL' : "b",
            'piHW8' : "c",
            '4QXBv' : "d",
            'LDkJp' : "e",
            'c0fCS' : "f",
            'iGiZz' : "g",
            'GsT20' : "h",
            '1BWcd' : "i",
            '1LVBz' : "j",
            'ABR9N' : "k",
            'b3tDp' : "l",
            'TL2hv' : "m",
            'uhHnQ' : "n",
            '8XcXH' : "o",
            'leCmS' : "p",
            'KuIfX' : "q",
            'X3ilW' : "r",
            'mWnb5' : "s",
            'nXZpK' : "t",
            'dQT4L' : "u",
            'DOtQr' : "v",
            'l5uVp' : "w",
            'DbH7V' : "x",
            'Lm8Fq' : "y",
            'Nov2R' : "z",
            'hjQdG' : "æ",
            'Kafdg' : "ø",
            'fQAh6' : "å",
            '4aL1B' : "A",
            'StaOL' : "B",
            'Th80G' : "C",
            'l4B94' : "D",
            'gMO01' : "E",
            '13Pme' : "F",
            'eF103' : "G",
            'G0Qk8' : "H",
            'x73Qe' : "I",
            '3zI8E' : "J",
            'k75Xx' : "K",
            'Gb45p' : "L",
            '5a7ZX' : "M",
            'Df4B6' : "N",
            'rK31M' : "O",
            'Ye75j' : "P",
            '817xC' : "Q",
            'Dok94' : "R",
            'vN88X' : "S",
            'jT36X' : "T",
            'mS54V' : "U",
            'mS54V' : "V",
            'oA49M' : "W",
            'rT13f' : "X",
            '7A1iH' : "Y",
            'Rd30Q' : "Z",
            'L6c0z' : "Æ",
            'A7c1T' : "Ø",
            'Qg1N2' : "Å",
            'i0DQd' : " "}

help = '''
    python3 encoder.py [option] <string> ... [-e] <string> | [-d] <string
    wrap in quotes to encode strings with spaces
    
    -e --encode | encode string
    -d --decode | decode string
        '''

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"he:d:",["ifile=","ofile="])
    except getopt.GetoptError:
        print (help)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(help)
            sys.exit()

        elif opt in ("-e", "--encode"):
            encode = arg
            encode_phrase = []

            for i in list(encode):
                p = encoding[i]
                encode_phrase.append(p)

            print('\n' + 'Encoded string: ' + ''.join(encode_phrase) + '\n')

        elif opt in ("-d", "--decode"):
            decode = arg
            decode_phrase = []
            r = [decode[i:i+5] for i in range(0, len(decode), 5)]

            for i in r:
                p = decoding[i]
                decode_phrase.append(p)

            print('\n' + 'Decoded string: ' + ''.join(decode_phrase) + '\n')

if __name__ == "__main__":
   main(sys.argv[1:])

# old code
'''
def encode():

    encode = input("\nEnter string to encode: ")
    encode_phrase = []

    for i in list(encode):
        p = encoding[i]
        encode_phrase.append(p)

    print('\n')
    print('Encoded string: ' + ''.join(encode_phrase))
def decode():
    decode = input("\nEnter string to decode: ")

    decode_phrase = []

    r = [decode[i:i+5] for i in range(0, len(decode), 5)]

    for i in r:
        p = decoding[i]
        decode_phrase.append(p)

    print('\n')
    print('Decoded string: ' + ''.join(decode_phrase))
'''

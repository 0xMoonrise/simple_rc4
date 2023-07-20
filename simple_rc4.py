#!/usr/bin/env python
import sys
import argparse


def bytes_stream(key):
    key = [ord(char) for char in key]
    stream = [_ for _ in range(256)]
    i = 0
    for j in range(256):
        i = (i + stream[j] + key[j % len(key)]) % 256
        stream[j], stream[i] = stream[i], stream[j]
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (stream[i] + j) % 256
        stream[j], stream[i] = stream[i], stream[j]
        yield stream[(stream[i] + stream[j]) % 256]

def encrypt(text, key):
    text = [ord(char) for char in text]
    bytes = bytes_stream(key)
    return ' '.join([f'{char ^ next(bytes):02X}' for char in text])

def decrypt(bytes, key):
    cipher = [char for char in bytes if char != ' ']
    cipher = map(lambda _: int(f"0x{''.join(_)}", 0), zip(*[iter(cipher)] * 2))
    bytes = bytes_stream(key)
    return "".join([chr(char ^ next(bytes)) for char in cipher])


parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mode", type=str,
                    help="use 'e' to encrypt or 'd' to decrypt a text.")
parser.add_argument("-t", "--text", type=str,
                    help="set the text value.")
parser.add_argument("-k", "--key", type=str,
                    help="set the key value.")
args = parser.parse_args()

match args.mode:
    case 'd':
        if args.text:
            print(decrypt(args.text, args.key))
        else:
            print(decrypt(sys.stdin.read(), args.key).strip())
    case 'e':
        if args.text:
            print(encrypt(args.text, args.key))
        else:
            print(encrypt(sys.stdin.read(), args.key).strip())
    case _:
        print(f'Error, the mode it was not the right one, for help use {sys.argv[0]} -h')

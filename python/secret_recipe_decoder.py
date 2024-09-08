#!/usr/bin/python3
import pydoc
import sys
import os

# Caesar encoding, for use with decoding below
ENCODING = {
    'y': 'a',
    'h': 'b',
    'v': 'c',
    'x': 'd',
    'k': 'e',
    'p': 'f',
    'z': 'g',
    's': 'h',
    'a': 'i',
    'b': 'j',
    'e': 'k',
    'w': 'l',
    'u': 'm',
    'q': 'n',
    'n': 'o',
    'l': 'p',
    'm': 'q',
    'f': 'r',
    'o': 's',
    'i': 't',
    'g': 'u',
    'j': 'v',
    't': 'w',
    'd': 'x',
    'r': 'y',
    'c': 'z',
    '3': '0',
    '8': '1',
    '4': '2',
    '0': '3',
    '2': '4',
    '7': '5',
    '5': '6',
    '9': '7',
    '1': '8',
    '6': '9'
 }

"""An ingredient has an amount and a description.
For example: an Ingredient could have "1 cup" as the amount and "butter" as the description."""
class Ingredient():
    def __init__(self, amount, description) -> None:
        self.amount = amount
        self.description = description


def decode_string(input_string):
    """Given a string named input_string, use the Caesar encoding above to return the decoded string."""
    # TODO: implement me 
    decoded_list = []
    for char in input_string:
        if char == '#':
            decoded_list.append(' ')
        elif char in ENCODING:
            decoded_list.append(ENCODING[char])
        else:
            decoded_list.append(char)
    return ''.join(decoded_list)

def decode_ingredient(line):
    """Given an ingredient, decode the amount and description, and return a new Ingredient"""
    # TODO: implement me

    parts = line.split('#', 1)
    if len(parts) == 2:
        qty_encoded, name_encoded = parts
    else:
        qty_encoded = parts[0]
        name_encoded = ''
    
    qty_decoded = decode_string(qty_encoded)
    name_decoded = decode_string(name_encoded)

    return Ingredient(qty_decoded, name_decoded)

def main():
    """A program that decodes a secret recipe"""
    # TODO: implement me

    with open('secret_recipe.txt', 'r') as file:
        encoded_recipe = file.readlines()

    with open('decoded_recipe.txt', 'w') as output_file:
        for line in encoded_recipe:
            output_file.write(decode_string(line) + '\n')

if __name__ == "__main__":
    main()
#!/usr/bin/python3
"""
printing text
"""

def text_indentation(text):
    """function that prints a text with 2 new lines
    after each of these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == " ":
            if text[i - 1] == "." or text[i - 1] == "?" or text[i - 1] == ":" or text[i - 1] == " ":
                continue
        print(text[i], end='')
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print()
            print()

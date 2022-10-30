#!/usr/bin/env python
# coding: utf-8


def cipher(text, shift, encrypt=True):
    """
    Each letter is replaced by a letter some fixed number of positions down the alphabet

    Parameters
    ----------
    text : string
      The text that we want to encrypt or decrypt.
    shift : integer
      The number of positions down to encrypt or decrpt.
     encrypt : boolean
      True if encrypt, false if decrypt.

    Returns
    -------
    string
      The encrpted or decrypted string.

    Examples
    --------
    >>> from cipher_tl3179 import cipher_tl3179
    >>> text = 'Apple'
    >>> shift = 1
    >>> encrypt = True
    >>> cipher_tl3179.cipher(text, shift, encrypt):
    'Bqqmf'
    >>> text = 'Apple'
    >>> shift = 1
    >>> encrypt = False
    >>> cipher_tl3179.cipher(text, shift, encrypt):
    'zookd'
    """

    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text







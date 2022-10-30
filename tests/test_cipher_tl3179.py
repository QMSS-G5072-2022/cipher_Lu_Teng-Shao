from cipher_tl3179 import cipher_tl3179

def test_cipher():
    example_text = 'Apple'
    example_shift = 1
    expected = 'Bqqmf'
    actual = cipher_tl3179.cipher(example_text, example_shift)
    assert actual == expected
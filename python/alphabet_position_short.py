def alphabet_position(text):
    return print(' '.join(str(ord(number) - 96) for number in text.lower() if number.isalpha()))

text = 'Ab,cd'

alphabet_position(text)

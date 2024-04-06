import string


def caesar(text, shift, direction):
    alphabet = string.ascii_lowercase
    output = ""
    # when decoding we shift the letter position backward which is equivalent to subtracting or adding a negative number
    if direction == "decode":
        shift *= -1
    if shift > 25:
        shift = shift % 25
    for char in text:
        # all encoding and decoding are done in lowercase
        if char in alphabet:
            position = alphabet.index(char.lower())
            new_position = position + shift
            # deal with overflow
            if new_position > 25:
                new_position = new_position % 25 + shift
            elif new_position < 0:
                print(new_position)
                new_position += 26
            output += alphabet[new_position]
        else:
            output += char

    print(f"The {direction}d text is {output}")
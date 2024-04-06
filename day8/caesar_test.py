from caesar_cipher import caesar

run = "y"
while run == "y":
    direction_ = input("Type encode to encrypt or decode to decrypt: ")
    text_ = input("Type your message: ").lower()
    shift_ = int(input("Type the shift number: "))
    caesar(text=text_, direction=direction_, shift= shift_)
    run = input(f"Do you want to continue? (y/n): ").lower()
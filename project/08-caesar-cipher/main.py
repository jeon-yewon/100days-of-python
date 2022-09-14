import art
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
print(art.logo)

def caeser_cipher(text, shift, direction):

    text_return = ""
    shift = shift % 26

    for i in text:
        if i in alphabet:
            index = alphabet.index(i)
            if direction == "encode":
                # encoding part
                if index < (len(alphabet) - shift):
                    new_index = index + shift
                else:
                    new_index = shift - (len(alphabet) - index)
            elif direction == "decode":
                # decoding part
                new_index = index - shift
            else:
                print("Error! Please type 'encode' or 'decode'")
            text_return += alphabet[new_index]
        
        else:
            text_return += i

    print(f"The {direction}d text is {text_return}")

should_continue = True
while should_continue:
    input_d = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n-> ")
    input_t = input("Type your message:\n-> ").lower()
    input_s = int(input("Type the shift number:\n-> "))
    caeser_cipher(input_t, input_s, input_d)

    again = input("Type 'yes' if you want to go again. Otherwise type 'no'")
    if again == "no":
        should_continue = False

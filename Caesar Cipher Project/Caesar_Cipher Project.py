import caesar_cipher_art
print(caesar_cipher_art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

# def decrypt(original_text, shift_amount):
#     reverse_code_text = ""

#     for letters in original_text:
#         shifted_position = alphabet.index(letters) - shift_amount
#         shifted_position %= len(alphabet)
#         reverse_code_text += alphabet[shifted_position]
#     print(f"Here is the decoded result: {reverse_code_text}")


# def encrypt(original_text, shift_amount):
#     code_text = ""
#
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         code_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {code_text}")


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

#caesar(text, shift, direction) # Positional argument
# or
#caesar(original_text = text, shift_amount = shift, encode_or_decode = direction) # Keyword argument

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Do you want to go again? Type 'yes' to continue, or 'no' to end.\n").lower()
    if restart == 'no':
        should_continue = False
        print("Goodbye")

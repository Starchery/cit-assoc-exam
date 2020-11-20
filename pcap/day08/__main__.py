import pcap.day08.caesar_cipher as cc

# Import the module "caesar_cipher" from the package day8 in the package pcap
# 'as' allows us to use a shorter name for a module


def main():
    message = input("Enter a sensitive message: ")
    key = input("Enter the shift value: ")

    try:
        key = int(key)
    except ValueError:
        print(f"Sorry, {key!r} is not a valid shift.")
        return

    cipher = cc.CaesarCipher(shift=key)

    encrypted_message = cipher.encrypt(message)
    print(f"Encrypted: {encrypted_message}")

    # note that we decrypt the encrypted message, not the original one
    # and that we use the same cipher that we used to encrypt.
    # try using a different one with a different shift value
    decrypted_message = cipher.decrypt(encrypted_message)
    print(f"Decrypted: {decrypted_message}")


main()

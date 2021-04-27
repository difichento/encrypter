from caesar import caesar_encrypt_int, caesar_decrypt_int, caesar_auto_crack_int
from vigenere import vigenere_encrypt_int, vigenere_decrypt_int
from vernam import vernam_encrypt_int, vernam_decrypt_int
from picture import picture_encrypt_int, picture_decrypt_int


def hello():
    print("Hi, I'm encryptor, that's what I can do:")


def quit_program():
    quit()


def print_menu(menu_options):
    print("Available features:")
    for key in menu_options:
        print(key, ": ", menu_options[key]["text"], sep="")
    print("---------")


if __name__ == "__main__":
    menu_options = {"q": {"function": quit_program, "text": "Quit program"},
                    "1": {"function": caesar_encrypt_int, "text": "Caesar encrypt"},
                    "2": {"function": caesar_decrypt_int, "text": "Caesar decrypt"},
                    "3": {"function": caesar_auto_crack_int, "text": "Caesar auto crack"},
                    "4": {"function": vigenere_encrypt_int, "text": "Vigenere encrypt"},
                    "5": {"function": vigenere_decrypt_int, "text": "Vigenere decrypt"},
                    "6": {"function": vernam_encrypt_int, "text": "Vernam encrypt"},
                    "7": {"function": vernam_decrypt_int, "text": "Vernam decrypt"},
                    "8": {"function": picture_encrypt_int, "text": "Encrypt message in picture"},
                    "9": {"function": picture_decrypt_int, "text": "Decrypt message from picture"}}
    hello()
    keepWorking = True
    while keepWorking:
        menuSelection = ""
        while menuSelection not in menu_options.keys():
            print_menu(menu_options)
            menuSelection = input().lower()
        menu_options[menuSelection]["function"]()

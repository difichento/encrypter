from caesar import *
from vigenere import *
from vernam import *
from picture import *


def welcome_function():
    print("Hi, I'm encryptor, that's what I can do:")


def quit_program():
    quit()


def print_menu(option_list):
    print("Available features:")
    for key in option_list:
        print(key, ": ", option_list[key]["text"], sep="")
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
    welcome_function()
    keepWorking = True
    while keepWorking:
        menuSelection = ""
        while menuSelection not in menu_options.keys():
            print_menu(menu_options)
            menuSelection = input().lower()
        menu_options[menuSelection]["function"]()

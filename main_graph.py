from caesar import Caesar
from vigenere import Vigenere
from vernam import Vernam
from picture import Picture
from window import window

if __name__ == '__main__':
    cas = Caesar()
    vigen = Vigenere()
    vernam = Vernam()
    pic = Picture()

    cas.show()
    vigen.show()
    vernam.show_vernam()
    pic.show()
    window.mainloop()

from caesar import Caesar
from global_var import window
from picture import Picture
from vigenere import Vigenere
from vernam import Vernam

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

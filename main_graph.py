from caesar import Caesar
from global_var import window
from picture import Picture
from vigenere import Vigenere
from vernam import Vernam
<<<<<<< HEAD
=======
from picture import Picture
from window import window
>>>>>>> da2fa4dd70c943c684f5e805a708e99e2772c3fb

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

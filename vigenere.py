from global_var import alphabet_upper
from tkinter import filedialog, Label, Button, IntVar, Radiobutton, Entry, StringVar
from tkinter import messagebox
from window import vig


def vigenere_encrypt(source_file_way, result_file_way, key_word):
    """
    Функция для зашифровки шифром Виженера.
    Все буквы будут переведены в верхний регистр, а остальные символы удалены
    :param source_file_way: Файл с исходным текстом
    :param result_file_way: Файл куда будет записан результат
    :param key_word: Ключевое слово
    :return: Ничего не возвращает, но запысывает зашифрованный текст в result_file
    """
    result = ""
    source_file = open(source_file_way, "r")

    new_text = ""
    # preparing file
    for line in source_file.readlines():
        for i in line.upper():
            if i in alphabet_upper:
                new_text += i

    # preparing keyword
    tmp = ""
    for i in key_word.upper():
        if i in alphabet_upper:
            tmp += i
    key_word = tmp

    # encrypting
    for i in range(len(new_text)):
        result += alphabet_upper[alphabet_upper.find(new_text[i]) + alphabet_upper.find(key_word[i % len(key_word)])]

    # writing result
    result_file = open(result_file_way, "w")
    result_file.write(result)
    source_file.close()
    result_file.close()


def vigenere_encrypt_int():
    """
    Интерфейс для работы в консоли с функцией vigenere_encrypt
    :return: Ничего не возвращает
    """
    print("Your file will be reduced to this form: i want 98 cookies -> IWANTCOOKIES")
    source_file_way = input("Enter file you want encrypt name or absolute way: ")
    result_file_way = input("Enter the name of the file you want to save the result to: ")
    key_word = input("Enter keyword: ")
    vigenere_encrypt(source_file_way, result_file_way, key_word)


def vigenere_decrypt(source_file_way, result_file_way, key_word):
    """
    Функция для расшифровки шифра Виженера.
    :param source_file_way: Файл с исходным текстом
    :param result_file_way: Файл куда будет записан результат
    :param key_word: Ключевое слово
    :return: Ничего не возвращает, но запысывает расшифрованный текст в result_file
    """
    result = ""
    source_file = open(source_file_way, "r")

    new_text = ""
    # preparing file
    for line in source_file.readlines():
        for i in line.upper():
            if i in alphabet_upper:
                new_text += i

    # preparing keyword
    tmp = ""
    for i in key_word.upper():
        if i in alphabet_upper:
            tmp += i
    key_word = tmp

    # encrypting
    for i in range(len(new_text)):
        result += alphabet_upper[alphabet_upper.find(new_text[i]) - alphabet_upper.find(key_word[i % len(key_word)])]

    # writing result
    result_file = open(result_file_way, "w")
    result_file.write(result)
    source_file.close()
    result_file.close()


def vigenere_decrypt_int():
    """
    Интерфейс для работы в консоли с функцией vigenere_decrypt
    :return: Ничего не возвращает
    """
    source_file_way = input("Enter file you want decrypt name or absolute way: ")
    result_file_way = input("Enter the name of the file you want to save the result to: ")
    key_word = input("Enter keyword: ")
    vigenere_decrypt(source_file_way, result_file_way, key_word)


class Vigenere:
    """
    Класс для отрисовки вкладки "Шифр Виженера" в графическом интерфейсе
    """
    def __init__(self):
        self.source_file = None
        self.result_file = None
        self.selected_type = None
        self.selected_key = None

    def select_source(self):

        if self.source_file is not None:
            Label(vig, text="  " * len(self.source_file)).grid(column=1, row=1)
        self.source_file = filedialog.askopenfilename(
            filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
        txt = Label(vig, text=self.source_file)
        txt.grid(column=1, row=1)

    def select_result(self):

        if self.result_file is not None:
            Label(vig, text="  " * len(self.source_file)).grid(column=1, row=2)

        self.result_file = filedialog.askopenfilename(
            filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
        txt = Label(vig, text=self.result_file)
        txt.grid(column=1, row=2)

    def start(self):
        sel = self.selected_type.get()
        if self.source_file is None:
            messagebox.showinfo('Ошибка', 'Не выбран исходный файл')
        elif self.result_file is None:
            messagebox.showinfo('Ошибка', 'Не выбран файл для сохранения')
        else:
            if sel == 1:
                vigenere_encrypt(self.source_file, self.result_file, self.selected_key.get())
                messagebox.showinfo('Ура!', 'Файл успешно зашифрован')
            elif sel == 2:
                vigenere_decrypt(self.source_file, self.result_file, self.selected_key.get())
                messagebox.showinfo('Ура!', 'Файл успешно расшифрован')

    def show(self):
        description = Label(vig,
                                text="Шифр Виженера осуществляется суммой индексов буквы и ключа."
                                     "\nВсе символы как в ключе, так и в исходном тексте, кроме букв будут удалены,"
                                     " \nвсе буквы будут переведены в верхний регистр",
                                padx=0, pady=20)
        description.grid(column=0, row=0)

        choose_file = Button(vig, text="Выберите файл который хотите зашифровать/расшифровать",
                                 command=self.select_source)
        choose_file.grid(column=0, row=1)
        choose_file = Button(vig, text="Выберите куда сохранить результат",
                                 command=self.select_result)
        choose_file.grid(column=0, row=2)

        self.selected_type = IntVar()
        rad1 = Radiobutton(vig, text='Зашифровать', value=1, variable=self.selected_type)
        rad2 = Radiobutton(vig, text='Расшифровать', value=2, variable=self.selected_type)
        rad1.grid(column=0, row=3)
        rad2.grid(column=1, row=3)

        shift_text = Label(vig, text="Введите ключ")
        shift_text.grid(column=0, row=4)
        self.selected_key = StringVar()
        key = Entry(vig, textvariable=self.selected_key)
        key.grid(column=1, row=4)

        start = Button(vig, text="Начать", command=self.start)
        start.grid(column=0, row=5, pady=20)

from global_var import alphabet_upper
import random
from tkinter import filedialog, Label, Button, IntVar, Radiobutton, Entry
from tkinter import messagebox
from window import vern


def vernam_encrypt(source_file_way, result_file_way, result_key_file_way, seed):
    """
    Функция для зашифровки шифром Вернама. Генерирует случайный ключ из сида
    При этом все буквы будут переведены в верхний регистр, а остальные символы удалены
    :param source_file_way: Файл с текстом для зашифровки
    :param result_file_way: Файл куда будет сохранен зашифрованный текст
    :param result_key_file_way: Файлу куда будет сохранен ключ
    :param seed: Сид из которого будет сгенерирован случайный ключ
    :return: Ничего не возвращает, но запысывает зашифрованный текст в result_file
        и ключ в result_key_file
    """
    result = ""
    result_key = ""
    source_file = open(source_file_way, "r")

    random.seed(seed)

    # encrypting file
    for line in source_file:
        # preparing keyword
        new_line = ""

        for i in line.upper():
            if i in alphabet_upper:
                new_line += i
        line = new_line

        tmp = ""
        for i in range(len(line)):
            tmp += alphabet_upper[random.randint(0, 25)]
        keyword = tmp

        for let, klet in zip(line, keyword):
            found_let = alphabet_upper.find(let)
            found_key_let = alphabet_upper.find(klet)
            result += alphabet_upper[(found_let + found_key_let) % len(alphabet_upper)]

        result_key += keyword

    # writing result
    source_file = open(result_file_way, "w")
    source_file.write(result)
    source_file.close()
    result_key_file = open(result_key_file_way, "w")
    result_key_file.write(result_key)
    result_key_file.close()


def vernam_encrypt_int():
    """
    Интерфейс для работы в консоли с функцией vernam_encrypt
    :return: Ничего не возвращает
    """
    source_file_way = input("Enter file you want encrypt name or absolute way: ")
    result_file_way = input("Enter the name of the file you want to save the result to: ")
    new_key_file_way = input("Enter file with key name or absolute way: ")
    seed = input("Enter seed to generate random key: ")
    vernam_encrypt(source_file_way, result_file_way, new_key_file_way, seed)


def vernam_decrypt(source_file_way, result_file_way, key_file_way):
    """
    Функция для расшифровки шифра вернама
    :param source_file_way: Файл с зашифрованным текстом
    :param result_file_way: Файл куда будет сохранен результат
    :param key_file_way: Файл с ключом
    :return: Ничего не возвращает, но записывает результат расшифровки в result_file
    """
    result = ""
    source_file = open(source_file_way, "r")
    key_file = open(key_file_way, "r")

    # encrypting file
    for let, klet in zip(source_file.read(), key_file.read()):
        found_let = alphabet_upper.find(let)
        found_key_let = alphabet_upper.find(klet)
        result += alphabet_upper[(found_let - found_key_let) % len(alphabet_upper)]

    # writing result
    result_file = open(result_file_way, "w")
    result_file.write(result)
    source_file.close()
    result_file.close()
    key_file.close()


def vernam_decrypt_int():
    """
    Интерфейс для работы в консоли с функцией vernam_decrypt
    :return: Ничего не возвращает
    """
    source_file_way = input("Enter file you want decrypt name or absolute way: ")
    result_file_way = input("Enter the name of the file you want to save the result to: ")
    key_file_way = input("Enter the name of the file with key: ")
    vernam_decrypt(source_file_way, result_file_way, key_file_way)


class Vernam:
    """
    Класс для отрисовки вкладки "Шифр Вернама" в графическом интерфейсе
    """

    def __init__(self):
        self.source_file = None
        self.result_file = None
        self.key_file = None
        self.selected_type = None
        self.selected_seed = None

    def select_source(self):

        if self.source_file is not None:
            Label(vern, text="  " * len(self.source_file)).grid(column=1, row=1)
        self.source_file = filedialog.askopenfilename(
            filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
        txt = Label(vern, text=self.source_file)
        txt.grid(column=1, row=1)

    def select_result(self):

        if self.result_file is not None:
            Label(vern, text="  " * len(self.source_file)).grid(column=1, row=2)

        self.result_file = filedialog.askopenfilename(
            filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
        txt = Label(vern, text=self.result_file)
        txt.grid(column=1, row=2)

    def select_key(self):
        if self.key_file is not None:
            Label(vern, text="  " * len(self.source_file)).grid(column=1, row=3)

        self.key_file = filedialog.askopenfilename(
            filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
        txt = Label(vern, text=self.key_file)
        txt.grid(column=1, row=3)

    def start(self):
        sel = self.selected_type.get()
        if self.source_file is None:
            messagebox.showinfo('Ошибка', 'Не выбран исходный файл')
        elif self.result_file is None:
            messagebox.showinfo('Ошибка', 'Не выбран файл для сохранения')
        elif self.key_file is None:
            messagebox.showinfo('Ошибка', 'Не выбран файл с ключом')
        else:
            if sel == 1:
                vernam_encrypt(self.source_file, self.result_file, self.key_file,
                               int(self.selected_seed.get()))
                messagebox.showinfo('Ура!', 'Файл успешно зашифрован')
            elif sel == 2:
                vernam_decrypt(self.source_file, self.result_file, self.key_file)
                messagebox.showinfo('Ура!', 'Файл успешно расшифрован')

    def show_vernam(self):
        description = Label(vern,
                            text="Шифр Вернама осуществляется суммой индексов буквы и ключа."
                                 "\nВсе символы как в ключе, так и в исходном тексте, кроме букв будут удалены,"
                                 "\nвсе буквы будут переведены в верхний регистр."
                                 "\nКлюч будет автоматически сгенерирован из сида",
                            padx=0, pady=20)
        description.grid(column=0, row=0)

        choose_file = Button(vern, text="Выберите файл который хотите зашифровать/расшифровать",
                             command=self.select_source)
        choose_file.grid(column=0, row=1)
        choose_file = Button(vern, text="Выберите куда сохранить результат",
                             command=self.select_result)
        choose_file.grid(column=0, row=2)
        choose_key_file = Button(vern, text="Выберите файл с ключом/куда сохранить ключ",
                                 command=self.select_key)
        choose_key_file.grid(column=0, row=3)

        self.selected_type = IntVar()
        rad1 = Radiobutton(vern, text='Зашифровать', value=1, variable=self.selected_type)
        rad2 = Radiobutton(vern, text='Расшифровать', value=2, variable=self.selected_type)
        rad1.grid(column=0, row=4)
        rad2.grid(column=1, row=4)

        seed_text = Label(vern, text="Введите сид")
        seed_text.grid(column=0, row=5)
        self.selected_seed = IntVar()
        seed = Entry(vern, textvariable=self.selected_seed)
        seed.grid(column=1, row=5)

        start = Button(vern, text="Начать", command=self.start)
        start.grid(column=0, row=6, pady=20)

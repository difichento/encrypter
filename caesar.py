from global_var import alphabet_lower
from global_var import alphabet_upper
from tkinter import filedialog, Label, Button, IntVar, Radiobutton, Spinbox
from tkinter import messagebox
from window import caes


def encrypt_caes_line(line, shift):
    """
    Функция для зашифровки одной строки шифром цезаря
    :param line: Строка для зашифровки
    :param shift: Сдвиг
    :return: Зашифрованная строка
    """
    result = ""
    for let in line:
        find_res = alphabet_lower.find(let)
        if find_res != -1:
            find_res += shift
            find_res %= len(alphabet_upper)
            result += alphabet_lower[find_res]
        else:
            find_res = alphabet_upper.find(let)
            if find_res != -1:
                find_res += shift
                find_res %= len(alphabet_upper)
                result += alphabet_upper[find_res]
            else:
                result += let
    return result


def caesar_encrypt(source_file_way, result_file_way, shift):
    """
    Функция для зашифровки текста из файла шифром цезаря
    :param source_file_way: Файл с исходным текстом
    :param result_file_way: Файл куда будет сохранен результат (может быть и исходным файлом)
    :param shift: Сдвиг
    :return: Ничего не возвращает, но записывает зашифрованный текст в result_file
    """
    result = ""
    source_file = open(source_file_way, "r")

    # encrypting file
    for line in source_file.readlines():
        result += encrypt_caes_line(line, shift)
    source_file.close()

    # writing result
    result_file = open(result_file_way, "w")
    result_file.write(result)
    result_file.close()


def caesar_encrypt_int():
    """
    Интерфейс для работы в консоли с функцией caesar_encrypt
    :return: Ничего не возвращает
    """
    source_file_way = input("Enter file you want encrypt name or absolute way: ")
    result_file_way = input("Enter the name of the file you want to save the result to: ")
    shift = int(input("Enter shift from 1 to 25: "))
    caesar_encrypt(source_file_way, result_file_way, shift)


def decrypt_caes_line(line, shift):
    """
    Функция для расшифровки одной строки шифром цезаря
    :param line: Строка для расшифровки
    :param shift: Сдвиг
    :return: Расшифрованная строка
    """

    result = ""
    for let in line:
        find_res = alphabet_lower.find(let)
        if find_res != -1:
            find_res -= shift
            find_res %= len(alphabet_upper)
            result += alphabet_lower[find_res]
        else:
            find_res = alphabet_upper.find(let)
            if find_res != -1:
                find_res -= shift
                find_res %= len(alphabet_upper)
                result += alphabet_upper[find_res]
            else:
                result += let
    return result


def caesar_decrypt(source_file_way, result_file_way, shift):
    """
    Функция для расшифровки текста из файла шифром цезаря
    :param source_file_way: Файл с зашифрованным текстом
    :param result_file_way: Файл куда будет сохранен результат (может быть и исходным файлом)
    :param shift: Сдвиг
    :return: Ничего не возвращает, но записывает расшифрованный текст в result_file
    """
    result = ""
    source_file = open(source_file_way, "r")

    # encrypting file
    for line in source_file.readlines():
        result += decrypt_caes_line(line, shift)
    source_file.close()

    # writing result
    result_file = open(result_file_way, "w")
    result_file.write(result)


def caesar_decrypt_int():
    """
    Интерфейс для работы в консоли с функцией caesar_decrypt
    :return: Ничего не возвращает
    """
    source_file_way = input("Enter file you want decrypt name or absolute way: ")
    result_file_way = input("Enter the name of the file you want to save the result to: ")
    shift = int(input("Enter shift from 1 to 25: "))
    caesar_decrypt(source_file_way, result_file_way, shift)


def caesar_auto_crack(source_file_way, result_file_way):
    """
    Функция для авторасшифровки шифра цезаря методом частотного анализа
    :param source_file_way: Файл с зашифрованным текстом
    :param result_file_way: Файл куда будет сохранен результат
    :return: Ничего не возвращает, но записывает расшифрованный текст в result_file
    """
    source_file = open(source_file_way, "r")

    # Подсчет количества букв
    counter = {}
    let_sum = 0
    for let in alphabet_lower:
        counter[let] = 0
    for line in source_file.readlines():
        for let in line.lower():
            if let in counter.keys():
                counter[let] += 1
                let_sum += 1

    # Находим самую часто входящую букву и считаем что в исходном тексте это была буква "e"
    counter = (list(counter.items()))
    counter.sort(key=lambda i: i[1], reverse=True)
    counter = list(map(lambda x: [x[0], x[1] / let_sum], counter))
    shift = alphabet_lower.find(counter[0][0]) - alphabet_lower.find("e")
    if shift < 0:
        shift = len(alphabet_upper) + shift

    caesar_decrypt(source_file_way, result_file_way, shift)


def caesar_auto_crack_int():
    """
    Интерфейс для работы в консоли с функцией caesar_auto_crack
    :return: Ничего не возвращает
    """
    source_file_way = input("Enter file you want decrypt name or absolute way: ")
    result_file_way = input("Enter file you want to save result to name: ")
    caesar_auto_crack(source_file_way, result_file_way)


class Caesar:
    """
    Класс для отрисовки вкладки "Шифр Цезаря" в графическом интерфейсе
    """
    def __init__(self):
        self.source_file = None
        self.result_file = None
        self.selected_type = None
        self.selected_shift = None

    def select_source(self):
        if self.source_file is not None:
            Label(caes, text="  " * len(self.source_file)).grid(column=1, row=1)
        self.source_file = filedialog.askopenfilename(
            filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
        txt = Label(caes, text=self.source_file)
        txt.grid(column=1, row=1)

    def select_result(self):
        if self.result_file is not None:
            Label(caes, text="  " * len(self.source_file)).grid(column=1, row=2)
        self.result_file = filedialog.askopenfilename(
            filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
        txt = Label(caes, text=self.result_file)
        txt.grid(column=1, row=2)

    def start(self):
        sel = self.selected_type.get()
        if self.source_file is None:
            messagebox.showinfo('Ошибка', 'Не выбран исходный файл')
        elif self.result_file is None:
            messagebox.showinfo('Ошибка', 'Не выбран файл для сохранения')
        else:
            if sel == 1:
                caesar_encrypt(self.source_file, self.result_file, self.selected_shift.get())
                messagebox.showinfo('Ура!', 'Файл успешно зашифрован')
            elif sel == 2:
                caesar_decrypt(self.source_file, self.result_file, self.selected_shift.get())
                messagebox.showinfo('Ура!', 'Файл успешно расшифрован')

    def start_analys(self):
        sel = self.selected_type.get()
        if self.source_file is None:
            messagebox.showinfo('Ошибка', 'Не выбран исходный файл')
        elif self.result_file is None:
            messagebox.showinfo('Ошибка', 'Не выбран файл для сохранения')
        else:
            caesar_auto_crack(self.source_file, self.result_file)
            messagebox.showinfo('Ура!', 'Файл успешно расшифрован')

    def show(self):
        description = Label(caes, text="Шифр Цезаря осуществляется фикированным сдвигом текста\n"
                                            " по алфавиту.", padx=0, pady=20)
        description.grid(column=0, row=0)

        choose_file = Button(caes, text="Выберите файл который хотите зашифровать/расшифровать",
                                  command=self.select_source)
        choose_file.grid(column=0, row=1)
        choose_file = Button(caes, text="Выберите куда сохранить результат",
                                  command=self.select_result)
        choose_file.grid(column=0, row=2)

        self.selected_type = IntVar()
        rad1 = Radiobutton(caes, text='Зашифровать', value=1, variable=self.selected_type)
        rad2 = Radiobutton(caes, text='Расшифровать', value=2, variable=self.selected_type)
        rad1.grid(column=0, row=3)
        rad2.grid(column=1, row=3)

        shift_text = Label(caes, text="Выберите сдвиг")
        shift_text.grid(column=0, row=4)
        self.selected_shift = IntVar()
        shift = Spinbox(caes, from_=1, to=25, width=5, textvariable=self.selected_shift)
        shift.grid(column=1, row=4)

        start = Button(caes, text="Начать", command=self.start)
        start.grid(column=0, row=5, pady=20)

        description_caes_analys = Button(caes, text="Взлом частотным анализом", command=self.start_analys)
        description_caes_analys.grid(column=0, row=6)

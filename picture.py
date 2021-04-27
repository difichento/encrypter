import numpy as np
from PIL import Image
import random
from tkinter import filedialog, Label, Button, IntVar, Radiobutton, Entry, StringVar
from tkinter import messagebox
from window import pict


def picture_encrypt(source_picture_way, source_text_file_way, result_picture_way, seed):
    """
    Зашифровывает текст в случайные пиксели картинки (генерируются из сида)
    Один пиксель = один символ, соответственно зашифровать можно
    picture_height * picture_width - 1 символов (-1, т.к. в конец зашифровывается 0)
    :param source_picture_way: Файл с исходной картинкой
    :param source_text_file_way: Файл с текстом для зашифровки
    :param result_picture_way: Файл куда будет сохранена картинка
    :param seed: Сид для генерации случайной последовательности пикселей
    :return: Ничего не возвращает, но создает файл картинки с зашифрованным текстом
    """

    # загрузка файлов и инициализация некоторых переменных
    used_pixel_list = []

    source_text_file = open(source_text_file_way, "r")
    source_img = Image.open(source_picture_way)
    source_img.load()
    source_array = np.array(source_img)
    source_width, source_height = source_img.size

    random.seed(seed)
    current_pixel = random.randint(0, source_height * source_width)

    # основной цикл в котором шифруется текст
    for line in source_text_file.readlines():
        for let in line:
            while current_pixel in used_pixel_list:
                current_pixel = random.randint(0, source_height * source_width)
            pixel_line = current_pixel // source_width
            pixel_collumn = current_pixel % source_width
            let = ord(let)

            let_r = (let & 0b11100000) >> 5
            let_g = (let & 0b00011100) >> 2
            let_b = let & 0b00000011
            source_array[pixel_line][pixel_collumn][0] = (source_array[pixel_line][pixel_collumn][
                                                              0] & 0b11111000) + let_r
            source_array[pixel_line][pixel_collumn][1] = (source_array[pixel_line][pixel_collumn][
                                                              1] & 0b11111000) + let_g
            source_array[pixel_line][pixel_collumn][2] = (source_array[pixel_line][pixel_collumn][
                                                              2] & 0b11111100) + let_b
            used_pixel_list.append(current_pixel)

    # зашифровываем 0 чтобы оозначить конец последовательности
    while current_pixel in used_pixel_list:
        current_pixel = random.randint(0, source_height * source_width)
    pixel_line = current_pixel // source_width
    pixel_collumn = current_pixel % source_width
    source_array[pixel_line][pixel_collumn][0] = (source_array[pixel_line][pixel_collumn][0] & 0b11111000)
    source_array[pixel_line][pixel_collumn][1] = (source_array[pixel_line][pixel_collumn][1] & 0b11111000)
    source_array[pixel_line][pixel_collumn][2] = (source_array[pixel_line][pixel_collumn][2] & 0b11111100)

    # сохранение результата
    res = Image.fromarray(source_array, "RGB")
    res.save(result_picture_way)
    source_text_file.close()


def picture_encrypt_int():
    """
    Интерфейс для работы в консоли с функцией picture_encrypt
    :return: Ничего не возвращает
    """
    source_picture_way = input("Enter name of picture you want to encrypt in: ")
    source_text_way = input("Enter file you want to encrypt name: ")
    result_picture_name = input("Enter the name of the file you want to save the result to (without extension): ")
    seed = input("Enter seed: ")
    picture_encrypt(source_picture_way, source_text_way, result_picture_name + ".bmp", seed)


def picture_decrypt_letter(pixel):
    """
    Функция для извлечения символа из пикселя
    :param pixel: пиксель из которого нужно извлечь символ
    """
    let_r = (pixel[0] & 0b00000111) << 5
    let_g = (pixel[1] & 0b00000111) << 2
    let_b = pixel[2] & 0b00000011
    let = let_r + let_g + let_b
    return let


def picture_decrypt(source_picture_way, result_text_file_way, seed):
    """
    Функция для расшифровки текста из картинки, если будет указан неверный сид, программа
    скорее всего выдаст ошибку при попытке записи в файл.
    :param source_picture_way: Картинка с зашифрованным текстом
    :param result_text_file_way: Файл куда будет сохранен текст
    :param seed: Сид
    :return: Ничего не возвращает, но записывает результат расшифровки в result_text_file
    """

    # загрузка файлов и инициализация некоторых переменных
    used_pixel_list = []

    result_file = open(result_text_file_way, "w")
    source_img = Image.open(source_picture_way)
    source_img.load()
    source_array = np.array(source_img)

    source_width, source_height = source_img.size

    random.seed(seed)
    result = ""
    # расшифровываем по пикселю, пока не найдем 0
    while True:
        current_pixel = random.randint(0, source_height * source_width)
        while current_pixel in used_pixel_list:
            current_pixel = random.randint(0, source_height * source_width)
        pixel_line = current_pixel // source_width
        pixel_collumn = current_pixel % source_width
        tmp = picture_decrypt_letter(source_array[pixel_line][pixel_collumn])

        if tmp == 0:
            break
        else:
            result += chr(tmp)

    result_file.write(result)
    result_file.close()


def picture_decrypt_int():
    """
    Интерфейс для работы в консоли с функцией picture_decrypt
    :return: Ничего не возвращает
    """
    source_picture_way = input("Enter name of picture you want to decrypt: ")
    result_text_file_way = input("Enter the name of the file you want to save the result to: ")
    seed = input("Enter seed: ")
    picture_decrypt(source_picture_way, result_text_file_way, seed)


class Picture:
    """
    Класс для отрисовки вкладки "Шифр Цезаря" в графическом интерфейсе
    """

    def __init__(self):
        self.source_file = None
        self.source_text_file = None
        self.result_file = None
        self.result_picture = None
        self.selected_type = None
        self.selected_seed = None

    def select_source(self):

        if self.source_file is not None:
            Label(pict, text="  " * len(self.source_file)).grid(column=1, row=1)
        self.source_file = filedialog.askopenfilename(
            filetypes=(("Pictures", "*.png *.jpg *.bmp"), ("all files", "*.*")))
        txt = Label(pict, text=self.source_file)
        txt.grid(column=1, row=1)

    def select_source_text(self):

        if self.source_file is not None:
            Label(pict, text="  " * len(self.source_file)).grid(column=1, row=2)
        self.source_text_file = filedialog.askopenfilename(
            filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
        txt = Label(pict, text=self.source_text_file)
        txt.grid(column=1, row=2)

    def select_result(self):

        if self.result_file is not None:
            Label(pict, text="  " * len(self.result_file)).grid(column=1, row=3)

        self.result_file = filedialog.askopenfilename(
            filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
        txt = Label(pict, text=self.result_file)
        txt.grid(column=1, row=3)

    def start(self):
        sel = self.selected_type.get()
        if self.source_file is None:
            messagebox.showinfo('Ошибка', 'Не выбран исходный файл')
        else:
            if sel == 1:
                if self.result_picture is None:
                    messagebox.showinfo('Ошибка', 'Не выбран файл для сохранения')
                else:
                    picture_encrypt(self.source_file, self.source_text_file, self.result_picture.get() + ".bmp",
                                    int(self.selected_seed.get()))
                    messagebox.showinfo('Ура!', 'Файл успешно зашифрован')
            elif sel == 2:
                if self.result_file is None:
                    messagebox.showinfo('Ошибка', 'Не выбран файл для сохранения')
                else:
                    picture_decrypt(self.source_file, self.result_file, int(self.selected_seed.get()))
                    messagebox.showinfo('Ура!', 'Файл успешно расшифрован')

    def show(self):
        description = Label(pict,
                            text="Шифрование текста в картинку"
                                 "\nСама картинка почти не изменится"
                                 "\nКартинка с зашифрованным в нее текстом будет сохранена в формате .bmp"
                                 "\nЧтобы расшифровать картинку понадобится сид, указанный при шифровании",
                            padx=0, pady=20)
        description.grid(column=0, row=0)

        choose_file = Button(pict, text="Выберите файл который хотите зашифровать/расшифровать",
                             command=self.select_source)
        choose_file.grid(column=0, row=1)

        choose_text_file = Button(pict, text="Выберите файл c текстом который хотите зашифровать",
                                  command=self.select_source_text)
        choose_text_file.grid(column=0, row=2)

        choose_result_file = Button(pict, text="Выберите куда сохранить результат (для расшифровки)",
                                    command=self.select_result)
        choose_result_file.grid(column=0, row=3)

        result_picture_text = Label(pict, text="Введите имя для картинки, полученной в результате шифрования"
                                               "\n(без расширения)")
        result_picture_text.grid(column=0, row=5)
        self.result_picture = StringVar()
        result = Entry(pict, textvariable=self.result_picture)
        result.grid(column=1, row=5)

        self.selected_type = IntVar()
        rad1 = Radiobutton(pict, text='Зашифровать', value=1, variable=self.selected_type)
        rad2 = Radiobutton(pict, text='Расшифровать', value=2, variable=self.selected_type)
        rad1.grid(column=0, row=4)
        rad2.grid(column=1, row=4)

        seed_text = Label(pict, text="Введите сид")
        seed_text.grid(column=0, row=6)
        self.selected_seed = IntVar()
        seed = Entry(pict, textvariable=self.selected_seed)
        seed.grid(column=1, row=6)

        start = Button(pict, text="Начать", command=self.start)
        start.grid(column=0, row=7, pady=20)

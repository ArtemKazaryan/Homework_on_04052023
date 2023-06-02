

# !!!!!!  ДЛЯ ЗАПУСКА ОТДЕЛЬНЫХ ЗАДАНИЙ РАЗВЕРНИТЕ (И ЕСЛИ ПОТРЕБУЕТСЯ, РАСКОММЕНТИРУЙТЕ) ИХ РЕШЕНИЕ !!!!!!

# Домашняя работа на 04.05.2023

# 1. Напишите функцию analysis_and_summarize_file, которая принимает имя файла в
# качестве входных данных. Файл содержит большое количество текстовых данных.
# Функция должна прочитать содержимое файла, проанализировать данные для сбора
# соответствующей информации (например, частота слов, количество строк, средняя длина слова)
# и создать сводный отчет в новом файле.

# Решение:
def analysis_and_summarize_file(filename_in):
    with open('text_data.txt', 'r', encoding='utf-8') as f:
        text_data = f.read()
        # print(text_data)
        word_list = text_data.split(' ')
        word_count = f'Количество слов: {len(word_list)}\n'
        lines = text_data.count('\n') + 1
        string_count = f'Количество строк: {lines}\n'
        alphab = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыъэюя'
        symbols_count = 0
        text_data.split()
        for i in range(len(text_data)):
            if text_data[i].lower() in alphab:
                symbols_count += 1
        average_word_length = f'Средняя длина слова: {round(symbols_count / len(word_list), 2)}\n'
        # print(word_count)
        # print(string_count)
        # print(average_word_length)
        filename_out = 'Сводный_отчёт_по_файлу_(' + filename_in + ').txt'
    with open(filename_out, 'w', encoding='utf-8') as f:
        f.write(word_count)
        f.write(string_count)
        f.write(average_word_length)

analysis_and_summarize_file('text_data.txt')



# 2. Напишите две функции: encrypt_file и decrypt_file. Функция encrypt_file должна
# принимать имя файла и ключ в качестве входных данных, считывать содержимое файла,
# шифровать содержимое с помощью пользовательского алгоритма шифрования и записывать
# зашифрованные данные в новый файл. Функция decrypt_file должна принимать имя файла
# и тот же ключ в качестве входных данных, читать зашифрованное содержимое файла,
# расшифровывать содержимое с использованием обратного алгоритма и записывать
# расшифрованные данные в новый файл. Создайте декоратор с именем encryption_logging,
# который регистрирует сведения об операциях шифрования и дешифрования,
# такие как имя файла, ключ и отметка времени.

# Решение:

import datetime

def encryption_logging(func):
    def wrapper(file_name, key):
        result = func(file_name, key)
        with open('log.txt', 'a') as log_file:
            log_file.write(f'{datetime.datetime.now()}: {func.__name__} вызван с именем файла={file_name} и ключом={key}\n')
        return result
    return wrapper

@encryption_logging
def encrypt_file(filename, key):
    a0 = list('abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщьыъэюя'
              'ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ0123456789'
              '!"#$%&()*+,-./:;<=>?@[\]^ _`{|}~\n')
    ak = ['-'] * (len(a0) + key)
    for i in range(key, len(ak)):
        ak[i] = a0[i - key]
    for i in range(len(ak) - key, len(ak)):
        ak[i - len(a0)] = ak[i]
    for i in range(0, key):
        ak.pop()
    a0k_dict = {}
    for i in range(len(a0)):
        a0k_dict[a0[i]] = ak[i]

    with open(filename, 'r', encoding='utf-8') as f_in:
        data = list(f_in.read())
        code = []
        for i in range(len(data)):
            code.append(a0k_dict[data[i]])
        code_str = ''.join(code)
    with open('encrypted_file.txt', 'w', encoding='utf-8') as f_encr:
        f_encr.write(code_str)
    print()

@encryption_logging
def decrypt_file(filename, key):
    a0 = list('abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщьыъэюя'
              'ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ0123456789'
              '!"#$%&()*+,-./:;<=>?@[\]^ _`{|}~\n')
    ak = ['-'] * (len(a0) + key)
    for i in range(key, len(ak)):
        ak[i] = a0[i - key]
    for i in range(len(ak) - key, len(ak)):
        ak[i - len(a0)] = ak[i]
    for i in range(0, key):
        ak.pop()
    ak0_dict = {}
    for i in range(len(ak)):
        ak0_dict[ak[i]] = a0[i]

    with open(filename, 'r', encoding='utf-8') as f_in:
        code = list(f_in.read())
        data = []
        for i in range(len(code)):
            data.append(ak0_dict[code[i]])
        data_str = ''.join(data)

    with open('decrypted_file.txt', 'w', encoding='utf-8') as f_decr:
        f_decr.write(data_str)
    print()

encrypt_file('file_for_encryption.txt', 140)
decrypt_file('encrypted_file.txt', 140)



# 3. Напишите функцию с именем analysis_file_sizes, которая принимает путь к каталогу
# в качестве входных данных. Функция должна рекурсивно обходить каталог и его подкаталоги и
# вычислять общий размер всех файлов, содержащихся в них. Результат должен быть возвращен в
# удобочитаемом формате, например, в килобайтах (КБ), мегабайтах (МБ) или гигабайтах (ГБ).
# Реализуйте эту функциональность с помощью модуля os в Python.

# Решение:

import os
def analysis_file_sizes(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            print(file_path)
            total_size += os.path.getsize(file_path)
            if total_size < 1024:
                return f'{total_size} Б'
            elif total_size < 1024 ** 2:
                return f'{round(total_size / 1024, 2)} КБ'
            elif total_size < 1024 ** 3:
                return f'{round(total_size / (1024 ** 2), 2)} МБ'
            else:
                return f'{round(total_size / (1024 ** 3), 2)} ГБ'

path = 'C:/Windows/'
print(analysis_file_sizes(path))

import os
import shutil


def remove_word_from_directory(path, word_to_remove):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            if word_to_remove in name:
                new_name = name.replace(word_to_remove, '')
                new_path = os.path.join(root, new_name)
                if os.path.exists(new_path):
                    base, extension = os.path.splitext(new_name)
                    count = 1
                    while os.path.exists(new_path):
                        new_name = f"{base}_{count}{extension}"
                        new_path = os.path.join(root, new_name)
                        count += 1
                os.rename(os.path.join(root, name), new_path)
        for name in dirs:
            if word_to_remove in name:
                new_name = name.replace(word_to_remove, '')
                new_path = os.path.join(root, new_name)
                if os.path.exists(new_path):
                    base, extension = os.path.splitext(new_name)
                    count = 1
                    while os.path.exists(new_path):
                        new_name = f"{base}_{count}{extension}"
                        new_path = os.path.join(root, new_name)
                        count += 1
                os.rename(os.path.join(root, name), new_path)


# Пример использования:
root_folder = input("Введите путь к корневой папке: ")
word_to_remove = "[SW.BAND] "

remove_word_from_directory(root_folder, word_to_remove)
print("Готово. Указанное слово было удалено из названий папок и файлов.")

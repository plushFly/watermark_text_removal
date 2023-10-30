import os


def remove_words_from_directory(path, words_to_remove):
    """
    Удаляет указанные слова из названий файлов и папок в заданной директории.
    :param path: Путь к корневой папке, в которой нужно выполнить удаление слов.
    :param words_to_remove: Список слов для удаления.
    """
    for root, dirs, files in os.walk(path, topdown=False):  # Проходим по всем файлам и папкам в директории
        for name in files + dirs:  # Обрабатываем каждый файл и папку
            for word_to_remove in words_to_remove:  # Проверяем каждое слово на наличие в имени файла или папки
                if word_to_remove in name:  # Если слово найдено в имени
                    new_name = name  # Создаем новое имя
                    for word in words_to_remove:  # Удаляем все указанные слова из имени
                        new_name = new_name.replace(word, '')
                    count = 1  # Счетчик для добавления к имени файла, если файл с таким именем уже существует
                    new_path = os.path.join(root, new_name)  # Создаем новый путь к файлу или папке
                    while os.path.exists(new_path):  # Проверяем, существует ли уже файл или папка с таким именем
                        base, extension = os.path.splitext(new_name)  # Разделяем имя файла и его расширение
                        new_name = f"{base}_{count}{extension}"  # Добавляем счетчик к имени файла
                        new_path = os.path.join(root, new_name)  # Обновляем путь к файлу или папке
                        count += 1  # Увеличиваем счетчик
                    os.rename(os.path.join(root, name), new_path)  # Переименовываем файл или папку


def main():
    root_folder = input("Введите путь к корневой папке: ")  # Запрашиваем у пользователя путь к корневой папке
    words_to_remove = input("Введите слова для удаления (через запятую): ").split(
        ',')  # Запрашиваем у пользователя список слов для удаления
    words_to_remove = [word.strip() for word in words_to_remove]  # Убираем лишние пробелы вокруг слов
    remove_words_from_directory(root_folder,
                                words_to_remove)  # Вызываем функцию для удаления слов из названий файлов и папок
    print("Готово. Указанные слова были удалены из названий папок и файлов.")  # Выводим сообщение о завершении работы


if __name__ == "__main__":
    main()

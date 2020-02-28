#Case-study
#Recursion

# Developers:   Arhipova A. (%),
#               Revtova L. (%),
import os
import os.path


def main():
    path = os.getcwd()
    print('Путь:', path)
    path_up = path[:path.rfind('\\')]
    
    def all_catalog(path, level=1):
        print('Уровень =', level, 'Содержимое папки:', os.listdir(path))
        for i in os.listdir(path):
            if os.path.isdir(path + '\\' + i):
                all_catalog(path + '\\' + i, level + 1)

    def all_catalog_up(path, level=1):
        print('Уровень =', level, 'Содержимое папки:', os.listdir(path))
        for i in os.listdir(path):
            if os.path.isdir(path + '\\' + i):
                all_catalog(path + '\\' + i, level + 1)

    def findFiles(name, path):
        for i in os.listdir(path):
            if i == name:
                print(path + '\\' + i)
            elif os.path.isdir(path + "\\" + i):
                findFiles(name, path + "\\" + i)

    def moveDown(path):
        for i in os.listdir(path):
            if os.path.isdir(i):
                print(i)
        print('Введите название папки:')
        directory = str(input())
        return all_catalog(directory, level=1)
    
    def countFiles(path):
        count = 0
        for i in os.listdir(path):
            put = path + '\\' + i
            # print('путь', put)
            if os.path.isfile(put):
                count += 1
            elif os.path.isdir(put):
                count += countFiles(put)
        return count

    def countBytes(path):
        bytes = os.path.getsize(path)
        for i in os.listdir(path):
            folder = path + '\\' + i
            if os.path.isfile(folder):
                bytes += os.path.getsize(folder)
            elif os.path.isdir(folder):
                bytes = bytes + countBytes(folder)
        return bytes

    def runCommand(command):
        if command == 1:
            return all_catalog(path)
        elif command == 2:
            return all_catalog_up(path_up)
        elif command == 3:
            return moveDown(path)
        elif command == 4:
            print('Количество файлов в каталоге: ', end='')
            print(countFiles(path))
        elif command == 5:
            print('Размер текущего каталога (в байтах): ', end='')
            print(countBytes(path))
        elif command == 6:
            print('Введите название файла (с расширением)')
            target = str(input())
            print(findFiles(target, path))

    def acceptCommand():
        print('''1. Просмотр каталога\n2. На уровень вверх\n3. На уровень вниз\n4. Количество файлов и каталогов''')
        print('''5. Размер текущего каталога (в байтах)\n6. Поиск файла\n7. Выход из программы''')
        print('Выберите пункт меню:')
        command = int(input())
        if command < 1 or command > 7:
            print('ОШИБКА')
            return acceptCommand()
        if command == 7:
            print('Работа программы завершена')
            exit()
        else:
            runCommand(command)
        while command != 7 or command < 1 or command > 7:
            return acceptCommand()
    acceptCommand()
    

main()

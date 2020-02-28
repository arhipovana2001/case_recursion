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

    

main()

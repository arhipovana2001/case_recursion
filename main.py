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
    

main()

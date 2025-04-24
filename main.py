"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False

DEFAULT_DUPLICATES_BEFORE_SORT = False
DEFAULT_ASCENDING = True



def sort_list(items, ascending=True, remove_before_sort=False):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")
    
    if remove_before_sort:
        items = list(set(items))
        
    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES

    remove_duplicates_before_sort = DEFAULT_DUPLICATES_BEFORE_SORT
    if len(sys.argv) == 4:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        remove_duplicates_before_sort = sys.argv[3].lower() == "yes"
    else:
        print("Se debe indicar el fichero como primer argumento")
        print("El segundo argumento indica si se quieren eliminar duplicados")
        print("El tercer argumento indica si se quieren eliminar duplicados antes de imprimir")
        sys.exit(1)

    print(f"Se leerán las palabras del fichero {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"El fichero {filename} no existe")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates and not remove_duplicates_before_sort:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list, remove_before_sort=remove_duplicates_before_sort))

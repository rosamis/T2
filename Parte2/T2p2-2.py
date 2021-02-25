import sys
import os
import pefile

def getSections(file_path):
    pe_sections = set([])
    pe = pefile.PE(file_path)
    
    for section in pe.sections:
        pe_sections.add(section.Name.decode("utf-8"))

    return pe_sections

def main(argv):
    first_path = argv[0]
    second_path = argv[1]

    if (not os.path.isfile(first_path)) or (not os.path.isfile(second_path)):
        print("Forneça o caminho de dois arquivos PE")
        sys.exit(0)

    pe_first_sections = getSections(first_path)
    pe_second_sections = getSections(second_path)

    pe_first = pe_first_sections.difference(pe_second_sections)
    pe_second = pe_second_sections.difference(pe_first_sections)

    print("========================\n")
    print("Permissões únicas por PE\n")
    print("========================\n")
    print(f'{first_path}: {list(pe_first)}')
    print(f'{second_path}: {list(pe_second)}')

    intersection = pe_first_sections.intersection(pe_second_sections)

    print("=========================\n")
    print("Permissões comuns dos PEs\n")
    print("=========================\n")
    print(list(intersection))

if __name__ == "__main__":
    main(sys.argv[1:])
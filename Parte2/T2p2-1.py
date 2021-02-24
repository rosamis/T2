#!/usr/bin/python3

import sys
import os
import pefile

EXECUTABLE_SECTION = 0x20000000


def checkExecutable(section):
    characteristics = getattr(section, 'Characteristics')
    if characteristics & EXECUTABLE_SECTION > 0:
        return True

    return False

if __name__ == "__main__":
    file_path = sys.argv[1:][0]

    if os.path.isdir(file_path):
        exe_dict = dict({})
        pe_files = os.listdir(file_path)

        for pe_file in pe_files:
            pe_file_path = str(file_path + "/" + pe_file)
            name = pe_file_path.split('.exe')[0]
            pe = pefile.PE(pe_file_path)
            executables = list([])
            for section in pe.sections:
                if checkExecutable(section):
                    executables.append(section.Name.decode("utf-8"))
            exe_dict[name] = executables

        print("=========================")
        print("Seções executáveis cada PE")
        print("=========================")

        for key in exe_dict:
            print(f'{key}: {exe_dict[key]}')   
    
    elif os.path.isfile(file_path):
        exe_dict = dict({})

        name = file_path.split('.exe')[0]
        pe = pefile.PE(file_path)

        executables = list([])
        for section in pe.sections:
            if checkExecutable(section):
                executables.append(section.Name.decode("utf-8"))
        exe_dict[name] = executables

        print("========================")
        print("Seções executáveis de PE específico")
        print("========================")

        for key in exe_dict:
            print(f'{key}: {exe_dict[key]}')
    
    else:
        print("arquivo PE ou um diretório com arquivos PEs faltando")
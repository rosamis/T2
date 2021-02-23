import xmltodict
import json
import sys
from os import listdir
from os.path import isfile, join

def listFiles(path):
    return [str(f) for f in listdir(path) if isfile(join(path, f))]

def permissionAPK(list_files, name_dir):
    print('===================')
    print('Permissões por APK')
    print('===================')

    total = {}
    for lf in list_files:
        list_permissions = []
        with open(name_dir + '/' + lf) as fd:
            doc = xmltodict.parse(fd.read())
            for d in doc["manifest"]["uses-permission"]:
                for key, value in d.items(): 
                    if 'permission.' in value:
                        if '.' in value.split('permission.')[1]:
                            list_permissions.append(value.split('permission.')[1].split('.')[0])
                        else:
                            list_permissions.append(value.split('permission.')[1])
            file_name = lf.split('AndroidManifest_')[1].replace('.xml','')
            print(file_name,': ', list_permissions)
        total[file_name] = list_permissions

    print('===================')
    print('Permissões únicas por APK')
    print('===================')

    unique_permission = {}
    for key in total.keys():
        temp_dic = total.copy()
        temp_dic.pop(key)
        unique_permission[key] = list(set(total[key]).difference(*temp_dic.values()))
        print(key + ': ', unique_permission[key])

    print('===================')
    print('Permissões comuns das APKs')
    print('===================')

    values_dic = list(total.values())
    common = set(values_dic[0]).intersection(*values_dic[1:])
    print(list(common))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        name_dir = sys.argv[1]
        list_files = listFiles(name_dir)
        permissionAPK(list_files, name_dir)
    else:
        print('Error: missing args')

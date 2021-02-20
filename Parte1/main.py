import xmltodict
import json

# xml_content = open('dataset/finance/AndroidManifest_albert_3.2.1-3210.xml')


with open('dataset/finance/AndroidManifest_albert_3.2.1-3210.xml') as fd:
    doc = xmltodict.parse(fd.read())

print(doc["manifest"]["uses-permission"])
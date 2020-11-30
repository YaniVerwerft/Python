import xml.etree.ElementTree as ET
xmlDoc = ET.parse('drugs.xml')
root = xmlDoc.getroot()
#
# print('root[1].tag: ',root[1].tag)
# print('root[0][3].tag: ',root[0][3].tag)
# print('root[0][3].text: ',root[0][3].text)
# print('root[1][0].text: ',root[1][0].text)
# print('root[1][1][1].text: ',root[1][1][1].text)
# print('root[2][3].text: ',root[2][3].text)

# for leaflet in root.iter('leaflet'):
#         print(leaflet[0].text,' : ',leaflet[3].text)

for leaflet in root.iter('leaflet'):
    print(leaflet[0].text)
    print('\t',leaflet[2].text)
    print('\t','pharmaceutical forms: ')
    for form in leaflet[1]:
        print('\t\t', form.text)
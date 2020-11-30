import xml.etree.ElementTree as ET
xmlDoc = ET.parse('cinemas.xml')
root = xmlDoc.getroot()

print('Bioscopen in Antwerpen')

for bioscoopoverzicht in root:
    print(bioscoopoverzicht[4].text)
    print(bioscoopoverzicht[5].text, bioscoopoverzicht[6].text)
    print(bioscoopoverzicht[7].text, bioscoopoverzicht[8].text,'\n')


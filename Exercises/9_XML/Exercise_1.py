import xml.etree.ElementTree as ET
xmlDoc = ET.parse('plants.xml')
root = xmlDoc.getroot()
counter = 1


for plant in root.iter('plant'):
    naam = plant.find('common')
# for plant in root:
    if plant[3].text == 'SUN':
        print('Plant', counter, ':', naam.text, '(' + plant[1].text.capitalize()+')')
        counter += 1

#find example
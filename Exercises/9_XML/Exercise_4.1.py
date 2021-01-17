import xml.etree.ElementTree as ET
xmlDoc = ET.parse('drugs.xml')
root = xmlDoc.getroot()

for leaflet in root:
    name_drug = leaflet.find('name')
    name_drug.text = name_drug.text.upper()
    forms = leaflet.find('pharmaceutical_forms')
    #forms = leaflet[1]
    leaflet.remove(forms)

xmlDoc.write('drugs_changed.xml')
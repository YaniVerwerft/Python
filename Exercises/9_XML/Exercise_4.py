# output_file = open('drugs_changed.xml', 'w', encoding='UTF-8')
import xml.etree.ElementTree as ET
xmlDoc = ET.parse('drugs.xml')
root = xmlDoc.getroot()

for leaflet in root:
    for pf in leaflet.iter('pharmaceutical_forms'):
        leaflet.remove(pf)







#output_file.write(mydata)
# output_file.close()
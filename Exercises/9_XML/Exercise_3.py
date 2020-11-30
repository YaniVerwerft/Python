import xml.etree.ElementTree as ET
xmlDoc = ET.parse('jobs.xml')
root = xmlDoc.getroot()
counter = 1
for company in root.iter('company'):

    for vacancy in company[2].iter('vacancy'):
        #position = vacancy[0]
        #if position.get('group') == 'IT':
        if vacancy[0].get('group') == 'IT':
            print(str(counter) + '.\t Position:\t' + vacancy[0].text)
            print('\t Company:\t' + company[0].text)
            print('\t Contact:\t' + company[1][1].text + '\n')
            counter += 1





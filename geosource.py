from lxml import etree
import csv

doc = etree.parse(r'k:\researchspace\placeandlabel.xml')

root = doc.getroot()
results = root[1]
output = open(r'k:\researchspace\placeandlabel.csv','a',encoding='utf-8')
print(r'PREFIX thesIdentifier: <http://collection.britishmuseum.org/id/>',file=output)
print(r'PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>',file=output)

line = ''
for result in results:
    for bind in result:
        for triple in bind:

            line = line + str(triple.text) + '^'
    #line = line.replace('http://erlangen-crm.org/current/', 'crm:')

    line = line.replace('http://collection.britishmuseum.org/id/place/','thesIdentifier:')
    #line = line.encode('utf-8')
    print(str(line) + ' \n', end="", file=output)

    line = ''

output.close()

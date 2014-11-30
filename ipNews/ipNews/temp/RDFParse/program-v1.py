__author__ = 'phoenix'

import tarfile
from xml.dom.minidom import parseString

tar = tarfile.open("Dataset/Ontology-1.tar.gz","r:gz")
d_name_code = {}
code = 1
for tarinfo in tar:
	if ".txt" in tarinfo.name:
		d_name_code[code] = [tarinfo.name]
		code = code+1

count = 0
total = 0

for aKey in d_name_code.keys():
    content = tar.extractfile(d_name_code[aKey][0]).read()

    # Take out Headline from each news article - and/or Date (Month Date and Time)
    content_new = content.split('\n')
    element = content_new[0]
    if element.find('Subscri') < 0:
    #rdf file
        # print d_name_code[aKey][0][:-4]
        rdf_input = tar.extractfile(d_name_code[aKey][0][:-4]).read()
        dom = parseString(rdf_input)
        rdfTag = dom.getElementsByTagName('owl:NamedIndividual')[:]
        person = []
        place_1 = []
        place_2 = []
        for tag_1 in rdfTag:
            tag_1 = tag_1.toxml()
            if tag_1.find('pershash') > -1 and tag_1.find('Person') > -1:
                rdfData = [line.replace('<c:name>','').replace('</c:name>','').strip() for line in tag_1.split('\n') if line.find('c:name') > -1]
                if len(rdfData) > 0:
                    person.append(rdfData[0])
            if tag_1.find('provinceorstate') > 1 and tag_1.find('ProvinceOrState') > 1:
                rdfData = [line.replace('<c:name>','').replace('</c:name>','').strip() for line in tag_1.split('\n') if line.find('c:name') > -1]
                if len(rdfData) > 0:
                    place_1.append(rdfData[0])
            if tag_1.find('geo/city') > 1 and tag_1.find('Geo/City') > 1:
                rdfData = [line.replace('<c:name>','').replace('</c:name>','').strip() for line in tag_1.split('\n') if line.find('c:name') > -1]
                if len(rdfData) > 0:
                    place_2.append(rdfData[0])
            if tag_1.find('company') > 1 and tag_1.find('Company') > 1:
                rdfData = [line.replace('<c:name>','').replace('</c:name>','').strip() for line in tag_1.split('\n') if line.find('c:name') > -1]
                if len(rdfData) > 0:
                    place_2.append(rdfData[0])
            if tag_1.find('genericHasher') > 1 and tag_1.find('Facility') > 1:
                rdfData = [line.replace('<c:name>','').replace('</c:name>','').strip() for line in tag_1.split('\n') if line.find('c:name') > -1]
                if len(rdfData) > 0:
                    place_2.append(rdfData[0])

        total += 1
        if len(person) + len(place_1) + len(place_2) > 0:
            f_write_name = 'Dataset/Ontology-1/' + str(aKey)
            f_write = open(f_write_name, 'w')
            if len(person) > 0:
                f_write.write(str(person) + '\n')
            else:
                f_write.write('\n')

            if len(place_1) > 0:
                f_write.write(str(place_1) + '\n')
            else:
                f_write.write('\n')

            if len(place_2) > 0:
                f_write.write(str(place_2) + '\n')
            else:
                f_write.write('\n')

            f_write.write('\n' + content.strip())

    # any modifications on the whole text go here
	#content = clean_array(content)
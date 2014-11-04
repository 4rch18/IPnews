import rdfxml
import json
from pprint import pprint


class Sink(object):
    def __init__(self): self.result = []

    def triple(self, s, p, o): self.result.append((s, p, o))


def rdfToPython(s, base=None):
    sink = Sink()
    return rdfxml.parseRDF(s, base=None, sink=sink).result


f = open('test2', 'r')
str = f.read()
strL = str.split("\n")
#print strL

f.close()

s_rdf = str
pyth = rdfToPython(s_rdf)
s_jsn = json.dumps(pyth)

f_jsn = open('test.json', 'w')
f_jsn.write(s_jsn)
f_jsn.close()
# print s_jsn

json_data = open('test.json')
data = json.load(json_data)
json_data.close()
#pprint(data[0])
print(len(data))

for i in range(len(data)):
    if data[i][1].find('categoryName') > -1:
        data[i][1] = u'Category'
        data[i][2] = data[i][2].replace('\"', '')
        data[i].remove(data[i][0])
        print data[i]

    #for j in range(len(data[i])):
        #if data[i][j].find('Person') > -1:
         #   data[i][j] = u'Person'
          #  print data[i]
        #if data[i][j].find('personType') > -1:
         #   print data[i]
        #if data[i][j].find('ProvinceOrState') > -1:
            #print data[i]


for i in range(len(strL)):
    if strL[i].find('Person: ') > -1 and len(strL[i]) < 200:
        print strL[i]
    if strL[i].find('ProvinceOrState: ') > -1 and len(strL[i]) < 200:
        print strL[i]
            #print(data)

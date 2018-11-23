import xml.etree.ElementTree


root = xml.etree.ElementTree.parse("myXML.xml")
# nodes = root.getiterator()


ele = root.findall(".//age")
print(ele)

ele1 = root.findall("Student")
print(ele1)

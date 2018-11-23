import xml.etree.ElementTree


root = xml.etree.ElementTree.parse("myXML.xml")
nodes = root.getiterator()

for items in nodes:
    if items.text and items.attrib:
        print("{0}---{1}---{2}".format(items.tag, items.text, items.attrib))

print("#" * 30)


# ele = root.findall("name")
# for v in ele:
#     print("{0}====={1}".format(v.tag, v.text))


print("#" * 30)
ele_name = root.find("name")
print(ele_name)

ele = root.findall("name")
print(ele)
# print(ele_name, ele_name.tag, ele_name.text, sep="///")

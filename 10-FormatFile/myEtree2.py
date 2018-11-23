import xml.etree.ElementTree as et


tree = et.parse("myXML.xml")

tree_it = tree.getiterator()
#print(tree_it)

root = tree.getroot()
#print(root)

for e in root.iter("name"):
    print(e.text)

for stu in root.iter("Student"):
    print(stu.tag, stu.find("name"))
    name = stu.find("name")
    if name:
        # name.set("test", name.text * 2)
        name.remove("test")

stu = root.find("Student")

e = et.Element("Adder")
e.attrib = {"attr":"OK..."}
e.text = "Nothing special"

stu.append(e)

tree.write("myXML.xml")
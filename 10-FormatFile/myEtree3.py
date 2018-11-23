import xml.etree.ElementTree as et

# with open ('etree3.xml', 'a+', encoding='utf-8') as f:
#tree = et.parse('etree3.xml')

root = et.Element("School")

grade = et.SubElement(root, "Grade")
grade.attrib = {"Junior":"4"}
grade.text = "C4"

teacher = et.SubElement(grade, "Teacher")
teacher.text = "Yz"

tree = et.ElementTree(root)
tree.write("etree3.xml", encoding='utf-8', xml_declaration=True)

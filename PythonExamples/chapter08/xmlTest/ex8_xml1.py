#my.xml을 가지고 값얻어오기 연습
import xml.etree.ElementTree as etree

xmlfile = etree.parse("my.xml")
#etree.dump(xmlfile)

root = xmlfile.getroot()
print(root.tag)

print()
print(root[0].tag)
print(root[1].tag)

print('\n----요소와 속성 읽기----')
print(root[0][0].tag)
print(root[0][1].tag)
print(root[0][2].tag)

print()
print(root[0][2].attrib.keys())
print("리스트로 형변환 : ", list(root[0][2].attrib.keys()))
print(root[0][2].attrib.values())
print("키가 kor인 value :", root[0][2].attrib.get("kor"))

print()
temp = list(root[0][2].attrib.values())
print(temp[0]+" "+temp[1])

print()
myname=root.find("item").find("name").text
mytel=root.find("item").find("tel").text
print(myname + "," + mytel)

print("\n----반복 처리----")
for child in root:
    print(child.tag)
    for child2 in child:
        print("tag : {}, attribute : {}".format(child2.tag, child2.attrib))
    print()

print("\n----특정 요소 속성 읽기----")
for a in root.iter('exam'):
    print(a.attrib)
    
print('\n----특정 요소값 읽기----')
children = root.getchildren()
#children = rootfindall('item')     #위와 같은 결과를 얻음
for it in children:
    re_id=it.find('name').get('id')
    re_name=it.find('name').text
    re_tel=it.find('tel').text
    print(re_id, re_name, re_tel)
# 
# 
# print()
# print(root[0][0].tag)
# print(root[0][1].tag)
# print(root[0][2].tag)

import xml.etree.ElementTree as ET

postMap = ET.parse("locations.xml")
postMapRoot = postMap.getroot()

county = {}

for postObject in postMapRoot:
    if postObject[3].text == "EE":
        if postObject[4].text in county:
            county[postObject[4].text] += 1
        else:
            county[postObject[4].text] = 1

print(county)
import xml.etree.ElementTree as ET

postMap = ET.parse("locations.xml")
postMapRoot = postMap.getroot()

i = 0

for postObject in postMapRoot:
    if postObject[2].text == str(0) and postObject[3].text == "EE":
        i += 1

print("Post automats in Estonia: ",i)
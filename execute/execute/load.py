import requests
import json
from jsonmerge import merge
import xml.etree.ElementTree as ET

dict = {"en":{},"id":{}}
mytree = ET.parse('/Users/phamhaituan/Documents/PROJECTS/TelkomselAutomationTest/Phincon-AutoTest/SourceCode/PhinconAutoTest/variables/language/temp/Android/en.xml')
myroot = mytree.getroot()

for x in myroot:
     dict["en"][x.attrib["name"]] = x.text


mytree = ET.parse('/Users/phamhaituan/Documents/PROJECTS/TelkomselAutomationTest/Phincon-AutoTest/SourceCode/PhinconAutoTest/variables/language/temp/Android/id.xml')
myroot = mytree.getroot()

for x in myroot:
     dict["id"][x.attrib["name"]] = x.text



data = json.load(open('/Users/phamhaituan/Documents/PROJECTS/TelkomselAutomationTest/Phincon-AutoTest/SourceCode/PhinconAutoTest/variables/language/wcmstranslation.json') )
base = data

response = requests.get("https://tdwstcontent.telkomsel.com/api/translation/all/mobile")
json = response.json()
head = json
result = merge(merge(dict, base), head)
langEN = result["en"]
langID = result["id"]

def getLanguageText(key):
     if key in langEN :
          return langEN[key]
     else:
          return 'WCMS not contain key : '+key
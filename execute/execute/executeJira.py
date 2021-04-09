from jira import JIRA
from parserResult import Config
from parserResult import Suite
from parserResult import TestCase
from parserResult import TestStep
from parserResult import ParserRobotXML



import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))



HOST = 'https://team-1617605645510.atlassian.net/'
UserName = 'sanjayastephen5@gmail.com'
Token   = '8BqeTaz63UBDD3oh2Slr3986'
ReportPath = sys.argv[1]

xmlPath = sys.argv[2]

ConfigFile = sys.argv[3]
DeviceName = sys.argv[4]

# f = open(ConfigFile, "r")
# DeviceTest = f.read()
postString = "No Config Now" #DeviceTest.split("\n",1)[1]
print(postString)
preconfig = '==========>Device Test Information<============' +'\n'
preconfig += postString
preconfig += '\n'
preconfig += '\n'



result = ParserRobotXML(xmlPath)

testCaseFail = result.getFailCases()

print(testCaseFail.count)
jira = JIRA(server= HOST,basic_auth=(UserName, Token))


for tc in testCaseFail:
    
    new_issue = jira.create_issue(project='MST', summary='['+DeviceName+']'+tc.testName, description=preconfig + tc.getStringTestCase(), issuetype={'name': 'Bug'})
    fileName = "" #tc.captureScreen
    if fileName != "":
        path = ReportPath+fileName
        print(path)
        # jira.add_attachment(issue=new_issue, attachment=path)
        with open(path, 'rb') as f:
            jira.add_attachment(issue=new_issue, attachment=f)
    
    # parent_issue = jira.issue('AUTO-135')
    # jira.create_issue_link('tests', new_issue, parent_issue, None)
    break                  
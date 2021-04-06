import xml.etree.ElementTree as ET
import json
from load import getLanguageText

class Config(object):
    # generator=''
    # generated = ''
    # suites = []
    # statistics = {}
    # errors = {}
    def __init__(self):
        self.suites = []

    def parserInfomation(self, att):
        self.generator = att['generator']
        self.generated = att['generated']

    def parserStatics(self, statistics):
        self.statistics = statistics

    def parserError(self, errors):
        self.errors = errors
        
    def parserSuits(self, element):
        suite = Suite()
        suite.config = self
        suite.parseSuite(element)
        self.suites.append(suite)

class Suite(object):
    # id =''
    # name= ''
    # source =''
    # status = ''
    # starttime = ''
    # endtime = ''
    # suites = []
    # testCases = []
    # setup   = ''
    # teardown   = ''
    
    def __init__(self):
        self.suites = []
        self.testCases = []

    def parseSuite(self, element):
        self.id = element.attrib['id']
        self.name = element.attrib['name']
        self.source = element.attrib['source']
        

        for child in element:
            if child.tag == 'suite' :
                self.parserChildSuite(child)
            elif child.tag == 'test' :
                self.parserTestCases(child)
            elif child.tag == 'status' :
                self.status = child.attrib['status']
                self.starttime = child.attrib['starttime']
                self.endtime = child.attrib['endtime']
            elif child.tag == 'kw' :
                if child.attrib['type'] == 'setup' :
                    self.setup = child.attrib['name']
                elif child.attrib['type'] == 'teardown' :
                    self.teardown = child.attrib['name']
            

    def parserChildSuite(self, element):
        suite = Suite()
        suite.parseSuite(element)
        self.suites.append(suite)

    def parserTestCases(self, element):
        tc = TestCase()
        tc.suit = self
        tc.parseTestCase(element)
        self.testCases.append(tc)

class TestCase(object):
    # suit = ''
    # testName = ''
    # status = ''
    # starttime = ''
    # endtime = ''

    # testSteps = []
    # tags = []

    def __init__(self):
        self.testSteps = []
        self.tags = []
        self.doc = ''

    def getStringTestCase(self):
        strTestCase = '*' + self.testName + '*' +'\n'
        strTestCase += self.doc + '\n'
        strTestCase += 'Build Number : TBD' + '\n'
        strTestCase += 'Date Time : '+self.starttime + '\n'+ '\n'
        strTestCase += '||*No.*||*Step*||*Agruments*||*Status*||' +'\n'
        failStep = ''
        index = 1
        for ts in self.testSteps:
            if ts.status == 'FAIL':
                failStep = ts
            strTestCase = strTestCase + '|%d|' % (index) + ts.getStringStep() + '\n'
            index += 1

        if failStep != '':
            strTestCase += failStep.getDetailFailCase()
            self.captureScreen = failStep.getCaptureScreenImage()
        return strTestCase

    def parseTestCase(self, element):
        self.testName = element.attrib['name']
        for child in element:
            if child.tag == 'status' :
                self.status = child.attrib['status']
                self.starttime = child.attrib['starttime']
                self.endtime = child.attrib['endtime']
            elif child.tag == 'tags' :
                print(child.attrib)
            elif child.tag == 'kw' :
                self.parserTestStep(child)
            elif child.tag == 'doc' :
                self.doc = child.text
        
    
    def parserTestStep(self, element):
        ts = TestStep()
        ts.parseTestStep(element)
        self.testSteps.append(ts)


class TestStep(object):
    # name = ''
    # status = ''
    # starttime = ''
    # endtime = ''
    # doc = ''
    # msg = ''
    # arguments = {}
    # subTestSteps = []
    


    def __init__(self):
        self.subTestSteps = []
        self.arguments = ''
        self.doc = ''
        self.msg = ''
        self.img = ''

    def getStringStep(self):
        strStatus = ''
        detailFail = ''
        if self.status == 'PASS':
            strStatus = "*{color:green}" + self.status + "{color}*"
        elif self.status == 'FAIL':
            strStatus = "*{color:red}" + self.status + "{color}*"
            detailFail = self.msg
        else:
            strStatus = "*{color:orange}" + self.status + "{color}*"
            detailFail = self.msg

        agr = self.arguments

        stepStr = '|'

        stepStr += self.name 

        if detailFail != "":
            stepStr += '{quote}' + detailFail + '{quote}'

        if agr != '' :
            stepStr += '|' + agr + '|'
        else:
            stepStr += '|' + ' ' + '|'

        stepStr += '|' + strStatus + '|'
        

        return stepStr

    def getDetailFailCase(self):
        stepStr = ''
        if self.status == 'FAIL':
            agr = self.arguments
            stepStr += '*{color:red} =====> TEST CASE FAIL <=====  {color}* \n'
            stepStr += 'TEST STEP : '+ self.name +'\n'
            stepStr += 'Arugment : ' + agr +'\n'
            stepStr += 'Doc : ' + self.doc +'\n'
            stepStr += 'Message : ' + self.msg +'\n'
            stepStr += self.getTestStepFail(self)
            # for ts in self.subTestSteps:
            #     if s.name == "Capture Page Screenshot":
            #         stepStr = stepStr + ts.getCaptureScreen() + '\n'
            #     else:
            #         stepStr = stepStr + ts.getStringStep() + '\n'
            #     if ts.status == 'FAIL':
            #         for s in ts.subTestSteps:
            #             if s.name == "Capture Page Screenshot":
            #                 stepStr = stepStr + s.getCaptureScreen() + '\n'
            #             else:
            #                 stepStr = stepStr + s.getStringStep() + '\n'
        return stepStr

    def getTestStepFail(self,subTestStep):
        stepStr = ''
        for ts in subTestStep.subTestSteps:
            if ts.name == "Capture Page Screenshot":
                stepStr = stepStr + ts.getCaptureScreen() + '\n'
            else:
                stepStr = stepStr + ts.getStringStep() + '\n'
            if ts.status == 'FAIL':
                if len(ts.subTestSteps) > 0 :
                    stepStr += self.getTestStepFail(ts)
        return stepStr

    def getCaptureScreen(self):
        strStatus = ''
        detailFail = ''
        if self.status == 'PASS':
            strStatus = "*{color:green}" + self.status + "{color}*"
        else:
            strStatus = "*{color:red}" + self.status + "{color}*"
            detailFail = self.msg

        agr = self.arguments

        stepStr = '|'

        stepStr += self.name 

        if detailFail != "":
            stepStr += '{quote}' + detailFail + '{quote}'

        if self.img != '' :
            stepStr += '| !' + self.img + '! |'
        else:
            stepStr += '|' + ' ' + '|'

        stepStr += '|' + strStatus + '|'
        

        return stepStr

    def parseTestStep(self, element):
        self.name = element.attrib['name']
        for child in element:
            if child.tag == 'status' :
                self.status = child.attrib['status']
                self.starttime = child.attrib['starttime']
                self.endtime = child.attrib['endtime']
            elif child.tag == 'doc' :
                self.doc = child.text
            elif child.tag == 'arguments' :
                print(child.tag)
                for sc in child:
                    print(self.correctArg(sc.text))
                    self.arguments += self.correctArg(sc.text) + '\t'
            elif child.tag == 'arg' :
                print(self.correctArg(child.text))
                self.arguments += self.correctArg(child.text) + '\t'
            elif child.tag == 'kw' :
                self.parserTestStep(child)
            elif child.tag == 'msg' :
                self.msg = child.text
                if self.name == "Capture Page Screenshot":
                    self.subImagePath(self.msg)
            
    def correctArg(self, textAgr):
        temp = textAgr
        result = temp.find('WCMS')
        if result >= 0:
            temp = temp.replace('${WCMS["','')
            temp = temp.replace('"]}','')
            return getLanguageText(temp)
        return temp

    def subImagePath(self,msg):
        pre = 'img src="'
        result = msg.index(pre)
        sub = msg[result::]
        sub = sub.replace(pre,'')
        result = sub.index('"')
        strResult = sub[:result]
        self.img = strResult
        print(self.img)

    def getCaptureScreenImage(self):
        imgPath = ''
        if self.img == "":
            for ts in self.subTestSteps:
                path = ts.getCaptureScreenImage()
                if path != '':
                    imgPath = path
        else:
            imgPath = self.img
        return imgPath

    def parserTestStep(self, element):
        ts = TestStep()
        ts.parseTestStep(element)
        self.subTestSteps.append(ts)

class ParserRobotXML(object):
    rootResult = Config()
    def __init__(self, path):
        tree = ET.parse(path)
        root = tree.getroot()
       
        self._handlerRoot(root)
        
    def _handlerRoot(self, element):
        self.rootResult.result = element.attrib
        for child in element:
            if child.tag == 'suite' :
                self.rootResult.parserSuits(child)
            elif child.tag == 'statistics' :
                self.rootResult.parserStatics(child.attrib)
            elif child.tag == 'errors' :
                self.rootResult.parserError(child.attrib) 
        
    def getFailCases(self):
        testCaseFail = []
        print(self.rootResult.suites.count)
        for suite in self.rootResult.suites:
            fail = self._getFailCasesInSuite(suite)
            for tc in fail:
                testCaseFail.append(tc)
        return testCaseFail

    def _getFailCasesInSuite(self, suite):
        failCases = []
       
        for tc in suite.testCases:
          
            if tc.status == 'FAIL':
                failCases.append(tc)
        
        for s in suite.suites:
            fail = self._getFailCasesInSuite(s)
            for tc in fail:
                failCases.append(tc)

        return failCases 
            





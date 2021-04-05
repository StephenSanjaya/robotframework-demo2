*** Settings ***
Documentation       Test and verify if login is invalid & fetch data from json file
Resource            001_resource.robot
Suite Setup         Json File
Library             JSONLibrary

*** Test Cases ***
Check Login For Invalid Crendential Through Json File
    FOR    ${i}    IN RANGE     ${lengthOfData}
            Open Saucedemo Application
            Run Keyword And Continue On Failure
...         Login Template  ${data["users"][${i}]["username"]}  
...                         ${data["users"][${i}]["password"]}     
...                         ${data["users"][${i}]["error"]}
            Close Application
    END

*** Keywords ***
Wait Until Saucedemo Image Show
    Wait Until Element Is Visible   //android.view.ViewGroup/android.widget.ImageView[@index='0']

Json File
    ${json_obj}=    Load JSON From File         ./Data_Set/users.json
    ${json_str}=	Convert JSON To String	    ${json_obj}

    ${data}=    evaluate        json.loads('''${json_str}''')    json
    ${lengthOfData}=  Get length      ${data["users"]}
    Set Global Variable         ${data}
    Set Global Variable         ${lengthOfData}

Login Template
    [Arguments]     ${username}     ${password}     ${error}
    Input Username      ${username}
    Input Password      ${password}
    Click Login Button
    Login Should Fail   ${error}

Login Should Fail
    [Arguments]     ${msg}    
    Wait Until Element Is Visible   //android.view.ViewGroup[@content-desc="test-Error message"]
    ${text}=            Get Text            //android.view.ViewGroup[@content-desc="test-Error message"]/android.widget.TextView[@index='0']
    Should Be Equal     ${msg}      ${text}

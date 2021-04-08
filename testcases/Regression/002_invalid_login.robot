*** Settings ***
Documentation       Test and verify if login is invalid
# Library             DataDriver      ../Data_Set/login_data.csv
Library             DataDriver      ../../Data_Set/login_data_excel.xlsx  Sheet_name=Sheet1
Resource            ../CommonKeyword.robot
# Suite Setup         Open App
# Suite Teardown      Close Application
Test Setup          Initialize System
Test Teardown       Close Application
Test Template       Login Template

*** Test Cases ***                      USERNAME        PASSWORD        ERROR
Check Login For Invalid Crendential    ${username}     ${password}     ${error}

*** Keywords ***
Login Template
    [Arguments]     ${username}     ${password}     ${error}
    Input Username      ${username}
    Input Password      ${password}
    Click Login Button
    Login Should Fail   ${error}

Login Should Fail
    [Arguments]     ${msg}    
    Wait Until Element Is Visible           ${element_error_message}
    ${text}=            Get Text            ${txt_error_message}
    Should Be Equal     ${msg}      ${text}

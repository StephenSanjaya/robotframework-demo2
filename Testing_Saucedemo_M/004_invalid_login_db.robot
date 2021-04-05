*** Settings ***
Documentation       Test and verify if login is invalid & fetch data from database
Library             DatabaseLibrary
Resource            001_resource.robot
Suite Setup     Run Keywords  Connect To Database     pymysql      ${db_name}  ${db_user}  
...             ${db_pasword}   ${db_host}  ${db_port}   AND  Fetch Data  AND  Row Count In Users Table
Suite Teardown  Disconnect From Database

*** Variables ***
${db_name}          db_test
${db_user}          root
${db_pasword}       
${db_host}          127.0.0.1
${db_port}          3306

*** Test Cases ***
Check Login For Invalid Crendential Through Database
    FOR    ${i}    IN RANGE     ${lengthOfData}
            Open Saucedemo Application
            Run Keyword And Continue On Failure
...         Login Template  ${queryResults[${i}][0]}
...                         ${queryResults[${i}][1]}     
...                         ${queryResults[${i}][2]}
            Close Application
    END

*** Keywords ***
Wait Until Saucedemo Image Show
    Wait Until Element Is Visible   //android.view.ViewGroup/android.widget.ImageView[@index='0']
    
Fetch Data
    ${queryResults}	        Query	    select username, password, error from users
    Set Global Variable     ${queryResults}

Row Count In Users Table
    ${lengthOfData}	            Row Count	select * from users
    Set Global Variable     ${lengthOfData}

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
    
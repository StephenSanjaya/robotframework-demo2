*** Settings ***
Resource            ../CommonKeyword.robot
Suite Setup     Initialize System

*** Test Cases ***
Input Valid Crendential
    Input Username          ${VALID_USERNAME}
    Input Password          ${VALID_PASSWORD}
    Click Login Button
    Login Should Success
    Capture Page Screenshot

*** Keywords ***
Login Should Success
    Wait Until Element Is Visible       ${txt_title}   
    ${text}=            Get Text        ${txt_title}   
    Should be Equal     ${text}         PRODUCTS
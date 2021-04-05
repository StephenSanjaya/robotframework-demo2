*** Settings ***
Resource        001_resource.robot
Suite Setup     Open Saucedemo Application

*** Test Cases ***
Input Valid Crendential
    Input Username          ${VALID_USERNAME}
    Input Password          ${VALID_PASSWORD}
    Click Login Button
    Login Should Success

*** Keywords ***
Login Should Success
    Wait Until Element Is Visible       ${txt_title}   
    ${text}=            Get Text        ${txt_title}   
    Should be Equal     ${text}         PRODUCTS
*** Settings ***
Library         AppiumLibrary       run_on_failure=Nothing
Variables       ../Library/locators.py
Resource        ../resources/controller.robot

*** Variables ***
${VALID_USERNAME}       standard_user
${VALID_PASSWORD}       secret_sauce

*** Keywords ***
Initialize System
    Open App  
    Wait Until Saucedemo Image Show

Wait Until Saucedemo Image Show
    Wait Until Element Is Visible   ${element_image_saucedemo}

Input Username
    [Arguments]     ${username}
    Input Text          ${txt_username}     ${username}

Input Password
    [Arguments]     ${password}
    Input Text          ${txt_password}     ${password}

Click Login Button
    Click Element         ${btn_login}
*** Settings ***
Library         AppiumLibrary       run_on_failure=Nothing
Variables       ../Library/locators.py

*** Variables ***
${REMOTE_URL}           http://127.0.0.1:4723/wd/hub
${PLATFORM_NAME}        Android
${PLATFORM_VERSION}     7.0
${DEVICE_NAME}          emulator-5554
${APP_ACTIVITY}         com.swaglabsmobileapp.SplashActivity
${APP_PACKAGE}          com.swaglabsmobileapp
${VALID_USERNAME}       standard_user
${VALID_PASSWORD}       secret_sauce

*** Keywords ***
Open Saucedemo Application
    Open Application            ${REMOTE_URL}
...                             platformName=${PLATFORM_NAME}
...                             platformVersion=${PLATFORM_VERSION}
...                             deviceName=${DEVICE_NAME}
...                             automationName=UiAutomator2
...                             appActivity=${APP_ACTIVITY}
...                             appPackage=${APP_PACKAGE}
    Wait Until Saucedemo Image Show

Start Appium Server
    Start Server
    Sleep           5s

Stop Appium Server
    Stop Server
    Sleep           5s

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
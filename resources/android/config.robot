*** Settings ***
Library    AppiumLibrary
Library    BuiltIn

*** Variables ***
${Activity_Login}       com.swaglabsmobileapp.MainActivity
${REMOTE_URL}           http://127.0.0.1:${port}/wd/hub

*** Keywords ***
Open App
    [Arguments]    ${appActivity}=${Activity_Login}
    open application            ${REMOTE_URL}  
    ...  automationName=${AUTOMATION_NAME}
    ...  app=${APP}  platformName=${PLATFORM_NAME}  platformVersion=${PLATFORM_VERSION}
    ...  appPackage=${APP_PACKAGE}
    ...  appActivity=${appActivity}
    ...  deviceName=${Device_Name}
    ...  noReset=true
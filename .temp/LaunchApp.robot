

*** Settings ***
Resource    ./CommonKeyword.robot
Resource    ../Library/locators.robot

Suite Setup         Open App      ${EMPTY}
Suite Teardown      Close Application
# Test Setup          Launch Application
# Test Teardown       Tear Down Test Cases

*** Keywords ***

*** Test Cases ***
Launch App And PreSetup
    [Tags]    Init
    Initialize System
    BuiltIn.Sleep   20
    
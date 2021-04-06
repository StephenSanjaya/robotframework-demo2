*** Settings ***
Resource            001_resource.robot

*** Test Cases ***
Order The Expensive Item
    Click Filter 
    Click Price (high to low)
    Click Add To Cart
    Click Cart
    Click Checkout 
    Wait Until Element Is Visible   ${txt_firstname}
    Input Valid Information  stepen  sanjaya  11111
    Click Continue
    Click Finish
    Close Application

*** Keywords ***
Click Filter 
    Click Element       ${iv_filter}

Click Price (high to low)
    Wait Until Element Is Visible   ${vg_high_to_low}
    Click Element                   ${vg_high_to_low}

Click Add To Cart
    Wait Until Element Is Visible   ${vg_add_to_cart}
    Click Element                   ${vg_add_to_cart}

Click Cart
    Click Element                   ${btn_cart}

Click Checkout 
    Wait Until Element Is Visible   ${txt_title_yourcart}    
    Swipe By Percent	            50	90	50	35
    Wait Until Element Is Visible   ${btn_checkout}
    Click Element                   ${btn_checkout}

Input Valid Information
    [Arguments]     ${firstname}    ${lastname}     ${postalcode}
    Input Text     ${txt_firstname}     ${firstname}
    Input Text     ${txt_lastname}      ${lastname}
    Input Text     ${txt_postalcode}    ${postalcode}

Click Continue
    Click Element       ${btn_continue}

Click Finish
    Wait Until Element Is Visible   ${txt_checkout_overview}
    Swipe By Percent                50	90	50	30
    Wait Until Element Is Visible   ${btn_finish}
    Click Element                   ${btn_finish}
    Checkout should be success

Checkout should be success
    Wait Until Element Is Visible       ${txt_checkout_complete}
    ${text}=            Get Text        ${txt_checkout_complete}
    Should be equal     ${text}         CHECKOUT: COMPLETE!
*** Settings ***
Library    AppiumLibrary    run_on_failure=Nothing
Library    String

Resource    ../resources/devices/${device}.robot
Resource    ../resources/${ENV}/config.robot

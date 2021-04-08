
echo %path%
set DeviceName=sm_android_API10
set OutputFolder=report\

set port=4725
@REM set TAG=Inbox


set projectFolder=.\

set tc=%projectFolder%testcases\
set report=%projectFolder%report\
mkdir %report%

echo %tc%
set i = %DeviceName%
set output=%OutputFolder%
mkdir %output%
set fail=fail


start cmd /k appium --address 0.0.0.0 --port %port%


robot --variable device:%DeviceName% --variable port:%port%  --output %output%output --log %output%output   %tc%




@REM echo 'Start push bug Jira'
@REM set jira=%projectFolder%execute\executeJira.py
@REM set xmlfile=%output%output.xml
@REM python %jira% %output% %xmlfile% %DeviceName% 
@REM echo 'Done push bug Jira'

exit 0


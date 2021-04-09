set port=4725


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


robot --variable device:%DeviceName% --variable port:%port% --output %output%output --log %output%output   %tc%


@REM echo 'Start push bug Jira'
@REM set jira=%projectFolder%execute\executeJira.py
@REM set xmlfile=%output%output.xml
@REM python %jira% %output% %xmlfile% %DeviceName% 
@REM echo 'Done push bug Jira'

echo 'Start push bug Jira'
set jira=%projectFolder%execute\execute\executeJira.py
set xmlfile=%output%output.xml
python %jira% %output% %xmlfile% "%WORKSPACE%\resources\devices\%DeviceName%.robot"  %DeviceName%
echo 'Done push bug Jira'

exit 0


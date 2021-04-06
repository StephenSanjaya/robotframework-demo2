#! /bin/bash -x

projectFolder="/Users/phamhaituan/Documents/PROJECTS/TelkomselAutomationTest/Phincon-AutoTest/SourceCode/PhinconAutoTest/"
tc=$projectFolder"testcases"
dt=`date '+%d%m%Y_%H%M%S'`
report=$projectFolder"report/$dt"
mkdir $report
port=4725
lang=en
TAG=Inbox
for i in sm_iOS_14
do
   output=$report"/$i/"
   mkdir $output
   # Start Server
   osascript -e "tell application \"Terminal\" to do script \"appium --address 0.0.0.0 --port $port\""

   sleep 5
   # Start execute test
   osascript -e "tell application \"Terminal\" to do script \"cd $tc; robot --variable device:$i --variable port:$port --variable lang:$lang --output $output$i --log $output$i --include $TAG .\""

   let "port += 1"
done
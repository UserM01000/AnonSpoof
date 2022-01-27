#!/bin/bash

trap ctrl_c INT
ctrl_c() {
clear
echo "(Ctrl + C ) Detected"
echo "Script stopping..."
sleep 2
sleep 1
clear
echo ""
echo "Thanks for using AnonSpoof :D"
echo ""
exit
}
clear
echo -n "
    _                      ____                     __
   / \   _ __   ___  _ __ / ___| _ __   ___   ___  / _|
  / _ \ | '_ \ / _ \| '_ \\\___ \| '_ \ / _ \ / _ \| |_
 / ___ \| | | | (_) | | | |___) | |_) | (_) | (_) |  _|
/_/   \_\_| |_|\___/|_| |_|____/| .__/ \___/ \___/|_|
                                |_| ----> https://t.me/HackForAll1

"
echo -e "\nYOU CAN ONLY SEND ONE SMS EVERY 24 HOURS\n"

echo -e "WRITE THE NUMBER MORE WITH THE COUNTRY CODE\n"
read -e -p "NUMBER: " numero

read -e -p "MESSAGE: " mensaje


result=$(curl -# -X POST https://textbelt.com/text --data-urlencode phone="$PHONE" --data-urlencode message="$SMS" -d key=textbelt)

if grep -q true <<<"$result"

then
    clear
    echo ""
    echo "SUCCESS --> SMS sent"
    echo ""

elif grep -q "Only one test text message is allowed per day" <<<"$result"

then
    clear
    echo ""
    echo "One sms for day"
    echo ""

else
    clear
    echo ""
    echo "FAIL --> SMS not sent"
    echo ""

fi


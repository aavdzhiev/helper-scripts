#!/bin/bash
adb devices | sed -n '2,$p'| awk '{print $1}' > devices.list


device=''
num_of_devices=$(wc --lines < devices.list)

if [ $num_of_devices -gt 2 ]
then 

	select ip in $(cat devices.list) exit; do 
	   case $ip in
	      exit) echo "exiting"
		    exit 1 ;;
	      *) device=$ip;
		    break ;;
	   esac
	done
else
	device=$(head -n 1 devices.list)
fi

echo "Installing on device $device"
adb -s $device install "$1"

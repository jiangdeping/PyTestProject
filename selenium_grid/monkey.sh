#/bin/bash
devices=`adb devices|grep 'device\>'|awk '{print $1}'`
for device in $devices
	do
	echo $device
	{ nohup adb -s $device shell monkey -p com.xueqiu.android --pct-touch 30 --pct-motion 20 --pct-trackball 30 --pct-majornav 20 -v --throttle 50 100 &}
	done


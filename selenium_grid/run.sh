for i in `adb devices |grep 'device\>'|awk '{print $1}'`
do
	echo $i
	#${i/:/-} 处理字符':'
	udid=$i pytest -v -s test_case.py --alluredir ./result_${i/:/-} &
done

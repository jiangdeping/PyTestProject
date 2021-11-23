#!/bin/bash
rand(){
#// /处理空格  local声明局部变量
local seeds=`while read line;do echo ${line// /};done < tmp.txt`
local count=0
#不停的筛选，直到只剩下一个人
while [[ $count != 1 ]];do
 #猜拳操作，是1增留下，是0则淘汰
  seeds=`for seed in $seeds;do (($RANDOM%2)) &&echo $seed; done`
 #计算当前剩余人数
  count=`echo "$seeds"|wc -l`
done
 if [[ $seeds == ""  ]];then
   rand
#!/bin/bash
rand(){
#// /处理空格  local声明局部变量
local seeds=`while read line;do echo ${line// /};done < tmp.txt`
local count=0
#不停的筛选，直到只剩下一个人
while [[ $count != 1 ]];do
 #猜拳操作，是1增留下，是0则淘汰
  seeds=`for seed in $seeds;do (($RANDOM%2)) &&echo $seed; done`
 #计算当前剩余人数
  count=`echo "$seeds"|wc -l`
done
 if [[ $seeds == ""  ]];then
   rand
else
  echo $seeds
fi
}
#中奖人数通过传参控制
res(){
        for((i=0;i<$1;i++));do
        tmp=`rand`
        while [[ `duplicate $tmp` == 0 ]];do
        tmp=`rand`
        done
        arrs[$i]=$tmp
        done
        echo ${arrs[@]}
}
#中奖人数去重
duplicate()
{
for arr in ${arrs[@]};do
if [[ $arr == $1 ]];then
echo 0;  #如果相同 输出为0
return 0; #结束函数
fi
 done
 echo 1;  #如果不相同 输出为1
}

res $1


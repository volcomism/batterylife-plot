#!/bin/sh
i=`date '+%s'`
j=`/usr/sbin/ioreg -l | grep \"CycleCount | sed 's/^.*\=.//'`
k=`/usr/sbin/ioreg -l | grep \"MaxCapacity | sed 's/^.*\=.//'`
echo $i $k $j >> /opt/batlife.log

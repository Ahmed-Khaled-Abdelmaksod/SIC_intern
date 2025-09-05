#!/bin/bash
while true;do
	echo "Sensor Reading : $RANDOM" >> ../logs/temperature.log 
	sleep 5
done

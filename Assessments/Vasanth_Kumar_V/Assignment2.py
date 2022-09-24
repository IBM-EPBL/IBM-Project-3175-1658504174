#Assignment2
#Problem statement: write a python code to detect high temperature and generate an alarm

import random
import time

temperature = range(10,45) #temperature in degree celsius
humidity = range(0,100)	#humidity in percentage

while True:
	time.sleep(5)	#create a delay of 5s to imitate temperature update every 5s
	current_temp=random.choice(temperature)	#pick a random temperature
	current_hum = random.choice(humidity)	#pick a random humidity
	
	print("Temperature:",current_temp," C\t","Humidity:",current_hum,"%") #print current temperature and humidity
	if(current_temp > 35):	#if temperature raises above 35 C, raise an alarm
		print("!!!Alarm!!! It's too hot")
	else:
		continue
	
	

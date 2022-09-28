import random
import time
while(1):
 temp = round(random.uniform(0,50),2)
 print(temp,'temperature in celsius')
 humid = round(random.uniform(30,70),2)
 print(humid ,'humidity in percentage')
 if(temp>33):
     print('temperature is high alarm is detected It\'s like an oven out there ')
 time.sleep(5)

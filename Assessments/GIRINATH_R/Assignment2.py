import random
import time
def get_temp():
    return round(random.uniform(20,40),2) ##20 to 24 cold; 25 to 35 normal; 36 to 40 hot

def get_humidity():
    return round(random.uniform(30,80),2) ##30 to 40 low; 40 to 60 normal; 60 to 80 high

while 1:
    temp=get_temp()
    humid = get_humidity()
    print('Temperature ',temp,'C')
    print('Humidity ',humid,'%')
    if temp>35:
        print('!!ALERT!! The temperature is high.Its roasting out there..')
    time.sleep(5)
    





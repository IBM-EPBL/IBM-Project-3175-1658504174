
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import time
import sys
import ibmiotf.device
import random

organisation="js87ki"
deviceType="abcd"
deviceId="12"
authMethod="token"
authToken="12345678"

def myCommandCallback(cmd):
    print("Command Recd! %s" % cmd.data['command'])
    status=cmd.data['command']
    if status=='lighton':
        print("LED ON!")
    elif status=='lightoff':
        print("LED OFF!")
    else:
        print("Send Proper command")
try:
    deviceOptions={"org":organisation,"type":deviceType,"id":deviceId,"auth-method":authMethod,"auth-token":authToken}
    deviceCli=ibmiotf.device.Client(deviceOptions)
except Exception as e:
    print("Caught exception connecting device!")
    sys.exit()
deviceCli.connect()
while True:
    temp=random.randint(0,50)
    humid=random.randint(0,100)
    data={'temp':temp,'humid':humid}
    def myOnPublishCallback():
        print("Published Temperature =%s C" % temp,"Humidity =%s %%" % humid,"to IBM Watson")
    success=deviceCli.publishEvent("IoTSensor","json",data,qos=0,on_publish=myOnPublishCallback())
    if not success:
        print("Failed!!")
    time.sleep(10)
    deviceCli.commandCallback=myCommandCallback
deviceCli.disconnect()



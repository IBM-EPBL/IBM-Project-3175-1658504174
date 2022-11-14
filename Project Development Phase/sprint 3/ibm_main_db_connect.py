
import time
import sys
import ibmiotf.device
import random
from ibmcloudant.cloudant_v1 import Document, CloudantV1, BulkDocs
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('OiShNMZ-LVn5yaGwm89YfzSuMIkFBgE43XUFpOEMuRmE')

service = CloudantV1(authenticator=authenticator)

service.set_service_url('https://ade6d239-b201-49e3-8c8c-fd1fd9fef164-bluemix.cloudantnosqldb.appdomain.cloud')

organisation="js87ki"
deviceType="my_devices"
deviceId="1"
authMethod="token"
authToken="my_device_token"

# a-js87ki-4h8q4ploiq
# GiQhbtWSUHg1E2g3KO
lat=13.012594155082645
long=80.23527327140268
def get_bin_value_weight():
    final_value_and_weight=[]
    bin_value_list=[]
    bin_weight_list=[]
    for i in range(100):
        bin_value_list.append(random.randint(0,100))
        bin_weight_list.append(random.randint(0,25))
    bin_value_list.sort()
    bin_weight_list.sort()
    for i in range(100):
        final_value_and_weight.append([bin_value_list[i],bin_weight_list[i]])
    return final_value_and_weight



try:
    deviceOptions={"org":organisation,"type":deviceType,"id":deviceId,"auth-method":authMethod,"auth-token":authToken}
    deviceCli=ibmiotf.device.Client(deviceOptions)
except Exception as e:
    print("Caught exception connecting device!")
    sys.exit()
deviceCli.connect()

#Get initial rev value
response = service.post_all_docs(
  db='dustbin_locations',
  key='sensor_readings',
  limit=10
).get_result()
rev=response['rows'][0]['value']['rev']

while True:
    bin_value_weight=get_bin_value_weight()
    for i in bin_value_weight:
        data={'lat':lat,'long':long,'bin_value':i[0],'bin_weight':i[1]}
        products_doc = Document(
            id="sensor_readings",
            rev=rev,
            lat_1=lat,
            long_1=long,
            bin_value_1=i[0],
            bin_weight=i[1])
        def myOnPublishCallback():
            print("Published Latitude =%s" % lat ,"Longitude =%s " % long,"Bin value =%s" % i[0],"Bin weight =%s kgs  " % i[1],"to IBM Watson")
        success=deviceCli.publishEvent("IoTSensor","json",data,qos=0,on_publish=myOnPublishCallback())
        response = service.post_document(db='dustbin_locations', document=products_doc).get_result()
        rev=response['rev']
        if not success:
            print("Failed!!")
        time.sleep(1)
deviceCli.disconnect()



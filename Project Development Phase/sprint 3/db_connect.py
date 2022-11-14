from ibmcloudant.cloudant_v1 import Document, CloudantV1, BulkDocs
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('OiShNMZ-LVn5yaGwm89YfzSuMIkFBgE43XUFpOEMuRmE')

service = CloudantV1(authenticator=authenticator)

service.set_service_url('https://ade6d239-b201-49e3-8c8c-fd1fd9fef164-bluemix.cloudantnosqldb.appdomain.cloud')

products_doc = Document(
  id="sensor_readings",
  rev="7-7caf7a93de3a788129c2b55f4e3cea1f",
  lat_1="13.012594155082645",
long_1="80.23527327140268",
bin_value_1=56,
bin_weight=20)

# response = service.post_document(db='dustbin_locations', document=products_doc).get_result()
response = service.post_all_docs(
  db='dustbin_locations',
  key='sensor_readings',
  limit=10
).get_result()

print(response['rows'][0]['value']['rev'])

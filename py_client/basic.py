from sys import api_version
import requests

# endpoint ="https://github.com"
endpoint="http://httpbin.org/status/200"

endpoint="http://httpbin.org/anything"

#phone -get-->camera -->App -->API -->CAMERA
#Rest api -->web api



# rest api as web based api_version'

get_response =requests.get(endpoint)
print(get_response.text)
# the work place is calculated in ther field

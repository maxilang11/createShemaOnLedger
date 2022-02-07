import requests
import json

url = "http://router.beta.de.com:8014/schemas"

payload = json.dumps({
  "attributes": [
    "start_date",
    "expire_date",
    "label",
    "security_class"
  ],
  "schema_name": "RailChain-ICE-Internal-Sensor-Access",
  "schema_version": "1.1"
})
headers = {
  'X-API-Key': 'drom',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
#####################################################################################

url = "http://router.beta.de.com:8014/credential-definitions"

payload = json.dumps({
  "revocation_registry_size": 1000,
  "schema_id": "2jkYm5jm5SdJfx89QYYAJ2:2:RailChain-ICE-Internal-Sensor-Access:1.1",
  "support_revocation": False,
  "tag": "RailChain-ICE-Internal-Sensor-Access Ver. 1.1"
})
headers = {
  'X-API-Key': 'drom',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
#####################################################################################


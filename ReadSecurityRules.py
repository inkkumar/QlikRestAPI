import requests
import json

url = "https://dashboards.cobundu.com/meteor/qrs/systemrule/{category}/associatedrules?xrfkey=1234567890123456"

payload={}
headers = {
  'hdr-usr': '.\\bi_admin',
  'Content-Type': 'application/json',
  'x-qlik-xrfkey': '1234567890123456',
  'Cookie': 'X-Qlik-Session-meteor={23DA935C-D834-43BA-AA16-9F1ADCB88879}:280265bd-32e3-4627-ba1a-606eb320cfb1'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
